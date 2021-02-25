from django.contrib import admin
from .models import UserRecord, PersonnelRecord, Department

admin.site.register(UserRecord)
admin.site.register(PersonnelRecord)
admin.site.register(Department)
