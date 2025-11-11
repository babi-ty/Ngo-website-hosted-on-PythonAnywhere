from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Banner, VisionMission, Statistic, Initiative
from .forms import BannerForm, VisionMissionForm, StatisticForm, InitiativeForm

# ==================== PUBLIC PAGES ====================

def Home(request):
    """Homepage view"""
    banners = Banner.objects.filter(status=True).order_by('order')
    vision_mission = VisionMission.objects.first()
    statistics = Statistic.objects.filter(status=True).order_by('order')
    initiatives = Initiative.objects.filter(status=True).order_by('order')
    
    context = {
        'banners': banners,
        'vision_mission': vision_mission,
        'statistics': statistics,
        'initiatives': initiatives,
    }
    return render(request, 'index.html', context)

def rescue_page(request):
    return render(request, 'rescue.html')

def surgery_page(request):
    return render(request, 'surgery.html')

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

@login_required
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

@login_required
def manage_image_slider(request):
    """List all banners"""
    banners = Banner.objects.all().order_by('order')
    return render(request, 'dashboard/manage_slider.html', {'banners': banners})

@login_required
def manage_slider_add(request):
    """Add new banner"""
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Banner added successfully!')
            return redirect('dashboard_manage_slider')
    else:
        form = BannerForm()
    return render(request, 'dashboard/slider_form.html', {'form': form, 'action': 'Add'})

@login_required
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
        form = BannerForm(instance=banner)
    return render(request, 'dashboard/slider_form.html', {'form': form, 'action': 'Edit'})

@login_required
def manage_slider_delete(request, pk):
    """Delete banner"""
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        banner.delete()
        messages.success(request, 'Banner deleted successfully!')
        return redirect('dashboard_manage_slider')
    return render(request, 'dashboard/confirm_delete.html', {'object': banner, 'type': 'Banner'})


# ==================== STATISTIC MANAGEMENT ====================

@login_required
def manage_statistic(request):
    """List all statistics"""
    statistics = Statistic.objects.all().order_by('order')
    return render(request, 'dashboard/manage_statistic.html', {'statistics': statistics})

@login_required
def manage_statistic_add(request):
    """Add new statistic"""
    if request.method == 'POST':
        form = StatisticForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Statistic added successfully!')
            return redirect('dashboard_manage_statistic')
    else:
        form = StatisticForm()
    return render(request, 'dashboard/statistic_form.html', {'form': form, 'action': 'Add'})

@login_required
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
        form = StatisticForm(instance=statistic)
    return render(request, 'dashboard/statistic_form.html', {'form': form, 'action': 'Edit'})

@login_required
def manage_statistic_delete(request, pk):
    """Delete statistic"""
    statistic = get_object_or_404(Statistic, pk=pk)
    if request.method == 'POST':
        statistic.delete()
        messages.success(request, 'Statistic deleted successfully!')
        return redirect('dashboard_manage_statistic')
    return render(request, 'dashboard/confirm_delete.html', {'object': statistic, 'type': 'Statistic'})


# ==================== VISION & MISSION MANAGEMENT ====================

@login_required
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
        form = VisionMissionForm(instance=vision_mission)
    
    return render(request, 'dashboard/vision_form.html', {'form': form})


# ==================== INITIATIVE MANAGEMENT ====================

@login_required
def manage_initiative(request):
    """List all initiatives"""
    initiatives = Initiative.objects.all().order_by('order')
    return render(request, 'dashboard/manage_initiative.html', {'initiatives': initiatives})

@login_required
def manage_initiative_add(request):
    """Add new initiative"""
    if request.method == 'POST':
        form = InitiativeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Initiative added successfully!')
            return redirect('dashboard_manage_initiative')
    else:
        form = InitiativeForm()
    return render(request, 'dashboard/initiative_form.html', {'form': form, 'action': 'Add'})

@login_required
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
        form = InitiativeForm(instance=initiative)
    return render(request, 'dashboard/initiative_form.html', {'form': form, 'action': 'Edit'})

@login_required
def manage_initiative_delete(request, pk):
    """Delete initiative"""
    initiative = get_object_or_404(Initiative, pk=pk)
    if request.method == 'POST':
        initiative.delete()
        messages.success(request, 'Initiative deleted successfully!')
        return redirect('dashboard_manage_initiative')
    return render(request, 'dashboard/confirm_delete.html', {'object': initiative, 'type': 'Initiative'})