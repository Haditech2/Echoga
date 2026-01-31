from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from .models import NewsArticle, Testimonial, GalleryImage
from .forms import ContactForm, NewsletterForm, VolunteerForm, HelpRequestForm


def help_request(request):
    """Help request page view"""
    help_form = HelpRequestForm()
    
    if request.method == 'POST':
        help_form = HelpRequestForm(request.POST)
        if help_form.is_valid():
            # Save request to database
            help_obj = help_form.save()
            
            # Send email notification to founder
            try:
                subject = f"NEW HELP REQUEST: {help_obj.get_help_type_display()} - {help_obj.subject}"
                email_message = f"You have received a new HELP REQUEST from the ECHOGA Foundation website:\n\n" \
                                f"Type: {help_obj.get_help_type_display()}\n" \
                                f"Name: {help_obj.name}\n" \
                                f"Email: {help_obj.email}\n" \
                                f"Phone: {help_obj.phone}\n" \
                                f"Subject: {help_obj.subject}\n\n" \
                                f"Message:\n{help_obj.message}\n\n" \
                                f"--- End of Request ---"
                
                send_mail(
                    subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@echogafoundation.org',
                    [settings.FOUNDER_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Error sending help email: {e}")
            
            messages.success(request, 'Your request for assistance has been submitted to Hon. Attah personally. We will review and get back to you.')
            return redirect('help_request')
    
    context = {
        'help_form': help_form,
    }
    return render(request, 'pages/help_request.html', context)


def home(request):
    """Home page view"""
    # Get featured news and testimonials, handle if models don't exist yet
    try:
        featured_news = NewsArticle.objects.filter(is_featured=True)[:3]
    except Exception:
        featured_news = []
    
    try:
        testimonials = Testimonial.objects.filter(is_active=True)[:6]
    except Exception:
        testimonials = []
    
    # Handle newsletter subscription
    newsletter_form = NewsletterForm()
    
    context = {
        'featured_news': featured_news,
        'testimonials': testimonials,
        'newsletter_form': newsletter_form,
    }
    return render(request, 'pages/home.html', context)


def about_founder(request):
    """About Founder page view"""
    return render(request, 'pages/about_founder.html')


def about_foundation(request):
    """About Foundation page view"""
    return render(request, 'pages/about_foundation.html')


def programs(request):
    """Programs page view"""
    return render(request, 'pages/programs.html')


def gallery(request):
    """Gallery page view"""
    # Get all active gallery images
    category = request.GET.get('category', 'all')
    
    try:
        if category and category != 'all':
            images = GalleryImage.objects.filter(is_active=True, category=category)
        else:
            images = GalleryImage.objects.filter(is_active=True)
    except Exception:
        images = []
    
    # Pagination
    paginator = Paginator(images, 12)  # Show 12 images per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'current_category': category,
    }
    return render(request, 'pages/gallery.html', context)


def news(request):
    """News and Impact page view"""
    # Get all news articles
    try:
        news_list = NewsArticle.objects.all()
    except Exception:
        news_list = []
    
    # Pagination
    paginator = Paginator(news_list, 6)  # Show 6 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get featured article
    try:
        featured_article = NewsArticle.objects.filter(is_featured=True).first()
    except Exception:
        featured_article = None
    
    context = {
        'page_obj': page_obj,
        'featured_article': featured_article,
    }
    return render(request, 'pages/news.html', context)


def news_detail(request, slug):
    """News article detail view"""
    article = get_object_or_404(NewsArticle, slug=slug)
    recent_news = NewsArticle.objects.exclude(id=article.id)[:3]
    
    context = {
        'article': article,
        'recent_news': recent_news,
    }
    return render(request, 'pages/news_detail.html', context)


def get_involved(request):
    """Get Involved page view (Donate/Volunteer)"""
    volunteer_form = VolunteerForm()
    
    if request.method == 'POST':
        if 'volunteer_submit' in request.POST:
            volunteer_form = VolunteerForm(request.POST)
            if volunteer_form.is_valid():
                # Save application to database
                volunteer_obj = volunteer_form.save()
                
                # Send email notification to founder
                try:
                    subject = f"New Volunteer Application: {volunteer_obj.name}"
                    email_message = f"You have received a new volunteer application from the ECHOGA Foundation website:\n\n" \
                                    f"Name: {volunteer_obj.name}\n" \
                                    f"Email: {volunteer_obj.email}\n" \
                                    f"Phone: {volunteer_obj.phone}\n" \
                                    f"Skills: {volunteer_obj.skills}\n\n" \
                                    f"Message:\n{volunteer_obj.message}\n\n" \
                                    f"--- End of Application ---"
                    
                    send_mail(
                        subject,
                        email_message,
                        settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@echogafoundation.org',
                        [settings.FOUNDER_EMAIL],
                        fail_silently=False,
                    )
                except Exception as e:
                    print(f"Error sending volunteer email: {e}")
                
                messages.success(request, 'Thank you for your interest! Your application has been sent to Hon. Attah.')
                return redirect('get_involved')
    
    context = {
        'volunteer_form': volunteer_form,
    }
    return render(request, 'pages/get_involved.html', context)


def contact(request):
    """Contact page view"""
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Save message to database
            message_obj = contact_form.save()
            
            # Send email notification to founder
            try:
                subject = f"New Contact Message: {message_obj.subject}"
                email_message = f"You have received a new message from the ECHOGA Foundation website:\n\n" \
                                f"Name: {message_obj.name}\n" \
                                f"Email: {message_obj.email}\n" \
                                f"Subject: {message_obj.subject}\n\n" \
                                f"Message:\n{message_obj.message}\n\n" \
                                f"--- End of Message ---"
                
                send_mail(
                    subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@echogafoundation.org',
                    [settings.FOUNDER_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                # Log error or handle silently in dev
                print(f"Error sending email: {e}")
            
            messages.success(request, 'Thank you for your message! It has been sent to Hon. Attah.')
            return redirect('contact')
    
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'pages/contact.html', context)


def newsletter_subscribe(request):
    """AJAX endpoint for newsletter subscription"""
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Successfully subscribed to newsletter!'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid email or already subscribed.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def image_test(request):
    """Test page to verify founder images are loading"""
    return render(request, 'pages/image_test.html')

