from django.views.generic import TemplateView
from django.urls import path, include
from .views import SignUp, Dashboard, UserList, UserRecordList, CreateRecord, DepartmentList, PatientList, LoginView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('record/patients/', CreateRecord.as_view(), name='record'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', UserList.as_view(), name='users'),
    path('records/', UserRecordList.as_view(), name='user-records'),
    path('patients/list/', PatientList.as_view(), name='patient-list'),
    path('depts/', DepartmentList.as_view(), name='depts'),
]
