from rest_framework import serializers
from employees.models import Employee, JobPosition


class EmployeeSerializer(serializers.ModelSerializer):
    job_position = serializers.SerializerMethodField('get_job_position')

    def get_job_position(self, obj):
        return obj.job_position.title

    class Meta:
        model = Employee
        fields = ['name', 'surname', 'email', 'job_position', 'salary', 'hire_date']


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__'
