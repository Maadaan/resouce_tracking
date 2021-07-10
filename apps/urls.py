from django.urls import path
from .user_views import dashboard, hospital_list, hospital_detail, doctor_list, doctor_detail, volunteer_list, \
    volunteer_detail, blood_list, blood_detail, hospital_related_list, hospital_related_detail

from .views import login_view, register_view, admin_hospital_list, admin_hospital_detail, admin_hospital_create, \
    admin_hospital_update, admin_hospital_delete, admin_home, admin_hospital_related_delete, admin_doctor_delete, \
    admin_blood_delete, admin_blood_update, admin_blood_list, admin_blood_detail, admin_blood_create, \
    admin_doctor_update, admin_doctor_list, admin_doctor_detail, admin_doctor_create, admin_volunteer_create, \
    admin_volunteer_list, admin_volunteer_delete, admin_volunteer_update, admin_volunteer_detail, \
    admin_hospital_related_create, admin_hospital_related_update, admin_hospital_related_detail, \
    admin_hospital_related_list

urlpatterns = [
    # for admins urls
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('admin_home/', admin_home, name='admin_home'),
    # hospital
    path('admin_hospital_list', admin_hospital_list, name='admin_hospital_list'),
    path('admin_hospital_detail/<int:pk>/', admin_hospital_detail, name='admin_hospital_detail'),
    path('admin_hospital_create/', admin_hospital_create, name='admin_hospital_create'),
    path('admin_hospital_update/<int:pk>/', admin_hospital_update, name='admin_hospital_update'),
    path('admin_hospital_delete/<int:pk>/', admin_hospital_delete, name='admin_hospital_delete'),

    # doctor
    path('admin_doctor_list', admin_doctor_list, name='admin_doctor_list'),
    path('admin_doctor_detail/<int:pk>/', admin_doctor_detail, name='admin_doctor_detail'),
    path('admin_doctor_create/', admin_doctor_create, name='admin_doctor_create'),
    path('admin_doctor_update/<int:pk>/', admin_doctor_update, name='admin_doctor_update'),
    path('admin_doctor_delete/<int:pk>/', admin_doctor_delete, name='admin_doctor_delete'),

    # volunteer
    path('admin_volunteer_list', admin_volunteer_list, name='admin_volunteer_list'),
    path('admin_volunteer_detail/<int:pk>/', admin_volunteer_detail, name='admin_volunteer_detail'),
    path('admin_volunteer_create/', admin_volunteer_create, name='admin_volunteer_create'),
    path('admin_volunteer_update/<int:pk>/', admin_volunteer_update, name='admin_volunteer_update'),
    path('admin_volunteer_delete/<int:pk>/', admin_volunteer_delete, name='admin_volunteer_delete'),

    # blood
    path('admin_blood_list', admin_blood_list, name='admin_blood_list'),
    path('admin_blood_detail/<int:pk>/', admin_blood_detail, name='admin_blood_detail'),
    path('admin_blood_create/', admin_blood_create, name='admin_blood_create'),
    path('admin_blood_update/<int:pk>/', admin_blood_update, name='admin_blood_update'),
    path('admin_blood_delete/<int:pk>/', admin_blood_delete, name='admin_blood_delete'),

    # hospital related
    path('admin_hospital_related_list', admin_hospital_related_list, name='admin_hospital_related_list'),
    path('admin_hospital_related_detail/<int:pk>/', admin_hospital_related_detail,
         name='admin_hospital_related_detail'),
    path('admin_hospital_related_create/', admin_hospital_related_create, name='admin_hospital_related_create'),
    path('admin_hospital_related_update/<int:pk>/', admin_hospital_related_update,
         name='admin_hospital_related_update'),
    path('admin_hospital_related_delete/<int:pk>/', admin_hospital_related_delete,
         name='admin_hospital_related_delete'),

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
