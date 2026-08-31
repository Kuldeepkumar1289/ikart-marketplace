from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomLoginForm, VendorRegistrationForm

def user_login(request):
    if request.user.is_authenticated:
        return redirect('product_list')

    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            if user.is_vendor:
                return redirect('vendor_dashboard')
            return redirect('product_list')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()

    return render(request, 'accounts/login.html', {'form': form})

def vendor_register(request):
    if request.user.is_authenticated:
        return redirect('product_list')

    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your seller account has been activated! Welcome aboard.")
            return redirect('vendor_dashboard')
        else:
            messages.error(request, "Please check the errors below.")
    else:
        form = VendorRegistrationForm()

    return render(request, 'accounts/register_vendor.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('product_list')