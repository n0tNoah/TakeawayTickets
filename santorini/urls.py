from django.contrib import admin
from django.urls import path
from .views import indexview,loginview,dashboardview,ticketview
urlpatterns = [
    path('', indexview),
    path('login', loginview),
    path('dashboard', dashboardview),
    path('report', ticketview),
]
