from django.urls import path
from where2med_auth import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('signup_patient/', views.Signup_Patient, name='signup_patient'),
    path('signup_medical_center/', views.Signup_MedicalCenter, name='signup_medicalcenter'),
]