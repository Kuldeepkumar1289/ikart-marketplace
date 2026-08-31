from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'user', 'commission_rate', 'is_approved', 'created_at')
    list_filter = ('is_approved',)
    search_fields = ('store_name', 'user__username', 'user__email')
    list_editable = ('is_approved',)