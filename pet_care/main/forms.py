from django import forms
from .models import User, Pet, Medicine, Appointment



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name_of_owner', 'password', 'phone']
        widgets = {
            'password': forms.PasswordInput(),
        }


class PetForm(forms.ModelForm):
    user_phone = forms.IntegerField(widget=forms.NumberInput(), required=True)

    class Meta:
        model = Pet
        fields = ['name_of_pet', 'name_of_owner', 'user_phone']

    def clean_user_phone(self):
        phone = self.cleaned_data['user_phone']
        try:
            user = User.objects.get(phone=phone)
            return user
        except User.DoesNotExist:
            raise forms.ValidationError("User with this phone number does not exist.")




class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name_of_medicine', 'purpose_of_medicine', 'price', 'quantity']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor_name', 'specialization']
