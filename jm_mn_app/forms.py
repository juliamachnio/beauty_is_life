from django import forms
from .models import Customer
from .models import Service
from .models import RequestsRegister


class CustomerForm(forms.ModelForm):

    class Meta:

        model = Customer
        fields = ('name', 'phone', 'mail',)


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('service_name', 'service_description', 'price', 'duration',)


class RequestForm(forms.ModelForm):

    class Meta:
        model = RequestsRegister
        fields = ('request_name', 'customer', 'service', 'service_date',)


