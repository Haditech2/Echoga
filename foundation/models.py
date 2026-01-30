from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class NewsArticle(models.Model):
    """Model for news articles and impact stories"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True)
    featured_image = models.ImageField(upload_to='news/', blank=True, null=True)
    author = models.CharField(max_length=100, default='ECHOGA Foundation')
    published_date = models.DateTimeField(default=timezone.now)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'News Article'
        verbose_name_plural = 'News Articles'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.excerpt:
            self.excerpt = self.content[:297] + '...' if len(self.content) > 300 else self.content
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """Model for community testimonials"""
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, help_text='e.g., Community Member, Beneficiary, Volunteer')
    content = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"{self.name} - {self.role}"


class NewsletterSubscriber(models.Model):
    """Model for newsletter email subscriptions"""
    email = models.EmailField(unique=True)
    subscribed_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-subscribed_date']
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'

    def __str__(self):
        return self.email


class ContactMessage(models.Model):
    """Model for contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} - {self.subject}"


class VolunteerApplication(models.Model):
    """Model for volunteer registration applications"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    skills = models.TextField(help_text='Skills and areas of interest')
    message = models.TextField(blank=True)
    submitted_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Volunteer Application'
        verbose_name_plural = 'Volunteer Applications'

    def __str__(self):
        return f"{self.name} - {self.status}"


class GalleryImage(models.Model):
    """Model for gallery images"""
    CATEGORY_CHOICES = [
        ('events', 'Events'),
        ('programs', 'Programs'),
        ('community', 'Community'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField(blank=True)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-uploaded_date']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.title
class HelpRequest(models.Model):
    """Model for specific help/aid requests from the community"""
    HELP_TYPE_CHOICES = [
        ('education', 'Educational Support'),
        ('healthcare', 'Medical Assistance'),
        ('financial', 'Financial Aid'),
        ('emergency', 'Emergency Relief'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    help_type = models.CharField(max_length=20, choices=HELP_TYPE_CHOICES, default='other')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Help Request'
        verbose_name_plural = 'Help Requests'

    def __str__(self):
        return f"{self.name} - {self.get_help_type_display()} - {self.subject}"
