from django.urls import path
from .user_views import dashboard

urlpatterns = [
    # for admins urls

    # for users urls
    path('', dashboard, name='dashboard')

]
