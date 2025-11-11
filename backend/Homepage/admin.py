from django.contrib import admin
from django.utils.html import mark_safe
from .models import Banner, VisionMission, Statistic, Initiative


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'status', 'image_preview', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'status']
    ordering = ['order']
    readonly_fields = ['created_at', 'updated_at', 'image_preview']
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'description', 'image', 'image_preview')
        }),
        ('Settings', {
            'fields': ('order', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 100px; height: auto; border-radius: 5px;" />')
        return '-'
    image_preview.short_description = 'Preview'


@admin.register(VisionMission)
class VisionMissionAdmin(admin.ModelAdmin):
    list_display = ['vision_title', 'mission_title', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Vision', {
            'fields': ('vision_title', 'vision_description')
        }),
        ('Mission', {
            'fields': ('mission_title', 'mission_description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one instance
        return not VisionMission.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Prevent deletion if you want to always have one instance
        return False


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ['label', 'value', 'order', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['label', 'value']
    list_editable = ['order', 'status']
    ordering = ['order']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Content', {
            'fields': ('label', 'value')
        }),
        ('Settings', {
            'fields': ('order', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'status', 'image_preview', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'status']
    ordering = ['order']
    readonly_fields = ['created_at', 'updated_at', 'image_preview']
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'description', 'image', 'image_preview')
        }),
        ('Settings', {
            'fields': ('order', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 100px; height: auto; border-radius: 5px;" />')
        return '-'
    image_preview.short_description = 'Preview'