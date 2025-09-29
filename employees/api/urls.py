from django.urls import path
from employees.api import views

urlpatterns = [
    path('', views.EmployeeList.as_view(), name='employee-list'),
    path('create/', views.EmployeeCreate.as_view(), name='employee-/create'),
    path('<int:pk>/', views.EmployeeDetail.as_view(), name='employee-detail'),
    path('<int:pk>/update/', views.EmployeeUpdate.as_view(), name='employee-update'),
    path('<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employee-delete'),
    path('job-position/list/', views.JobPositionList.as_view(), name='job-position-list'),
    path('job-position/create/', views.JobPositionCreate.as_view(), name='job-position-create'),
    path('job-position/<int:pk>/', views.JobPositionDetail.as_view(), name='job-position-detail'),
    path('job-position/<int:pk>/update/', views.JobPositionUpdate.as_view(), name='job-position-detail'),
    path('job-position/<int:pk>/delete/', views.JobPositionDelete.as_view(), name='job-position-detail'),
]
