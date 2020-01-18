from django.urls import path
from scheduling import views

urlpatterns = [
    path('', views.index, name='index_scheduling'),
]