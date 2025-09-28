from rest_framework import generics
from employees.models import Employee, JobPosition
from employees.api.serializers import EmployeeSerializer, JobPositionSerializer


class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    ordering_fields = ['name', 'surname', 'hire_date']
    search_fields = ['name', 'surname', 'email']
    pagination_class = None


class EmployeeDetail(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdate(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDelete(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class JobPositionCreate(generics.CreateAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer


class JobPositionList(generics.ListAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
    ordering_fields = ['name', ]


class JobPositionDetail(generics.RetrieveAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer


class JobPositionUpdate(generics.UpdateAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer


class JobPositionDelete(generics.DestroyAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
