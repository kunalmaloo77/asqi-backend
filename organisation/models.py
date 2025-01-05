from django.db import models

# Create your models here.
class Department(models.Model):
  name        = models.CharField(max_length=120)
  description = models.TextField()
  
class Employee(models.Model):
  name         = models.CharField(max_length=120)
  address      = models.TextField()
  department   = models.ForeignKey(
      Department,
      on_delete=models.CASCADE,  # Delete employees if the department is deleted
      related_name="employees",  # Enables reverse access (department.employees)
  )