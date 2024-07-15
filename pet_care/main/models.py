from django.db import models

# Create your models here.

from django.db import models

# main/models.py
from django.db import models
from django.core.exceptions import ValidationError

def validate_phone(value):
    if len(str(value)) != 10:
        raise ValidationError('Phone number must be exactly 10 digits.')

class User(models.Model):
    name_of_owner = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.BigIntegerField(primary_key=True, validators=[validate_phone])

    def __str__(self):
        return self.name_of_owner


class Pet(models.Model):
    name_of_pet = models.CharField(max_length=100)
    name_of_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    user_phone = models.ForeignKey(User, on_delete=models.CASCADE, to_field='phone')

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

