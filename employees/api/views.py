from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage
from employees.models import Employee, JobPosition
from employees.api.serializers import EmployeeSerializer, JobPositionSerializer


class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]


class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        employees_qs = self.get_queryset().select_related('job_position').all().order_by('id')

        job_position = request.GET.get('job_position')
        if job_position:
            employees_qs = employees_qs.filter(job_position__title__icontains=job_position)

        try:
            per_page = int(request.GET.get('per_page', 10))
            if per_page <= 0 or per_page > 100:
                per_page = 10
        except ValueError:
            per_page = 10

        paginator = Paginator(employees_qs, per_page)

        page_number = request.GET.get('page', 1)

        try:
            page_obj = paginator.page(page_number)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        except Exception:
            page_obj = paginator.page(1)

        employee_data = [EmployeeSerializer(employee).data for employee in page_obj]

        response_data = {
            'count': employees_qs.count(),
            'total_pages': paginator.num_pages,
            'current_page': page_obj.number,
            'per_page': per_page,
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
            'results': employee_data,
        }

        return JsonResponse(response_data, safe=False)


class EmployeeDetail(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]


class EmployeeUpdate(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]


class EmployeeDelete(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]


class JobPositionCreate(generics.CreateAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
    permission_classes = [IsAdminUser]


class JobPositionList(generics.ListAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
    ordering_fields = ['name', ]
    permission_classes = [IsAuthenticated]


class JobPositionDetail(generics.RetrieveAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
    permission_classes = [IsAuthenticated]


class JobPositionUpdate(generics.UpdateAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
    permission_classes = [IsAdminUser]


class JobPositionDelete(generics.DestroyAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
    permission_classes = [IsAdminUser]
