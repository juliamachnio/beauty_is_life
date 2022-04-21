from django.shortcuts import render

def requests_list(request):
    return render(request, 'jm_mn_app/requests_list.html', {})
