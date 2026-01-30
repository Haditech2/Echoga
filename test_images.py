#!/usr/bin/env python
"""
Test script to verify Cloudinary images are accessible
"""
import requests
from foundation.templatetags.cloudinary_tags import cloudinary_url

def test_cloudinary_images():
    """Test if Cloudinary images are accessible"""
    
    # List of founder images to test
    images = [
        'founder-1.jpg',
        'founder-2.jpg', 
        'founder-3.jpg',
        'founder-4.jpg',
        'founder-5.jpg',
        'founder.jpg',
        'logo.jpg',
        'hero-bg.jpg'
    ]
    
    print("🔍 Testing Cloudinary image accessibility...\n")
    
    for image in images:
        try:
            # Generate Cloudinary URL
            url = f"https://res.cloudinary.com/dafag8jhg/image/upload/echoga_foundation/images/{image.split('.')[0]}.jpg"
            
            # Test if image is accessible
            response = requests.head(url, timeout=10)
            
            if response.status_code == 200:
                print(f"✅ {image} - Accessible")
                print(f"   URL: {url}")
            else:
                print(f"❌ {image} - Not accessible (Status: {response.status_code})")
                print(f"   URL: {url}")
                
        except Exception as e:
            print(f"❌ {image} - Error: {str(e)}")
        
        print()
    
    print("🌐 Your Cloudinary images are now hosted at:")
    print("https://res.cloudinary.com/dafag8jhg/image/upload/echoga_foundation/images/")

if __name__ == "__main__":
    test_cloudinary_images()