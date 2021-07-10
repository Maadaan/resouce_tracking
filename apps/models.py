from django.db import models


# Create your models here.

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=15)
    hospital_image = models.ImageField(upload_to='hospital_image')

    def __str__(self):
        return str(self.name)


class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True, null=True)
    address = models.CharField(max_length=255)
    speciality = models.TextField()
    nmc_no = models.CharField(max_length=10)
    doctor_image = models.ImageField(upload_to='doctor_image')

    def __str__(self):
        return str(self.name)


class Volunteer(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_no = models.CharField(max_length=10)
    volunteer_image = models.ImageField(upload_to='volunteer_image')

    def __str__(self):
        return str(self.name)


blood_types = (
    ('A +', 'A positive'),
    ('B +', 'B positive'),
    ('O +', 'O positive'),
    ('AB +', 'AB positive'),

    ('A -', 'A negative'),
    ('B -', 'B negative'),
    ('O -', 'O negative'),
    ('AB -', 'AB negative'),

)


class Blood(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    blood_type = models.CharField(choices=blood_types, max_length=10)

    def __str__(self):
        return str(self.blood_type)


class HospitalRelated(models.Model):
    doctors_available = (
        ('Not Available', 'Not Available'),
        ('Available', 'Available'),

    )
    ambulance_available = (
        ('Not Available', 'Not Available'),
        ('Available', 'Available'),
    )
    blood_available = (
        ('Not Available', 'Not Available'),
        ('Available', 'Available'),
    )
    bed_available = (
        ('Not Available', 'Not Available'),
        ('Available', 'Available'),
    )
    oxygen_available = (
        ('Not Available', 'Not Available'),
        ('Available', 'Available'),
    )
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    has_doctor = models.CharField(choices=doctors_available, max_length=50, default='Not Available')
    has_ambulance = models.CharField(choices=ambulance_available, max_length=50, default='Not Available')
    has_blood = models.CharField(choices=blood_available, max_length=50, default='Not Available')
    has_bed = models.CharField(choices=bed_available, max_length=50, default='Not Available')
    has_oxygen = models.CharField(choices=oxygen_available, max_length=50, default='Not Available')
