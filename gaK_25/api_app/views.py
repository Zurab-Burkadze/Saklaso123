from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Employee
from .serializer import EmployeeSerializer
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework import mixins, generics

class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        print('Override list')
        return super().list(request, *args, **kwargs)

class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        print('Override perform_create')
        return super().perform_create(serializer)

class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def retrieve(self, request, *args, **kwargs):
        print('Override retrieve')
        return super().retrieve(request, *args, **kwargs)

class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_update(self, serializer):
        print('Override perform_update')
        return super().perform_update(serializer)

class EmployeeDestroyAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()

    def perform_destroy(self, instance):
        print('Override perform_destroy')
        return super().perform_destroy(instance)



