from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task


class TaskView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backend = [DjangoFilterBackend]
    filterset_fields = ['slack_name', 'track']
    
