from django.urls import path
from . import views


urlpatterns = [
    path("patient",views.patient_form,name="patient"),
    path("doctor",views.doctor_form,name="doctor"),
    path("login",views.user_login, name="login"),
    path("<str:slug>",views.profile, name="profile")
]
