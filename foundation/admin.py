from django.contrib import admin
from .models import NewsArticle, Testimonial, NewsletterSubscriber, ContactMessage, VolunteerApplication, GalleryImage, HelpRequest


@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'help_type', 'subject', 'submitted_date', 'is_read')
    list_filter = ('help_type', 'is_read', 'submitted_date')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('submitted_date',)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'is_featured']
    list_filter = ['is_featured', 'published_date']
    search_fields = ['title', 'content', 'author']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ['-published_date']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'is_active', 'created_date']
    list_filter = ['is_active', 'created_date']
    search_fields = ['name', 'role', 'content']
    ordering = ['-created_date']


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_date', 'is_active']
    list_filter = ['is_active', 'subscribed_date']
    search_fields = ['email']
    ordering = ['-subscribed_date']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'submitted_date', 'is_read']
    list_filter = ['is_read', 'submitted_date']
    search_fields = ['name', 'email', 'subject', 'message']
    ordering = ['-submitted_date']
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'status', 'submitted_date']
    list_filter = ['status', 'submitted_date']
    search_fields = ['name', 'email', 'phone', 'skills']
    ordering = ['-submitted_date']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'uploaded_date', 'is_active']
    list_filter = ['category', 'is_active', 'uploaded_date']
    search_fields = ['title', 'description']
    ordering = ['-uploaded_date']
