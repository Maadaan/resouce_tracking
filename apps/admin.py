from django.contrib import admin
from .models import Hospital, Doctor, Blood, Volunteer, HospitalRelated

# Register your models here.

admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Blood)
admin.site.register(Volunteer)
admin.site.register(HospitalRelated)
