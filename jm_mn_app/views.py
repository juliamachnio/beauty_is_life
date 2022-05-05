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



def requests_list(request):
    #requests_register = RequestsRegister.objects.filter(request_name="Tadataa")
    requests_register = RequestsRegister.objects.all()
    paginator = Paginator(requests_register, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'jm_mn_app/requests_list.html', {'requests_register': page_obj})


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
    return render(request, 'jm_mn_app/service_edit.html', {'form': form})


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
            return redirect('request_details', pk=service.pk)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'jm_mn_app/service_edit.html', {'form': form})


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('request_details', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'jm_mn_app/customer_edit.html', {'form': form})