from django.urls import path
from home_page import views

urlpatterns = [
    path("", views.index, name="index_home_page"),
    path("search/", views.search, name="search"),
    path("search_page/", views.search_page, name="search_page"),
]
