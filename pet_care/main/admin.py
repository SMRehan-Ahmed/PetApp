from django.contrib import admin
# main/admin.py
from django.contrib import admin
from main.models import User, Pet, Medicine, Appointment

admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Medicine)
admin.site.register(Appointment)
 
# Register your models here.
