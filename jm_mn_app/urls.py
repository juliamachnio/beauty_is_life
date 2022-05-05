from django.urls import path
from . import views

urlpatterns = [
    path('', views.requests_list, name='requests_list'),
    path('jm_mn_app/request/<int:pk>/', views.request_detail, name='request_details'),
    path('jm_mn_app/customer/<int:pk>/', views.customer_detail, name='customer_details'),
    path('jm_mn_app/service/<int:pk>/', views.service_detail, name='service_details'),
    path('jm_mn_app/request/<int:pk>/edit/', views.request_edit, name='request_edit'),
    path('jm_mn_app/service/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('jm_mn_app/customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('jm_mn_app/new_customer/', views.customer_new, name='customer_new'),
    path('jm_mn_app/new_service/', views.service_new, name='service_new'),
    path('jm_mn_app/new_request/', views.request_new, name='request_new'),
]