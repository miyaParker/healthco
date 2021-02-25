from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from .helpers import id_generator, bmi_calculator, blood_types, disease
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .serializers import UserRecordSerializer, DepartmentSerializer, UserRecordSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .models import UserRecord, Department, PersonnelRecord


# class SignUp(View):
#     def get(self, request):
#         return render(request, 'signup.html')
#
#     def post(self, request):
#         data = request.POST.dict()
#         user = User.objects.create_user(
#             data['username'], data['email'], data['password'])
#         user.save()
#         user = User.objects.get(username=data['username'])
#         patient = Group.objects.get(name='Patients')
#         patient.user_set.add(user)
#         return HttpResponseRedirect('/login')


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        data = request.POST.dict()
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            return HttpResponseRedirect('/dashboard')
        return render(request, 'registration/login.html')


class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        data = self.request.POST.dict()
        user = User.objects.create_user(
            data['username'], data['email'], data['password'])
        user.save()
        medical_personnel = Group.objects.get(name='Medical Personnel')
        medical_personnel.user_set.add(user)
        personnel = PersonnelRecord.objects.create(user=User.objects.get(username=data['username']),
                                                   fullname=data['fullname'], personnel_id=data['personnel_id'])
        personnel.save()
        return HttpResponseRedirect('/login')


class Dashboard(View):
    template_name = 'dashboard.html'

    def patients_by_departments(self):
        depts_count = {}
        depts = Department.objects.all()
        for dept in depts:
            dept = Department.objects.get(department=dept)
            depts_count[dept.department] = dept.userrecord_set.all().count()
        return depts_count.items()

    @method_decorator(login_required)
    def get(self, request, *args):
        user = User.objects.get(username=request.user)
        medical_group = user.groups.filter(name='Medical Personnel').exists()
        if medical_group:
            depts = self.patients_by_departments()
            context = {
                'user': user,
                'patients': UserRecord.objects.all().count(),
                'doctors': PersonnelRecord.objects.all().count(),
                'depts': depts
            }
        return render(request, self.template_name, context)


class UserList(APIView):
    def get(self, request, format=None):
        users = UserRecord.objects.all()
        serializer = UserRecordSerializer(
            users, many=True, context={'request': request})
        return Response(serializer.data)


class CreateRecord(View):
    template_name = 'recordForm.html'

    def get(self, request):
        context = {
            "diseases": disease,
            "blood_types": blood_types,
            "user": request.user
        }
        return render(request, self.template_name, context)

    def post(self, request):
        data = request.POST.dict()
        pregnant_list = [True, False]
        if data['pregnant'] == "Yes":
            pregnant = pregnant_list[0]
        else:
            pregnant = pregnant_list[1]
        record = UserRecord.objects.create(user=User.objects.get(username=request.user),
                                           department=Department.objects.get(department=data['department']),
                                           fullname=data['fullname'], age=data['age'], allergies=data['allergies'],
                                           address=data['address'],
                                           blood_type=data['blood-type'], pregnant=pregnant, patient_id=id_generator(),
                                           bmi=bmi_calculator(data['weight'], data['height']), gender=data['gender'],
                                           support_contact=data['support_contact'], weight=data['weight'],
                                           height=data['height'])

        record.save()
        return HttpResponseRedirect('/dashboard')


class PatientList(View):
    template_name = 'patientList.html'

    def get(self, request):
        user = User.objects.get(username=request.user)
        group = user.groups.filter(name='Medical Personnel').exists()
        if group:
            context = {
                "patients": UserRecord.objects.all()
            }
            return render(request, self.template_name, context)
        else:
            return HttpResponseRedirect('/dashboard')


class UserRecordList(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        records = UserRecord.objects.all()
        serializer = UserRecordSerializer(
            records, many=True, context={'request': request})
        return Response(serializer.data)


class DepartmentList(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(
            departments, many=True, context={'request': request})
        return Response(serializer.data)
