from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    name_of_owner = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, primary_key=True)

    def __str__(self):
        return self.name_of_owner

class Pet(models.Model):
    name_of_pet = models.CharField(max_length=100)
    name_of_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    phone = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_pet

class Medicine(models.Model):
    name_of_medicine = models.CharField(max_length=100)
    purpose_of_medicine = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name_of_medicine

class Appointment(models.Model):
    doctor_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.doctor_name

