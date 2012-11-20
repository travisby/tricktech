# Create your views here.
from django.shortcuts import render_to_response
import static_website.models


def index(request):
    return render_to_response(
        'index.html',
        {'active': 'index'}
    )


def contact(request):
    return render_to_response(
        'contact.html',
        {'active': 'contact'}
    )


def services(request):
    return render_to_response(
        'services.html',
        {
            'active': 'services',
            'services': static_website.models.Service.objects.all()
        }
    )
