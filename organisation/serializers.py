from rest_framework import serializers
from .models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = ['id', 'name', 'description']

class EmployeeSerializer(serializers.ModelSerializer):
  department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

  class Meta:
    model = Employee
    fields = ['id', 'name', 'address', 'department']
