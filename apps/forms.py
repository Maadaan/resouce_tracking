from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Hospital, Doctor, Volunteer, Blood, HospitalRelated


# ---------------------------------
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# ------------------------------------------------------------------------
class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'email', 'address', 'contact_no', 'hospital_image']


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'email', 'address', 'speciality', 'nmc_no', 'doctor_image']


class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'contact_no', 'volunteer_image']


class BloodForm(ModelForm):
    class Meta:
        model = Blood
        fields = ['blood_type']


class HospitalRelatedForm(ModelForm):
    class Meta:
        model = HospitalRelated
        fields = ['has_doctor', 'has_ambulance', 'has_blood', 'has_bed', 'has_oxygen']
