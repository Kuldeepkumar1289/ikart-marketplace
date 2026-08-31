from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Views
from products.views import product_list, product_detail
from vendors.views import vendor_dashboard, add_product
from accounts.views import user_login, vendor_register, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication & User Accounts
    path('login/', user_login, name='login'),
    path('register/vendor/', vendor_register, name='register_vendor'),
    path('logout/', user_logout, name='logout'),

    # Marketplace Storefront
    path('', product_list, name='product_list'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),

    # Vendor Dashboard
    path('vendor/dashboard/', vendor_dashboard, name='vendor_dashboard'),
    path('vendor/add-product/', add_product, name='add_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)