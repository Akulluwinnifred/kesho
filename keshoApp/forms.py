from django.forms import ModelForm
from .models import *



class BabeForm(ModelForm):
    class Meta:
        model = Babe
        fields = '__all__'

class AddPaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
