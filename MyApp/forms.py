from django.forms import ModelForm
from .models import Commande,Client


class CommandeForm(ModelForm):
    class Meta:
        model=Commande
        fields='__all__'

class ClientForm(ModelForm):
    class Meta:
        model=Client
        fields='__all__'