from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-founder/', views.about_founder, name='about_founder'),
    path('about-foundation/', views.about_foundation, name='about_foundation'),
    path('programs/', views.programs, name='programs'),
    path('gallery/', views.gallery, name='gallery'),
    path('news/', views.news, name='news'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('get-involved/', views.get_involved, name='get_involved'),
    path('contact/', views.contact, name='contact'),
    path('need-help/', views.help_request, name='help_request'),
    path('api/newsletter-subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('test-images/', views.image_test, name='image_test'),
]
