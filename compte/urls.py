from django.urls import path,include
from .import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('acces/',views.acces,name='acces'),
    path('quitter/',views.logoutuser,name='quitter')
]
