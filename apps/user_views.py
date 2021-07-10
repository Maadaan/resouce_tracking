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
    context = {

    }
    return render(request, 'user/hospital_list.html', context)


def hospital_detail(request):
    context = {

    }
    return render(request, 'user/hospital_detail.html', context)


# ----------------------------------------------------------------


# ------------------------------------------------------------
def doctor_list(request):
    context = {

    }
    return render(request, 'user/doctor_list.html', context)


def doctor_detail(request):
    context = {

    }
    return render(request, 'user/doctor_detail.html', context)


# ----------------------------------------------------------------


# ------------------------------------------------------------
def volunteer_list(request):
    context = {

    }
    return render(request, 'user/volunteer_list.html', context)


def volunteer_detail(request):
    context = {

    }
    return render(request, 'user/volunteer_detail.html', context)


# ----------------------------------------------------------------


# ------------------------------------------------------------
def blood_list(request):
    context = {

    }
    return render(request, 'user/blood_list.html', context)


def blood_detail(request):
    context = {

    }
    return render(request, 'user/blood_detail.html', context)


# ----------------------------------------------------------------


# ------------------------------------------------------------
def hospital_related_list(request):
    context = {

    }
    return render(request, 'user/hospital_related_list.html', context)


def hospital_related_detail(request):
    context = {

    }
    return render(request, 'user/hospital_related_detail.html', context)
# ----------------------------------------------------------------
