from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.core.validators import URLValidator

class Banner(models.Model):
    """Homepage banner/slider images"""
    image = models.ImageField(
        upload_to='banners/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
        help_text="Recommended size: 1920x600px"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Lower numbers appear first")
    status = models.BooleanField(default=True, help_text="Active/Inactive")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    def __str__(self):
        return self.title


class VisionMission(models.Model):
    """Organization vision and mission statement"""
    vision_title = models.CharField(max_length=200, default="Our Vision")
    vision_description = models.TextField()
    mission_title = models.CharField(max_length=200, default="Our Mission")
    mission_description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vision & Mission"
        verbose_name_plural = "Vision & Mission"

    def __str__(self):
        return "Vision & Mission Statement"


class Statistic(models.Model):
    """Homepage statistics display"""
    label = models.CharField(max_length=100, help_text="e.g., Rescues Monthly")
    value = models.CharField(max_length=50, help_text="e.g., 500+")
    order = models.IntegerField(default=0, help_text="Lower numbers appear first")
    status = models.BooleanField(default=True, help_text="Active/Inactive")
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
    
class Project(models.Model):
    """Organization projects"""
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(default=0, help_text="Lower numbers appear first")
    is_active = models.BooleanField(default=True, help_text="Active/Inactive")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    """Images for projects"""
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(
        upload_to='projects/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
        help_text="Recommended size: 600x400px"
    )
    is_primary = models.BooleanField(default=False, help_text="Primary display image")
    uploaded_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ['-is_primary', '-uploaded_at']
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"Image for {self.project.title}"
    
class PressRelease(models.Model):
    """Press releases and announcements"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    file = models.FileField(upload_to='press_releases/', blank=True, null=True, 
                           help_text='Optional PDF or document file')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text='Lower numbers appear first')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-release_date', 'order']
        verbose_name = 'Press Release'
        verbose_name_plural = 'Press Releases'

    def __str__(self):
        return self.title


class MediaCoverage(models.Model):
    """External media coverage and articles"""
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=2083, validators=[URLValidator()])
    source = models.CharField(max_length=255, help_text='e.g., The Hindu, Times of India')
    published_date = models.DateField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='media_coverage/', blank=True, null=True,
                                 help_text='Optional thumbnail image')
    description = models.TextField(blank=True, help_text='Brief summary of the coverage')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text='Lower numbers appear first')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date', 'order']
        verbose_name = 'Media Coverage'
        verbose_name_plural = 'Media Coverage'

    def __str__(self):
        return f"{self.title} - {self.source}"


class ImageGallery(models.Model):
    """Image gallery for events and activities"""
    CATEGORY_CHOICES = [
        ('event', 'Event'),
        ('rescue', 'Rescue Operation'),
        ('surgery', 'ABC Surgery'),
        ('awareness', 'Awareness Campaign'),
        ('other', 'Other'),
    ]
    
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    date_taken = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text='Lower numbers appear first')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_taken', 'order']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.title


class Video(models.Model):
    """Videos from YouTube or other platforms"""
    title = models.CharField(max_length=255)
    video_url = models.URLField(max_length=2083, validators=[URLValidator()],
                               help_text='YouTube, Vimeo, or other video URL')
    embed_code = models.TextField(blank=True, 
                                  help_text='Optional: Custom embed code (overrides URL)')
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, help_text='e.g., 5:30')
    uploaded_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text='Lower numbers appear first')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_date', 'order']
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.title
    
    def get_youtube_id(self):
        """Extract YouTube video ID from URL"""
        if 'youtube.com/watch?v=' in self.video_url:
            return self.video_url.split('watch?v=')[1].split('&')[0]
        elif 'youtu.be/' in self.video_url:
            return self.video_url.split('youtu.be/')[1].split('?')[0]
        return None
    
    def get_embed_url(self):
        """Get YouTube embed URL"""
        video_id = self.get_youtube_id()
        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return None


class MediaContact(models.Model):
    """Contact information for media inquiries"""
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='media_contacts/', blank=True, null=True)
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Media Contact'
        verbose_name_plural = 'Media Contacts'

    def __str__(self):
        return f"{self.name} - {self.designation}"