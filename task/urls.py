from django.urls import path
from .views import TaskListCreateView, TaskDetailView, trigger_deadline_check, restore_task

urlpatterns = [
    path('check-deadlines/', trigger_deadline_check, name='trigger_deadline_check'),
    path('', TaskListCreateView.as_view(), name='task_list_create'),
    path('<int:pk>/restore/', restore_task, name='restore_task'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]
