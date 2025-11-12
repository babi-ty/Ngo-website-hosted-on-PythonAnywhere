from django import forms
from .models import Banner, VisionMission, Statistic, Initiative
from Homepage.models import Project, ProjectImage,PressRelease, MediaCoverage, ImageGallery, Video, MediaContact


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


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'status', 'start_date', 'end_date', 
                  'location', 'order', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image', 'is_primary']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'is_primary': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }



class PressReleaseForm(forms.ModelForm):
    class Meta:
        model = PressRelease
        fields = ['title', 'description', 'release_date', 'file', 'is_active', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter press release title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Enter description'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'value': 0}),
        }


class MediaCoverageForm(forms.ModelForm):
    class Meta:
        model = MediaCoverage
        fields = ['title', 'url', 'source', 'published_date', 'thumbnail', 'description', 'is_active', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter article title'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com/article'}),
            'source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., The Hindu'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Brief summary'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'value': 0}),
        }


class ImageGalleryForm(forms.ModelForm):
    class Meta:
        model = ImageGallery
        fields = ['image', 'title', 'description', 'category', 'date_taken', 'is_active', 'order']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter image title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional description'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'date_taken': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'value': 0}),
        }


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_url', 'embed_code', 'description', 'thumbnail', 'duration', 'uploaded_date', 'is_active', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter video title'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://youtube.com/watch?v=...'}),
            'embed_code': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional custom embed code'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Video description'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 5:30'}),
            'uploaded_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'value': 0}),
        }


class MediaContactForm(forms.ModelForm):
    class Meta:
        model = MediaContact
        fields = ['name', 'designation', 'email', 'phone', 'photo', 'bio', 'is_active', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact person name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Media Relations Officer'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'media@ngo.org'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91 XXXXXXXXXX'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Brief bio'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'value': 0}),
        }