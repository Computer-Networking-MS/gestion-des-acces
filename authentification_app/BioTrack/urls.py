from django.urls import path

from . import views

# URLConf  module
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.home, name='about'),
    path('attendance/', views.home, name='attendance'),
    path('preinscription/', views.student_registration, name='preinscription'),
]
