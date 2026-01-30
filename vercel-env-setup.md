# Vercel Environment Variables Setup

To deploy your ECHOGA Foundation website on Vercel, you need to set up the following environment variables in your Vercel dashboard:

## Required Environment Variables

Go to your Vercel project dashboard and add these environment variables:

### 1. Cloudinary Configuration
```
CLOUDINARY_CLOUD_NAME = dafag8jhg
CLOUDINARY_API_KEY = 256576913286665
CLOUDINARY_API_SECRET = ZFZAXBI3oXwo-y64FA9dY0p2RPo
```

### 2. Django Configuration
```
SECRET_KEY = django-insecure-w(%11(d0^&5g2hzx2bx_551j)7ktsmiirxe=)8wk%1sqlyv1%c
DEBUG = False
```

### 3. Email Configuration
```
FOUNDER_EMAIL = ismailamuhammadattah@gmail.com
```

## How to Add Environment Variables in Vercel:

1. Go to https://vercel.com/dashboard
2. Select your ECHOGA project
3. Go to Settings → Environment Variables
4. Add each variable with its corresponding value
5. Make sure to set them for all environments (Production, Preview, Development)

## Deployment Steps:

1. Push your code to GitHub (already done ✅)
2. Connect your GitHub repository to Vercel
3. Add the environment variables above
4. Deploy!

Your images are now served from Cloudinary CDN for optimal performance:
- Automatic image optimization
- Responsive image delivery
- Fast global CDN
- Reduced server load

## Test URLs:
- Founder Image 1: https://res.cloudinary.com/dafag8jhg/image/upload/echoga_foundation/images/founder-1.jpg
- Logo: https://res.cloudinary.com/dafag8jhg/image/upload/echoga_foundation/images/logo.jpg