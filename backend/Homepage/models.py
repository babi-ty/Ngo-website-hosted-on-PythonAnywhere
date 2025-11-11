from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone


class Banner(models.Model):

    image = models.ImageField(
        upload_to='banners/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
        help_text="Recommended size: 1920x600px"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Lower numbers appear first")
    status = models.BooleanField(default=True, help_text="Active/Inactive")
    # This one is correct
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    def __str__(self):
        return self.title


class VisionMission(models.Model):

    vision_title = models.CharField(max_length=200, default="Our Vision")
    vision_description = models.TextField()
    mission_title = models.CharField(max_length=200, default="Our Mission")
    mission_description = models.TextField()
    # 👇 CHANGED THIS LINE
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vision & Mission"
        verbose_name_plural = "Vision & Mission"

    def __str__(self):
        return "Vision & Mission Statement"


class Statistic(models.Model):

    label = models.CharField(max_length=100, help_text="e.g., Rescues Monthly")
    value = models.CharField(max_length=50, help_text="e.g., 500+")
    order = models.IntegerField(default=0, help_text="Lower numbers appear first")
    status = models.BooleanField(default=True, help_text="Active/Inactive")
    # 👇 CHANGED THIS LINE
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Statistic"
        verbose_name_plural = "Statistics"

    def __str__(self):
        return f"{self.value} - {self.label}"


class Initiative(models.Model):
    """Organization initiatives/programs"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(
        upload_to='initiatives/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
        help_text="Recommended size: 600x400px"
    )
    order = models.IntegerField(default=0, help_text="Lower numbers appear first")
    status = models.BooleanField(default=True, help_text="Active/Inactive")

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Initiative"
        verbose_name_plural = "Initiatives"

    def __str__(self):
        return self.title