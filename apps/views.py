from django.contrib import messages
from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm, HospitalForm, DoctorForm, BloodForm, VolunteerForm, HospitalRelatedForm
from .models import Doctor, HospitalRelated, Hospital, Blood, Volunteer


# Create your views here.
def admin_home(request):
    hospitals = Hospital.objects.all()
    doctors = Doctor.objects.all()
    volunteers = Volunteer.objects.all()
    bloods = Blood.objects.all()
    hospital_relates = HospitalRelated.objects.all()
    context = {
        'hospitals': hospitals,
        'doctors': doctors,
        'volunteers': volunteers,
        'bloods': bloods,
        'hospital_relates': hospital_relates,
    }
    return render(request, 'apps/admin_home.html', context)


# --------------------------------------------------------------------

# register

def register_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'apps/register.html', context)


# login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Incorrect UserName or Incorrect Password')
        else:
            messages.error(request, 'Fill out the fields')
    context = {
    }
    return render(request, 'apps/login.html', context)


# logout
def logout(request):
    logout(request)
    return redirect('home')


# -----------------------------------------------------------------------

# hospital views
def admin_hospital_list(request):
    hospitals = Hospital.objects.all()
    context = {
        'hospitals': hospitals,
    }
    return render(request, 'apps/admin_hospital_list.html', context)


def admin_hospital_detail(request, pk):
    hospitals = Hospital.objects.get(id=pk)
    context = {
        'hospitals': hospitals,
    }
    return render(request, 'apps/admin_hospital_detail.html', context)


def admin_hospital_create(request):
    form = HospitalForm()
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin_hospital_list')
    else:
        form = HospitalForm()
    context = {
        'form': form,
    }
    return render(request, 'apps/admin_hospital_create.html', context)


def admin_hospital_update(request, pk):
    hospitals = Hospital.objects.get(id=pk)
    form = HospitalForm(instance=hospitals)

    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospitals)
        if form.is_valid():
            form.save()
            return redirect('/admin_hospital_list')

    context = {
        'hospitals': hospitals,

        'form': form,
    }
    return render(request, 'apps/admin_hospital_update.html', context)


def admin_hospital_delete(request, pk):
    hospitals = Hospital.objects.get(id=pk)
    if request.method == 'POST':
        hospitals.delete()
        return redirect('/admin_hospital_list')
    context = {
        'hospitals': hospitals
    }
    return render(request, 'apps/admin_hospital_delete.html', context)


# -----------------------------------------doctors views -----------------------------------------
def admin_doctor_list(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors,
    }
    return render(request, 'apps/admin_doctor_list.html', context)


def admin_doctor_detail(request, pk):
    doctors = Doctor.objects.get(id=pk)
    context = {
        'doctors': doctors,
    }
    return render(request, 'apps/admin_doctor_detail.html', context)


def admin_doctor_create(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin_doctor_list')
    else:
        form = DoctorForm()
    context = {
        'form': form,
    }
    return render(request, 'apps/admin_doctor_create.html', context)


def admin_doctor_update(request, pk):
    doctors = Doctor.objects.get(id=pk)
    form = DoctorForm(instance=doctors)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctors)
        if form.is_valid():
            form.save()
            return redirect('/admin_doctor_list')

    context = {
        'doctors': doctors,
        'form': form,
    }
    return render(request, 'apps/admin_doctor_update.html', context)


def admin_doctor_delete(request, pk):
    doctors = Doctor.objects.get(id=pk)
    if request.method == 'POST':
        doctors.delete()
        return redirect('/admin_hospital_list')
    context = {
        'doctors': doctors
    }
    return render(request, 'apps/admin_doctors_delete.html', context)


# -------------------------------
# ------blood views--------------

def admin_blood_list(request):
    bloods = Blood.objects.all()
    context = {
        'bloods': bloods,
    }
    return render(request, 'apps/admin_blood_list.html', context)


def admin_blood_detail(request, pk):
    bloods = Blood.objects.get(id=pk)
    context = {
        'bloods': bloods,
    }
    return render(request, 'apps/admin_blood_detail.html', context)


