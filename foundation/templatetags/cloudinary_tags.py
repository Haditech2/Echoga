from django import template
from django.conf import settings
import cloudinary
from cloudinary import CloudinaryImage

register = template.Library()

@register.simple_tag
def cloudinary_url(image_name, folder="echoga_foundation/images", **kwargs):
    """
    Generate Cloudinary URL for an image
    Usage: {% cloudinary_url 'founder-1.jpg' width=300 height=300 crop='fill' %}
    """
    try:
        # Remove file extension from image_name for public_id
        public_id = f"{folder}/{image_name.split('.')[0]}"
        
        # Create CloudinaryImage instance
        image = CloudinaryImage(public_id)
        
        # Apply transformations if provided
        if kwargs:
            return image.build_url(**kwargs)
        else:
            return image.build_url()
            
    except Exception as e:
        # Fallback to static URL if Cloudinary fails
        return f"/static/images/{image_name}"

@register.simple_tag
def founder_image(image_name, **kwargs):
    """
    Shortcut for founder images
    Usage: {% founder_image 'founder-1.jpg' width=200 height=200 crop='fill' %}
    """
    return cloudinary_url(image_name, **kwargs)

@register.simple_tag
def responsive_image(image_name, **kwargs):
    """
    Generate responsive image with default optimizations
    Usage: {% responsive_image 'founder-1.jpg' width=300 height=300 %}
    """
    default_params = {
        'quality': 'auto',
        'fetch_format': 'auto',
        'crop': 'fill',
        'gravity': 'face'  # Focus on faces for founder images
    }
    
    # Merge default params with provided kwargs
    params = {**default_params, **kwargs}
    
    return cloudinary_url(image_name, **params)