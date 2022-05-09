from django.shortcuts import render
from .models import RequestsRegister
from .models import Service
from .models import Customer
from django.shortcuts import get_object_or_404
from .forms import CustomerForm
from .forms import ServiceForm
from .forms import RequestForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
import csv
import mimetypes
import os
from django.http.response import HttpResponse
from .filters import RequestFilter


def requests_list(request):
    #requests_register = RequestsRegister.objects.filter(request_name="Tadataa")
    requests_register = RequestsRegister.objects.all()

    myFilter = RequestFilter(request.GET, queryset=requests_register)
    requests_register = myFilter.qs

    paginator = Paginator(requests_register, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = { 'myFilter': myFilter, 'requests_register': page_obj}


    return render(request, 'jm_mn_app/requests_list.html', context)


def request_detail(request, pk):

    requests_register = get_object_or_404(RequestsRegister, pk=pk)
    return render(request, 'jm_mn_app/request_details.html', {'req': requests_register})


def customer_detail(request, pk):

    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'jm_mn_app/customer_details.html', {'req': customer})


def service_detail(request, pk):

    service = get_object_or_404(Service, pk=pk)
    return render(request, 'jm_mn_app/service_details.html', {'req': service})


def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('customer_details', pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, 'jm_mn_app/customer_edit.html',  {'form': form})


def service_new(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.save()
            return redirect('service_details', pk=service.pk)
    else:
        form = ServiceForm()

        context = {'form': form}
    return render(request, 'jm_mn_app/service_edit.html', context)


def request_new(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            requests_register = form.save(commit=False)
            requests_register.save()
            return redirect('request_details', pk=requests_register.pk)
    else:
        form = RequestForm()
    return render(request, 'jm_mn_app/request_edit.html', {'form': form})


def request_edit(request, pk):
    requests_register = get_object_or_404(RequestsRegister, pk=pk)
    if request.method == "POST":
        form = RequestForm(request.POST, instance=requests_register)
        if form.is_valid():
            requests_register = form.save(commit=False)
            requests_register.save()
            return redirect('request_details', pk=requests_register.pk)
    else:
        form = RequestForm(instance=requests_register)
    return render(request, 'jm_mn_app/request_edit.html', {'form': form})


def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            service = form.save(commit=False)
            service.save()
            return redirect('service_details', pk=service.pk)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'jm_mn_app/service_edit.html', {'form': form})


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('customer_details', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'jm_mn_app/customer_edit.html', {'form': form})


def export_customers_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Customers.csv'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Phone', 'Mail'])

    customers = Customer.objects.all()

    for customer in customers:
        writer.writerow([customer.name, customer.phone, customer.mail])

    return response


def export_services_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Services.csv'

    writer = csv.writer(response)
    writer.writerow(['Service_name', 'Service_description', 'Price', 'Duration'])

    services = Service.objects.all()

    for service in services:
        writer.writerow([service.service_name, service.service_description, service.price, service.duration])
    return response


def export_requests_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Requests.csv'

    writer = csv.writer(response)
    writer.writerow(['Request_name', 'customer', 'service', 'service_date'])

    requests = RequestsRegister.objects.all()

    for request in requests:
        writer.writerow([request.request_name, request.customer, request.service, request.service_date])
    return response


