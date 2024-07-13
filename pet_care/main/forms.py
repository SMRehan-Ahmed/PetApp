from django import forms
from .models import User, Pet, Medicine, Appointment

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name_of_owner', 'password', 'phone']

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name_of_pet', 'name_of_owner', 'phone']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name_of_medicine', 'purpose_of_medicine', 'price', 'quantity']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor_name', 'specialization']
