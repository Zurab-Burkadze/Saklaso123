from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Task
from .serializer import TaskSerializer
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework import mixins, generics

class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        print('Override list')
        return super().list(request, *args, **kwargs)

class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        print('Override perform_create')
        return super().perform_create(serializer)

class TaskRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def retrieve(self, request, *args, **kwargs):
        print('Override retrieve')
        return super().retrieve(request, *args, **kwargs)

class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_update(self, serializer):
        print('Override perform_update')
        return super().perform_update(serializer)

class TaskDestroyAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()

    def perform_archieved(self, instance):
        instance.archieved = True



