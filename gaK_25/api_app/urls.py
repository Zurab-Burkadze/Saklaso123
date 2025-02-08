from django.urls import path
from .views import TaskCreateAPIView, TaskRetrieveAPIView, TaskDestroyAPIView, TaskListAPIView, TaskUpdateAPIView

urlpatterns = [
    path('employees/', TaskListAPIView.as_view(), name='task-list'),
    path('employees/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('employees/<int:pk>/', TaskRetrieveAPIView.as_view(), name='task-detail'),
    path('employees/<int:pk>/update/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('employees/<int:pk>/delete/', TaskDestroyAPIView.as_view(), name='task-delete'),
]
