from django.db import models

# Create your models here.



class Client(models.Model):
    nom=models.CharField(max_length=132)
    adresse=models.CharField(max_length=132)
    telephone=models.CharField(max_length=132)
    date_time=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural= "Clients"  
    def __str__(self):
        return self.nom  
    
class Commande(models.Model):
    client=models.ForeignKey(Client,null=True,on_delete=models.SET_NULL)
    payer= models.DecimalField(max_digits=100,decimal_places=2)
    date_time=models.DateTimeField(auto_now=True)
