from django.shortcuts import render
from django.http import JsonResponse
from .models import Department, Employee
import json
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_department_view(req,*args,**kwargs):
  if(req.method == 'GET'):
    obj = Department.objects.all()
    json_data = list(obj.values())
    return JsonResponse(json_data, safe=False, status=200)
  
  elif(req.method == 'POST'):
    data = json.loads(req.body)
    department = Department.objects.create(name=data["name"], description=data["description"])
    return JsonResponse({"message": "Department created", "name": department.name}, status=201)
  
  else:
    return JsonResponse({"error": "Method not allowed"}, status = 405)
  
@csrf_exempt
def create_employee_view(req,*args,**kwargs):
  if(req.method == 'GET'):
    name = req.GET.get('name', None)
    department_id = req.GET.get('departmentId', None)
    
    query = Q()
    if name:
      query &= Q(name__icontains=name)
    if department_id:
      query &= Q(department_id=department_id)
      
    employees = Employee.objects.filter(query).select_related('department')
    
    employees_data = [
        {
            "id": emp.id,
            "name": emp.name,
            "address": emp.address,
            "department_id": emp.department.id if emp.department else None,
        }
        for emp in employees
    ]
    
    return JsonResponse(employees_data, safe=False, status=200)
  
  elif(req.method == 'POST'):
    data = json.loads(req.body)
    employee = Employee.objects.create(name=data["name"], address=data["address"], department_id = data["departmentId"])
    return JsonResponse({"message": "Employee created", "name": employee.name}, status=201)