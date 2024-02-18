from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Commande,Client
from .forms import CommandeForm,ClientForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='acces')
def homme(request):
    commandes=Commande.objects.all().order_by('-date_time')
    clients = Client.objects.all().order_by('-date_time')
    client_total=clients.count()
    total_commande=commandes.count()
    context={'commandes':commandes,'clients':clients,'client_total':client_total,'total_commande':total_commande}

    return render(request,'acceuil.html',context)

#fonction pour ajouter le nouveau client
@login_required(login_url='acces')
def ajouter_client(request):
    form = ClientForm()
    if request.method=='POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}    
    return render(request,'ajouter_client.html',context)


@login_required(login_url='acces')
def list_client(request,pk):
    client= Client.objects.get(id=pk)
    commande=client.commande_set.all()
    commande_total=commande.count()
    context={'client':client,'commande':commande,'commande_total':commande_total}

    return render(request,'list_client.html',context)

@login_required(login_url='acces')
def ajouter_commande(request):
    form= CommandeForm()
    if request.method=='POST':
        form=CommandeForm(request.POST)
        if form .is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}    
    return render (request,'ajouter_commande.html',context)

#fonction pour modifer la comande
def modifier_commande(request,pk):
    commande= Commande.objects.get(id=pk)
    form = CommandeForm(instance=commande)
    if request.method=='POST':
        form=CommandeForm(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form} 
    return render (request,'ajouter_commande.html',context)

#fonction pour modifier le client
@login_required(login_url='acces')
def modifier_client(request,pk):
    client=Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method=='POST':
        form = ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'ajouter_client.html',context)    
#foction pour supprimer une commmande

def supprimer_commande(request,pk):
    commande=Commande.objects.get(id=pk)
    if request.method=='POST':
        commande.delete()
        return redirect('/')
    context={'item':commande}
    return render(request,'supprimer_commande.html',context)
# foction supprimer client
def supprimer_client(request,pk):
    client=Client.objects.get(id=pk)
    if request.method=='POST':
        client.delete()
        return redirect('/')
    context={'client':client,}
    return render(request,'supprimer_client.html',context)

def clients(request):
    clients= Client.objects.all().order_by('-date_time')  
    client_total=clients.count()
    context={'clients':clients,'client_total':client_total}
    return render(request,'client.html',context)

def depots(request):
   commandes=Commande.objects.all().order_by('-date_time')
   commande_total=commandes.count()
   context = {'commandes':commandes,'commande_total':commande_total}
   return render(request,'depot.html',context)


def voir_commande(request,pk):
   client= Client.objects.get(id=pk)
   commande=client.commande_set.all()
   commande_total=commande.count()
   context = {'client':client,'commande':commande,'commande_total':commande_total}
   return render(request,'recu.html',context)