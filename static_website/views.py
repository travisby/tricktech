# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse

import static_website.models
import static_website.forms

def index(request):
    return render_to_response(
        'index.html',
        {'active': 'index'}
    )


def contact(request):
    if request.method == 'GET':
        obj = {}
        obj.update(
            {
                'active': 'contact',
                'services': static_website.models.Service.objects.all(),
                'form': static_website.forms.CustomerServiceModelForm,
            }
        )
        return render_to_response(
            'contact.html',
            obj
        )
    elif request.method == 'POST':
        form = static_website.forms.CustomerServiceModelForm(request.POST)
        if form.is_valid():
            form.save()
            return admin(request)
        else:
            return HttpResponse('itdonebroke')

def admin(request):
    return render_to_response(
        'admin.html',
        {
            'customer_services': static_website.models.CustomerService.objects.all()
        }

    )

def faq(request):
    return render_to_response(
        'faq.html',
        {
            'faqs': static_website.models.Faq.objects.all()
        }
    )

def services(request):
    return render_to_response(
        'services.html',
        {
            'active': 'services',
            'services': static_website.models.Service.objects.all()
        }
    )
