# waverlyplace/urls.py
from django.urls import path
from waverlyplace import views

urlpatterns = [
    path('place', views.HomePageView.as_view()),
]
