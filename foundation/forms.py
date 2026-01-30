from django import forms
from .models import ContactMessage, NewsletterSubscriber, VolunteerApplication, HelpRequest


class HelpRequestForm(forms.ModelForm):
    """Form for need help page"""
    class Meta:
        model = HelpRequest
        fields = ['name', 'email', 'phone', 'help_type', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number', 'required': True}),
            'help_type': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject of Request', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your request in detail...', 'rows': 5, 'required': True}),
        }


class ContactForm(forms.ModelForm):
    """Form for contact page"""
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'required': True
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'rows': 5,
                'required': True
            }),
        }


class NewsletterForm(forms.ModelForm):
    """Form for newsletter subscription"""
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'required': True
            }),
        }


class VolunteerForm(forms.ModelForm):
    """Form for volunteer applications"""
    class Meta:
        model = VolunteerApplication
        fields = ['name', 'email', 'phone', 'skills', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number',
                'required': True
            }),
            'skills': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your skills and areas of interest',
                'rows': 3,
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Why do you want to volunteer? (Optional)',
                'rows': 4,
            }),
        }
