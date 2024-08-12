# core/models.py
from django.db import models

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=255)
    forename = models.CharField(max_length=255)

class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=255)
    forename = models.CharField(max_length=255)

class Admission(models.Model):
    id = models.IntegerField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateField()
    discharge_date = models.DateField()

class Allocation(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    admission_id = models.ForeignKey(Admission, on_delete=models.CASCADE)
