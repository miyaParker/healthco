from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserRecord, Department


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class UserRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRecord
        fields = ["patient_id", "fullname", "gender", "age", "bmi", "pregnant", "department_id", "blood_type",
                  "support_contact", "allergies"]


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ["department"]
