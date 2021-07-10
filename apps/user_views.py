from django.shortcuts import render

from .models import Hospital, Doctor, Blood, Volunteer, HospitalRelated


def dashboard(request):
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
    return render(request, 'user/dashboard.html', context)


# ------------------------------------------------------------
def hospital_list(request):
    hospitals = Hospital.objects.all()
    context = {
        'hospitals': hospitals,
    }
    return render(request, 'user/hospital_list.html', context)


def hospital_detail(request, pk):
    hospitals = Hospital.objects.get(id=pk)
    context = {
        'hospitals': hospitals,
    }
    return render(request, 'user/hospital_detail.html', context)


# ----------------------------------------------------------------


# ------------------------------------------------------------
def doctor_list(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors,
    }
    return render(request, 'user/doctor_list.html', context)


def doctor_detail(request, pk):
    doctors = Doctor.objects.get(id=pk)
    context = {
        'doctors': doctors,
    }
    return render(request, 'user/doctor_detail.html', context)


# ----------------------------------------------------------------


# ------------------------------------------------------------
def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    context = {
        'volunteers': volunteers,
    }
    return render(request, 'user/volunteer_list.html', context)


def volunteer_detail(request, pk):
    volunteers = Volunteer.objects.get(id=pk)

    context = {
        'volunteers': volunteers,
    }
    return render(request, 'user/volunteer_detail.html', context)


# ----------------------------------------------------------------


# ------------------------------------------------------------
def blood_list(request):
    bloods = Blood.objects.all()
    context = {
        'bloods': bloods,
    }
    return render(request, 'user/blood_list.html', context)


def blood_detail(request, pk):
    bloods = Blood.objects.get(id=pk)
    context = {
        'bloods': bloods,
    }
    return render(request, 'user/blood_detail.html', context)


# ----------------------------------------------------------------


# ------------------------------------------------------------
def hospital_related_list(request):
    hospital_relates = HospitalRelated.objects.all()
    context = {
        'hospital_relates': hospital_relates,
    }
    return render(request, 'user/hospital_related_list.html', context)


def hospital_related_detail(request, pk):
    hospital_relates = HospitalRelated.objects.get(id=pk)
    context = {
        'hospital_relates': hospital_relates,
    }
    return render(request, 'user/hospital_related_detail.html', context)
# ----------------------------------------------------------------
