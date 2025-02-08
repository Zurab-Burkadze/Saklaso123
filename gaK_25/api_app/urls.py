from django.urls import path
from .views import EmployeeCreateAPIView, EmployeeRetrieveAPIView, EmployeeDestroyAPIView, EmployeeListAPIView, EmployeeUpdateAPIView

urlpatterns = [
    path('tasks/', EmployeeListAPIView.as_view(), name='task-list'),
    path('tasks/create/', EmployeeCreateAPIView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', EmployeeRetrieveAPIView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', EmployeeUpdateAPIView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', EmployeeDestroyAPIView.as_view(), name='task-delete'),
]
