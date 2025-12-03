from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_completed', 'priority', 'deadline', 'created_at', 'reminder_sent', 'status']
        read_only_fields = ['created_at', 'reminder_sent']
