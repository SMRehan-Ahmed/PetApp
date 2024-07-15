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
    TIME_CHOICES = [
        ('09:00', '09:00 AM'),
        ('10:00', '10:00 AM'),
        ('11:00', '11:00 AM'),
        ('12:00', '12:00 PM'),
        ('13:00', '01:00 PM'),
        ('14:00', '02:00 PM'),
        ('15:00', '03:00 PM'),
        ('16:00', '04:00 PM'),
        ('17:00', '05:00 PM'),
    ]

    time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Appointment
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        appointments = Appointment.objects.all()  # Fetch all appointments
        for appointment in appointments:
            doctor_name = appointment.doctor_name
            specialization = appointment.specialization
            label = f"{doctor_name} - {specialization}"
            self.fields[f"appointment_{appointment.id}"] = forms.BooleanField(label=label, required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance