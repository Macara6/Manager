from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.homme,name='acceuil'),
    path('list_client/<str:pk>',views.list_client,name='list_client'),
    path('ajouter_commande/',views.ajouter_commande,name='ajouter_commande'),
    path("modifier_client/<str:pk>",views.modifier_client, name='modifier_client'),
    path('modifier_commande/<str:pk>',views.modifier_commande,name='modifier_commande'),
    path('supprimer_commande/<str:pk>',views.supprimer_commande,name='supprimer_commande'),
    path('voirRecu/<str:pk>',views.voir_commande,name='voirRecu'),
    path('ajouter_client/',views.ajouter_client,name='ajouter_client'),
    path('supprimer_client/<str:pk>',views.supprimer_client,name='supprimer_client'),
    path('clients/',views.clients,name='tout_client'),
    path('depot/',views.depots,name='tout_depots'),
   
]
