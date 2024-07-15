# main/views.py
from django.shortcuts import render, redirect
from .models import User, Pet, Medicine, Appointment
from .forms import UserForm, PetForm, MedicineForm, AppointmentForm

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        try:
            user = User.objects.get(phone=phone)
            if user.name_of_owner == name and user.password == password:
                # Successfully logged in, set session and redirect to home
                request.session['user_id'] = user.phone
                return redirect('home')
            else:
                error_message = "Invalid credentials. Please try again."
        except User.DoesNotExist:
            error_message = "User does not exist. Please register."
        return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def pet_profile(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PetForm()
    return render(request, 'pet_profile.html', {'form': form})

def medicine_view(request):
    if 'user_id' not in request.session:
        return redirect('login')

    medicines = Medicine.objects.all()
    return render(request, 'medicine.html', {'medicines': medicines})

def appointment_view(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def home(request):
    if 'user_id' not in request.session:
        return redirect('login')
    return render(request, 'home.html')



def diet_plan(request):
    return render(request,'diet_plan.html')