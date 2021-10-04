from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.index, name='hospital_home'),
    path('profile', views.profile, name='hospital_profile'),
    # path('dappointment', views.AppointmentsForAPatientView.as_view(), name='doctor-view-appointment')
    path('dappointment', views.hospital_view_appointment, name='doctor-view-appointment'),
    path('appointment_approved/<int:pk>', views.hospital_approve_appointment, name='doctor-approve-appointment'),
    path('appointment_delete/<int:pk>', views.hospital_delete_appointment, name='doctor-delete-appointment')
]