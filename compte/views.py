from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import  CreerUtilisateur
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        mon_utilisateur=User.objects.create_user(username,email,password)
        mon_utilisateur.frist_name=username
        mon_utilisateur.save()
        messages.success(request,'compte creer avec succes')

        return redirect('acces')    
    return render(request,'compte/inscription.html')

def acces(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('acceuil')
        else:
            messages.info(request,'Utilisateur et Mot de passe non trouver')
            
    return render(request,'compte/access.html')

def logoutuser(request):
    logout(request)
    return redirect('acces')