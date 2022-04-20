from django.conf import settings
from django.db import models
from django.utils import timezone

    #klient
    #usługa
    #zabiegi (harmonogram - o było i będzie)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    mail = models.EmailField()



    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.name


class Service(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.service_name


class RequestsRegister(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    service_date = models.DateTimeField(default=timezone.now)

