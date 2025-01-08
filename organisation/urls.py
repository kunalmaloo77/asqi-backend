from django.urls import path
from .views import DepartmentView, EmployeeView

urlpatterns = [
  path('api/department/', DepartmentView.as_view(), name='department'),
  path('api/employee/', EmployeeView.as_view(), name='employee')
]
