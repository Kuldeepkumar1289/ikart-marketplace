from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vendor
from .forms import ProductForm
from products.models import Product

@login_required
def vendor_dashboard(request):
    vendor = get_object_or_404(Vendor, user=request.user)
    products = Product.objects.filter(vendor=vendor)
    return render(request, 'vendors/dashboard.html', {
        'vendor': vendor,
        'products': products
    })

@login_required
def add_product(request):
    vendor = get_object_or_404(Vendor, user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = vendor
            product.save()
            return redirect('vendor_dashboard')
    else:
        form = ProductForm()
    return render(request, 'vendors/add_product.html', {'form': form})