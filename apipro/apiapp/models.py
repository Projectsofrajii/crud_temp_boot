from django.db import models

class Employee(models.Model):

    emp_id = models.CharField(unique=True,max_length=20)
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(unique=True)
    emp_contact = models.BigIntegerField(unique=True)
    class Meta:
        db_table = "employee"