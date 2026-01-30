from django.http import JsonResponse
import json

def handler(request):
    """Simple test endpoint for Vercel deployment"""
    return JsonResponse({
        'status': 'success',
        'message': 'ECHOGA Foundation API is working!',
        'method': request.method,
        'path': request.path
    })