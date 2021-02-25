from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    department = models.CharField(max_length=40)

    def __str__(self):
        return self.department


class UserRecord(models.Model):
    fullname = models.CharField(max_length=54, null=True)
    patient_id = models.CharField(max_length=14)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    height = models.CharField(max_length=5, null=True)
    blood_type = models.CharField(max_length=3)
    weight = models.CharField(max_length=10)
    bmi = models.CharField(max_length=15, null=True)
    allergies = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200)
    support_contact = models.CharField(max_length=100)
    pregnant = models.BooleanField(null=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, related_name='user')

    def __str__(self):
        return self.fullname


class PersonnelRecord(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=15)
    personnel_id = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    fullname = models.CharField(max_length=50)

    class Meta:
        permissions = (
            ("view_patient_record", "Can view Patient Record"),
        )

    def __str__(self):
        return self.user.username
