from django.shortcuts import render
from .models import RequestsRegister

def requests_list(request):
    requests_register = RequestsRegister.objects.filter(request_name="Tadataa")
    return render(request, 'jm_mn_app/requests_list.html', {'requests_register' : requests_register})
