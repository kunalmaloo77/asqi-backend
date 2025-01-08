from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DepartmentSerializer, EmployeeSerializer
from .models import Department, Employee


class DepartmentView(APIView):
  def get(self, request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message": "Department created", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def create_department_view(req,*args,**kwargs):
#   if(req.method == 'GET'):
#     obj = Department.objects.all()
#     json_data = list(obj.values())
#     return JsonResponse(json_data, safe=False, status=200)
  
#   elif(req.method == 'POST'):
#     data = json.loads(req.body)
#     department = Department.objects.create(name=data["name"], description=data["description"])
#     return JsonResponse({"message": "Department created", "name": department.name}, status=201)
  
#   else:
#     return JsonResponse({"error": "Method not allowed"}, status = 405)
  
class EmployeeView(APIView):
  def get(self, request):
    name = request.GET.get('name')
    department_id = request.GET.get('departmentId')
    
    query = Employee.objects.all()
    if name:
      query = query.filter(name__icontains=name)
    if department_id:
      query = query.filter(department_id=department_id)

    serializer = EmployeeSerializer(query, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      
    
      

# @csrf_exempt
# def create_employee_view(req,*args,**kwargs):
#   if(req.method == 'GET'):
#     name = req.GET.get('name', None)
#     department_id = req.GET.get('departmentId', None)
    
#     query = Q()
#     if name:
#       query &= Q(name__icontains=name)
#     if department_id:
#       query &= Q(department_id=department_id)
      
#     employees = Employee.objects.filter(query).select_related('department')
    
#     employees_data = [
#         {
#             "id": emp.id,
#             "name": emp.name,
#             "address": emp.address,
#             "department_id": emp.department.id if emp.department else None,
#         }
#         for emp in employees
#     ]
    
#     return JsonResponse(employees_data, safe=False, status=200)
  
#   elif(req.method == 'POST'):
#     data = json.loads(req.body)
#     employee = Employee.objects.create(name=data["name"], address=data["address"], department_id = data["departmentId"])
#     return JsonResponse({"message": "Employee created", "name": employee.name}, status=201)