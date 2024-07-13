from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User, Pet, Medicine, Appointment
from .forms import UserForm, PetForm, MedicineForm, AppointmentForm

'''
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

'''

from django.shortcuts import render, redirect
from .forms import UserForm

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "GET":
        name_of_owner = request.POST.get('name_of_owner')
        password = request.POST.get('password')
        user = authenticate(request, username=name_of_owner, password=password)
        if user is not None:
            login(request, user)
            return redirect('home.html')
        return render(request, 'login.html')



def pet_profile(request):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PetForm()
    return render(request, 'pet_profile.html', {'form': form})

def medicine_view(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine.html', {'medicines': medicines})

def appointment_view(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def home(request):
    return render(request, 'home.html')
