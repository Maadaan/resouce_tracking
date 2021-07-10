from django.urls import path
from .user_views import dashboard, hospital_list, hospital_detail, doctor_list, doctor_detail, volunteer_list, \
    volunteer_detail, blood_list, blood_detail, hospital_related_list, hospital_related_detail

urlpatterns = [
    # for admins urls

    # for users urls
    path('', dashboard, name='dashboard'),

    path('hospital_list/', hospital_list, name='hospital_list'),
    path('hospital_detail/<int:pk>/', hospital_detail, name='hospital_detail'),

    path('doctor_list/', doctor_list, name='doctor_list'),
    path('doctor_detail/<int:pk>/', doctor_detail, name='doctor_detail'),

    path('volunteer_list/', volunteer_list, name='volunteer_list'),
    path('volunteer_detail/<int:pk>/', volunteer_detail, name='volunteer_detail'),

    path('blood_list/', blood_list, name='blood_list'),
    path('blood_detail/<int:pk>/', blood_detail, name='blood_detail'),

    path('hospital_related_list/', hospital_related_list, name='hospital_related_list'),
    path('hospital_related_detail/<int:pk>/', hospital_related_detail, name='hospital_related_detail'),

]
