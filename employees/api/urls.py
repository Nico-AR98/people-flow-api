from django.urls import path
from employees.api.views import (
    EmployeeCreate,
    EmployeeList,
    EmployeeDetail,
    EmployeeUpdate,
    EmployeeDelete,
)

urlpatterns = [
    path('', EmployeeList.as_view(), name='employee-list'),
    path('create/', EmployeeCreate.as_view(), name='employee-create'),
    path('<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('<int:pk>/update/', EmployeeUpdate.as_view(), name='employee-update'),
    path('<int:pk>/delete/', EmployeeDelete.as_view(), name='employee-delete'),
]
