from django import forms
from .models import Banner, VisionMission, Statistic, Initiative

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['image', 'title', 'description', 'order', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter banner title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter banner description'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Display order (e.g., 1, 2, 3...)'
            }),
            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }

class VisionMissionForm(forms.ModelForm):
    class Meta:
        model = VisionMission
        fields = ['vision_title', 'vision_description', 'mission_title', 'mission_description']
        widgets = {
            'vision_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter vision title'
            }),
            'vision_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter vision description'
            }),
            'mission_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter mission title'
            }),
            'mission_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter mission description'
            }),
        }

class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = ['label', 'value', 'order', 'status']
        widgets = {
            'label': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Rescues Monthly'
            }),
            'value': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 500+'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Display order'
            }),
            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

class InitiativeForm(forms.ModelForm):
    class Meta:
        model = Initiative
        fields = ['title', 'description', 'image', 'order', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter initiative title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter initiative description'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Display order'
            }),
            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }