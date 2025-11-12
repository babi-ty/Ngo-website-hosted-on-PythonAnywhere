from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from Homepage.models import Banner, VisionMission, Statistic, Initiative
from .forms import BannerForm, VisionMissionForm, StatisticForm, InitiativeForm
from Homepage.models import Project, ProjectImage
from .forms import ProjectForm, ProjectImageForm
from django.forms import modelformset_factory
from django.core.validators import URLValidator
from Homepage.models import PressRelease, MediaCoverage, ImageGallery, Video, MediaContact
from .forms import PressReleaseForm, MediaCoverageForm, ImageGalleryForm, VideoForm, MediaContactForm

# ==================== PUBLIC PAGES ====================

def Home(request):
    """Homepage view"""
    banners = Banner.objects.filter(status=True).order_by('order')
    vision_mission = VisionMission.objects.first()
    statistics = Statistic.objects.filter(status=True).order_by('order')
    initiatives = Initiative.objects.filter(status=True).order_by('order')
    projects = Project.objects.filter(is_active=True).order_by('order')

    
    context = {
        'banners': banners,
        'vision_mission': vision_mission,
        'statistics': statistics,
        'initiatives': initiatives,
        'projects': projects,
    }
    return render(request, 'index.html', context)

def rescue_page(request):
    return render(request, 'rescue.html')

def surgery_page(request):
    return render(request, 'abc_surgery.html')  

def adopt_page(request):
    return render(request, 'adopt.html')

def volunteer_page(request):
    return render(request, 'volunteer.html')

def donate_page(request):
    return render(request, 'donate.html')

def who_are_we_page(request):
    return render(request, 'who_are_we.html')

def what_we_do_page(request):
    return render(request, 'what_we_do.html')

def ways_to_help_page(request):
    return render(request, 'ways_to_help.html')


# ==================== DASHBOARD HOME ====================

@staff_member_required(login_url='/auth/login/')
def dashboard_home(request):
    """Dashboard overview"""
    context = {
        'total_banners': Banner.objects.count(),
        'total_statistics': Statistic.objects.count(),
        'total_initiatives': Initiative.objects.count(),
        'vision_mission_exists': VisionMission.objects.exists(),
    }
    return render(request, 'dashboard/home.html', context)


# ==================== BANNER MANAGEMENT ====================

@staff_member_required(login_url='/auth/login/')
def manage_image_slider(request):
    """List all banners"""
    banners = Banner.objects.all().order_by('order')
    return render(request, 'dashboard/manage_slider.html', {'banners': banners})

@staff_member_required(login_url='/auth/login/')
def manage_slider_add(request):
    """Add new banner"""
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Banner added successfully!')
            return redirect('dashboard_manage_slider')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BannerForm()
    return render(request, 'dashboard/slider_form.html', {'form': form, 'action': 'Add'})

@staff_member_required(login_url='/auth/login/')
def manage_slider_edit(request, pk):
    """Edit existing banner"""
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            messages.success(request, 'Banner updated successfully!')
            return redirect('dashboard_manage_slider')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BannerForm(instance=banner)
    return render(request, 'dashboard/slider_form.html', {'form': form, 'action': 'Edit'})

@staff_member_required(login_url='/auth/login/')
def manage_slider_delete(request, pk):
    """Delete banner"""
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        banner.delete()
        messages.success(request, 'Banner deleted successfully!')
        return redirect('dashboard_manage_slider')
    return render(request, 'dashboard/confirm_delete.html', {'object': banner, 'type': 'Banner'})


# ==================== STATISTIC MANAGEMENT ====================

@staff_member_required(login_url='/auth/login/')
def manage_statistic(request):
    """List all statistics"""
    statistics = Statistic.objects.all().order_by('order')
    return render(request, 'dashboard/manage_statistic.html', {'statistics': statistics})

@staff_member_required(login_url='/auth/login/')
def manage_statistic_add(request):
    """Add new statistic"""
    if request.method == 'POST':
        form = StatisticForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Statistic added successfully!')
            return redirect('dashboard_manage_statistic')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StatisticForm()
    return render(request, 'dashboard/statistic_form.html', {'form': form, 'action': 'Add'})

@staff_member_required(login_url='/auth/login/')
def manage_statistic_edit(request, pk):
    """Edit existing statistic"""
    statistic = get_object_or_404(Statistic, pk=pk)
    if request.method == 'POST':
        form = StatisticForm(request.POST, instance=statistic)
        if form.is_valid():
            form.save()
            messages.success(request, 'Statistic updated successfully!')
            return redirect('dashboard_manage_statistic')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StatisticForm(instance=statistic)
    return render(request, 'dashboard/statistic_form.html', {'form': form, 'action': 'Edit'})

@staff_member_required(login_url='/auth/login/')
def manage_statistic_delete(request, pk):
    """Delete statistic"""
    statistic = get_object_or_404(Statistic, pk=pk)
    if request.method == 'POST':
        statistic.delete()
        messages.success(request, 'Statistic deleted successfully!')
        return redirect('dashboard_manage_statistic')
    return render(request, 'dashboard/confirm_delete.html', {'object': statistic, 'type': 'Statistic'})


# ==================== VISION & MISSION MANAGEMENT ====================

@staff_member_required(login_url='/auth/login/')
def manage_vision(request):
    """Manage Vision & Mission (single entry)"""
    vision_mission = VisionMission.objects.first()
    
    if request.method == 'POST':
        form = VisionMissionForm(request.POST, instance=vision_mission)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vision & Mission updated successfully!')
            return redirect('dashboard_home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = VisionMissionForm(instance=vision_mission)
    
    return render(request, 'dashboard/vision_form.html', {'form': form})


# ==================== INITIATIVE MANAGEMENT ====================

@staff_member_required(login_url='/auth/login/')
def manage_initiative(request):
    """List all initiatives"""
    initiatives = Initiative.objects.all().order_by('order')
    return render(request, 'dashboard/manage_initiative.html', {'initiatives': initiatives})

@staff_member_required(login_url='/auth/login/')
def manage_initiative_add(request):
    """Add new initiative"""
    if request.method == 'POST':
        form = InitiativeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Initiative added successfully!')
            return redirect('dashboard_manage_initiative')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = InitiativeForm()
    return render(request, 'dashboard/initiative_form.html', {'form': form, 'action': 'Add'})

@staff_member_required(login_url='/auth/login/')
def manage_initiative_edit(request, pk):
    """Edit existing initiative"""
    initiative = get_object_or_404(Initiative, pk=pk)
    if request.method == 'POST':
        form = InitiativeForm(request.POST, request.FILES, instance=initiative)
        if form.is_valid():
            form.save()
            messages.success(request, 'Initiative updated successfully!')
            return redirect('dashboard_manage_initiative')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = InitiativeForm(instance=initiative)
    return render(request, 'dashboard/initiative_form.html', {'form': form, 'action': 'Edit'})

@staff_member_required(login_url='/auth/login/')
def manage_initiative_delete(request, pk):
    """Delete initiative"""
    initiative = get_object_or_404(Initiative, pk=pk)
    if request.method == 'POST':
        initiative.delete()
        messages.success(request, 'Initiative deleted successfully!')
        return redirect('dashboard_manage_initiative')
    return render(request, 'dashboard/confirm_delete.html', {'object': initiative, 'type': 'Initiative'})

# ==================== PROJECT MANAGEMENT ====================

@staff_member_required(login_url='/auth/login/')
def manage_project(request):
    """List all projects"""
    projects = Project.objects.all().order_by('order')
    return render(request, 'dashboard/manage_project.html', {'projects': projects})


@staff_member_required(login_url='/auth/login/')
def manage_project_add(request):
    """Add new project"""
    ImageFormSet = modelformset_factory(ProjectImage, form=ProjectImageForm, extra=3, can_delete=True)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=ProjectImage.objects.none())
        
        if form.is_valid() and formset.is_valid():
            project = form.save()
            
            for image_form in formset:
                if image_form.cleaned_data.get('image'):
                    image = image_form.save(commit=False)
                    image.project = project
                    image.save()
            
            messages.success(request, 'Project added successfully!')
            return redirect('dashboard_manage_project')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProjectForm()
        formset = ImageFormSet(queryset=ProjectImage.objects.none())
    
    return render(request, 'dashboard/project_form.html', {
        'form': form,
        'formset': formset,
        'action': 'Add'
    })


@staff_member_required(login_url='/auth/login/')
def manage_project_edit(request, pk):
    """Edit existing project"""
    project = get_object_or_404(Project, pk=pk)
    ImageFormSet = modelformset_factory(ProjectImage, form=ProjectImageForm, extra=1, can_delete=True)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        formset = ImageFormSet(request.POST, request.FILES, queryset=project.images.all())
        
        if form.is_valid() and formset.is_valid():
            form.save()
            
            for image_form in formset:
                if image_form.cleaned_data.get('DELETE'):
                    if image_form.instance.pk:
                        image_form.instance.delete()
                elif image_form.cleaned_data.get('image'):
                    image = image_form.save(commit=False)
                    image.project = project
                    image.save()
            
            messages.success(request, 'Project updated successfully!')
            return redirect('dashboard_manage_project')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProjectForm(instance=project)
        formset = ImageFormSet(queryset=project.images.all())
    
    return render(request, 'dashboard/project_form.html', {
        'form': form,
        'formset': formset,
        'action': 'Edit',
        'project': project
    })


@staff_member_required(login_url='/auth/login/')
def manage_project_delete(request, pk):
    """Delete project"""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('dashboard_manage_project')
    return render(request, 'dashboard/confirm_delete.html', {
        'object': project,
        'type': 'Project'
    })


@staff_member_required(login_url='/auth/login/')
def dashboard_home(request):
    """Dashboard overview - UPDATED"""
    context = {
        'total_banners': Banner.objects.count(),
        'total_statistics': Statistic.objects.count(),
        'total_initiatives': Initiative.objects.count(),
        'total_projects': Project.objects.count(),  # NEW
        'vision_mission_exists': VisionMission.objects.exists(),
    }
    return render(request, 'dashboard/home.html', context)

# ==================== PUBLIC MEDIA PAGE ====================

def media_page(request):
    """Public media page displaying all media content"""
    press_releases = PressRelease.objects.filter(is_active=True)[:6]
    media_coverage = MediaCoverage.objects.filter(is_active=True)[:6]
    gallery_images = ImageGallery.objects.filter(is_active=True)[:12]
    videos = Video.objects.filter(is_active=True)[:6]
    media_contacts = MediaContact.objects.filter(is_active=True)
    
    context = {
        'press_releases': press_releases,
        'media_coverage': media_coverage,
        'gallery_images': gallery_images,
        'videos': videos,
        'media_contacts': media_contacts,
    }
    return render(request, 'dashboard/media.html', context)

# ==================== PRESS RELEASE MANAGEMENT ====================

@staff_member_required(login_url='/auth/login/')
def manage_press_release(request):
    """List all press releases"""
    press_releases = PressRelease.objects.all()
    return render(request, 'dashboard/manage_press_release.html', {'press_releases': press_releases})

@staff_member_required(login_url='/auth/login/')
def manage_press_release_add(request):
    """Add new press release"""
    if request.method == 'POST':
        form = PressReleaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Press release added successfully!')
            return redirect('dashboard_manage_press_release')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PressReleaseForm()
    return render(request, 'dashboard/press_release_form.html', {'form': form, 'action': 'Add'})

@staff_member_required(login_url='/auth/login/')
def manage_press_release_edit(request, pk):
    """Edit existing press release"""
    press_release = get_object_or_404(PressRelease, pk=pk)
    if request.method == 'POST':
        form = PressReleaseForm(request.POST, request.FILES, instance=press_release)
        if form.is_valid():
            form.save()
            messages.success(request, 'Press release updated successfully!')
            return redirect('dashboard_manage_press_release')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PressReleaseForm(instance=press_release)
    return render(request, 'dashboard/press_release_form.html', {'form': form, 'action': 'Edit'})

@staff_member_required(login_url='/auth/login/')
def manage_press_release_delete(request, pk):
    """Delete press release"""
    press_release = get_object_or_404(PressRelease, pk=pk)
    if request.method == 'POST':
        press_release.delete()
        messages.success(request, 'Press release deleted successfully!')
        return redirect('dashboard_manage_press_release')
    return render(request, 'dashboard/confirm_delete.html', {'object': press_release, 'type': 'Press Release'})


# ==================== MEDIA COVERAGE MANAGEMENT ====================

@staff_member_required(login_url='/auth/login/')
def manage_media_coverage(request):
    """List all media coverage"""
    media_coverage = MediaCoverage.objects.all()
    return render(request, 'dashboard/manage_media_coverage.html', {'media_coverage': media_coverage})

@staff_member_required(login_url='/auth/login/')
def manage_media_coverage_add(request):
    """Add new media coverage"""
    if request.method == 'POST':
        form = MediaCoverageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Media coverage added successfully!')
            return redirect('dashboard_manage_media_coverage')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MediaCoverageForm()
    return render(request, 'dashboard/media_coverage_form.html', {'form': form, 'action': 'Add'})

@staff_member_required(login_url='/auth/login/')
def manage_media_coverage_edit(request, pk):
    """Edit existing media coverage"""
    media_coverage = get_object_or_404(MediaCoverage, pk=pk)
    if request.method == 'POST':
        form = MediaCoverageForm(request.POST, request.FILES, instance=media_coverage)
        if form.is_valid():
            form.save()
            messages.success(request, 'Media coverage updated successfully!')
            return redirect('dashboard_manage_media_coverage')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MediaCoverageForm(instance=media_coverage)
    return render(request, 'dashboard/media_coverage_form.html', {'form': form, 'action': 'Edit'})

@staff_member_required(login_url='/auth/login/')
def manage_media_coverage_delete(request, pk):
    """Delete media coverage"""
    media_coverage = get_object_or_404(MediaCoverage, pk=pk)
    if request.method == 'POST':
        media_coverage.delete()
        messages.success(request, 'Media coverage deleted successfully!')
        return redirect('dashboard_manage_media_coverage')
    return render(request, 'dashboard/confirm_delete.html', {'object': media_coverage, 'type': 'Media Coverage'})


# ==================== IMAGE GALLERY MANAGEMENT ====================

@staff_member_required(login_url='/auth/login/')
def manage_gallery(request):
    """List all gallery images"""
    gallery_images = ImageGallery.objects.all()
    return render(request, 'dashboard/manage_gallery.html', {'gallery_images': gallery_images})

@staff_member_required(login_url='/auth/login/')
def manage_gallery_add(request):
    """Add new gallery image"""
    if request.method == 'POST':
        form = ImageGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image added to gallery successfully!')
            return redirect('dashboard_manage_gallery')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ImageGalleryForm()
    return render(request, 'dashboard/gallery_form.html', {'form': form, 'action': 'Add'})

@staff_member_required(login_url='/auth/login/')
def manage_gallery_edit(request, pk):
    """Edit existing gallery image"""
    gallery_image = get_object_or_404(ImageGallery, pk=pk)
    if request.method == 'POST':
        form = ImageGalleryForm(request.POST, request.FILES, instance=gallery_image)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gallery image updated successfully!')
            return redirect('dashboard_manage_gallery')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ImageGalleryForm(instance=gallery_image)
    return render(request, 'dashboard/gallery_form.html', {'form': form, 'action': 'Edit'})

@staff_member_required(login_url='/auth/login/')
def manage_gallery_delete(request, pk):
    """Delete gallery image"""
    gallery_image = get_object_or_404(ImageGallery, pk=pk)
    if request.method == 'POST':
        gallery_image.delete()
        messages.success(request, 'Gallery image deleted successfully!')
        return redirect('dashboard_manage_gallery')
    return render(request, 'dashboard/confirm_delete.html', {'object': gallery_image, 'type': 'Gallery Image'})


# ==================== VIDEO MANAGEMENT ====================

@staff_member_required(login_url='/auth/login/')
def manage_video(request):
    """List all videos"""
    videos = Video.objects.all()
    return render(request, 'dashboard/manage_video.html', {'videos': videos})

@staff_member_required(login_url='/auth/login/')
def manage_video_add(request):
    """Add new video"""
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video added successfully!')
            return redirect('dashboard_manage_video')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = VideoForm()
    return render(request, 'dashboard/video_form.html', {'form': form, 'action': 'Add'})

@staff_member_required(login_url='/auth/login/')
def manage_video_edit(request, pk):
    """Edit existing video"""
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video updated successfully!')
            return redirect('dashboard_manage_video')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = VideoForm(instance=video)
    return render(request, 'dashboard/video_form.html', {'form': form, 'action': 'Edit'})

@staff_member_required(login_url='/auth/login/')
def manage_video_delete(request, pk):
    """Delete video"""
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        messages.success(request, 'Video deleted successfully!')
        return redirect('dashboard_manage_video')
    return render(request, 'dashboard/confirm_delete.html', {'object': video, 'type': 'Video'})


# ==================== MEDIA CONTACT MANAGEMENT ====================

@staff_member_required(login_url='/auth/login/')
def manage_media_contact(request):
    """List all media contacts"""
    media_contacts = MediaContact.objects.all()
    return render(request, 'dashboard/manage_media_contact.html', {'media_contacts': media_contacts})

@staff_member_required(login_url='/auth/login/')
def manage_media_contact_add(request):
    """Add new media contact"""
    if request.method == 'POST':
        form = MediaContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Media contact added successfully!')
            return redirect('dashboard_manage_media_contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MediaContactForm()
    return render(request, 'dashboard/media_contact_form.html', {'form': form, 'action': 'Add'})

@staff_member_required(login_url='/auth/login/')
def manage_media_contact_edit(request, pk):
    """Edit existing media contact"""
    media_contact = get_object_or_404(MediaContact, pk=pk)
    if request.method == 'POST':
        form = MediaContactForm(request.POST, request.FILES, instance=media_contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Media contact updated successfully!')
            return redirect('dashboard_manage_media_contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MediaContactForm(instance=media_contact)
    return render(request, 'dashboard/media_contact_form.html', {'form': form, 'action': 'Edit'})

@staff_member_required(login_url='/auth/login/')
def manage_media_contact_delete(request, pk):
    """Delete media contact"""
    media_contact = get_object_or_404(MediaContact, pk=pk)
    if request.method == 'POST':
        media_contact.delete()
        messages.success(request, 'Media contact deleted successfully!')
        return redirect('dashboard_manage_media_contact')
    return render(request, 'dashboard/confirm_delete.html', {'object': media_contact, 'type': 'Media Contact'})

@staff_member_required(login_url='/auth/login/')
def manage_media_home(request):
    
    return render(request, 'dashboard/manage_media_home.html')
