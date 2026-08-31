from django.db import models
from django.utils.text import slugify
from django.conf import settings

class Vendor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='vendor_profile'
    )
    store_name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    store_logo = models.ImageField(upload_to='vendors/logos/', blank=True, null=True)
    commission_rate = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=10.00, 
        help_text="Platform fee percentage (e.g. 10.00 for 10%)"
    )
    is_approved = models.BooleanField(
        default=False, 
        help_text="Vendors must be verified by admin before selling"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.store_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.store_name