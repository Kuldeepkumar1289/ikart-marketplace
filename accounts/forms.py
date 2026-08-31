from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from vendors.models import Vendor

User = get_user_model()

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600/20 text-slate-800 transition',
        'placeholder': 'Enter your username or email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600/20 text-slate-800 transition',
        'placeholder': '••••••••'
    }))

class VendorRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600/20 text-slate-800 transition',
        'placeholder': 'Choose a username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600/20 text-slate-800 transition',
        'placeholder': 'business@example.com'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600/20 text-slate-800 transition',
        'placeholder': 'Create a strong password'
    }))
    store_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600/20 text-slate-800 transition',
        'placeholder': 'e.g. Acme Electronics'
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600/20 text-slate-800 transition resize-none',
        'placeholder': 'Brief description of what your store sells...',
        'rows': 3
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_vendor = True
        user.is_customer = True
        if commit:
            user.save()
            Vendor.objects.create(
                user=user,
                store_name=self.cleaned_data['store_name'],
                description=self.cleaned_data.get('description', ''),
                is_approved=True  # Set to True for testing; change to False for strict moderation
            )
        return user