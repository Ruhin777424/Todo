from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .tasks import check_deadlines

def home(request):
    return render(request, 'index.html')


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def trigger_deadline_check(request):
    """Manually trigger deadline email check"""
    try:
        result = check_deadlines()
        return Response({'message': result, 'status': 'success'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# 🔥 API VIEW — LIST + CREATE
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Task.objects.filter(user=self.request.user)

        # Filter by priority if provided (accepts numeric or name)
        priority = self.request.query_params.get('priority')
        if priority:
            mapping = {'low': Task.PRIORITY_LOW, 'medium': Task.PRIORITY_MEDIUM, 'high': Task.PRIORITY_HIGH}
            try:
                # allow numeric priority
                p = int(priority)
            except Exception:
                p = mapping.get(priority.lower())
            if p:
                qs = qs.filter(priority=p)

        # Filter by status (default to active)
        task_status = self.request.query_params.get('status', Task.STATUS_ACTIVE)
        if task_status:
            qs = qs.filter(status=task_status)

        # Ordering support: ?ordering=priority or ?ordering=-deadline etc.
        ordering = self.request.query_params.get('ordering')
        if ordering:
            qs = qs.order_by(ordering)

        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 🔥 API VIEW — GET + UPDATE + DELETE
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """Override delete to mark as deleted instead of hard delete"""
        task = self.get_object()
        task.status = Task.STATUS_DELETED
        task.save()
        return Response({'message': 'Task moved to trash'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def restore_task(request, pk):
    """Restore a task from archive or trash"""
    try:
        task = Task.objects.get(pk=pk, user=request.user)
        task.status = Task.STATUS_ACTIVE
        task.is_completed = False
        task.save()
        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
