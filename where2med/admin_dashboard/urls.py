from django.urls import path
from admin_dashboard import views

urlpatterns = [
    path('', views.index, name='index_admin_dashboard'),
]