def admin_blood_create(request):
    form = BloodForm()
    if request.method == 'POST':
        form = BloodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin_blood_list')
    else:
        form = BloodForm()
    context = {
        'form': form,
    }
    return render(request, 'apps/admin_blood_create.html', context)


def admin_blood_update(request, pk):
    bloods = Blood.objects.get(id=pk)
    form = DoctorForm(instance=bloods)

    if request.method == 'POST':
        form = BloodForm(request.POST, instance=bloods)
        if form.is_valid():
            form.save()
            return redirect('/admin_blood_list')

    context = {
        'bloods': bloods,
        'form': form,
    }
    return render(request, 'apps/admin_blood_update.html', context)


def admin_blood_delete(request, pk):
    bloods = Blood.objects.get(id=pk)
    if request.method == 'POST':
        bloods.delete()
        return redirect('/admin_blood_list')
    context = {
        'bloods': bloods
    }
    return render(request, 'apps/admin_blood_delete.html', context)


# ----------------------volunteer

def admin_volunteer_list(request):
    volunteers = Volunteer.objects.all()
    context = {
        'volunteers': volunteers,
    }
    return render(request, 'apps/admin_volunteer_list.html', context)


def admin_volunteer_detail(request, pk):
    volunteers = Volunteer.objects.get(id=pk)
    context = {
        'volunteers': volunteers,
    }
    return render(request, 'apps/admin_volunteer_detail.html', context)


def admin_volunteer_create(request):
    form = VolunteerForm()
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin_volunteer_list')
    else:
        form = VolunteerForm()
    context = {
        'form': form,
    }
    return render(request, 'apps/admin_volunteer_create.html', context)


def admin_volunteer_update(request, pk):
    volunteers = Volunteer.objects.get(id=pk)
    form = VolunteerForm(instance=volunteers)

    if request.method == 'POST':
        form = VolunteerForm(request.POST, instance=volunteers)
        if form.is_valid():
            form.save()
            return redirect('/admin_volunteer_list')

    context = {
        'volunteers': volunteers,
        'form': form,
    }
    return render(request, 'apps/admin_volunteer_update.html', context)


def admin_volunteer_delete(request, pk):
    volunteers = Volunteer.objects.get(id=pk)
    if request.method == 'POST':
        volunteers.delete()
        return redirect('/admin_volunteer_list')
    context = {
        'volunteers': volunteers,
    }
    return render(request, 'apps/admin_volunteer_delete.html', context)


# ---------------------hospital related


def admin_hospital_related_list(request):
    hospital_relates = HospitalRelated.objects.all()
    context = {
        'hospital_relates': hospital_relates,
    }
    return render(request, 'apps/admin_hospital_related_list.html', context)


def admin_hospital_related_detail(request, pk):
    hospital_relates = HospitalRelated.objects.get(id=pk)
    context = {
        'hospital_relates': hospital_relates,
    }
    return render(request, 'apps/admin_hospital_related_detail.html', context)


def admin_hospital_related_create(request):
    form = HospitalRelated()
    if request.method == 'POST':
        form = HospitalRelated(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin_hospital_related_list')
    else:
        form = HospitalRelated()
    context = {
        'form': form,
    }
    return render(request, 'apps/admin_hospital_related_create.html', context)


def admin_hospital_related_update(request, pk):
    hospital_relates = HospitalRelated.objects.get(id=pk)
    form = HospitalRelatedForm(instance=hospital_relates)

    if request.method == 'POST':
        form = HospitalRelatedForm(request.POST, instance=hospital_relates)
        if form.is_valid():
            form.save()
            return redirect('/admin_hospital_related_list')

    context = {
        'hospital_relates': hospital_relates,
        'form': form,
    }
    return render(request, 'apps/admin_hospital_related_update.html', context)


def admin_hospital_related_delete(request, pk):
    hospital_relates = HospitalRelated.objects.get(id=pk)
    if request.method == 'POST':
        hospital_relates.delete()
        return redirect('/admin_hospital_related_list')
    context = {
        'hospital_relates': hospital_relates,
    }
    return render(request, 'apps/admin_volunteer_delete.html', context)
