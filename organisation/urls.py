from django.urls import path

from . import views

urlpatterns = [
  path('api/department/', views.create_department_view),
  path('api/employee/', views.create_employee_view)
]
