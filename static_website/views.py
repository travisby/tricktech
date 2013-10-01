# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

import static_website.models
import static_website.forms

def index(request):
    services = static_website.models.Service.objects.order_by('?')[:3]
    return render_to_response(
        'index.html',
        {
            'active': 'index',
            'services': services,
            'login_form': AuthenticationForm,
        },
         context_instance=RequestContext(request)
    )


def contact(request):
    if request.method == 'GET':
        obj = {}
        obj.update(
            {
                'active': 'contact',
                'services': static_website.models.Service.objects.all(),
                'form': static_website.forms.CustomerServiceModelForm,
                'login_form': AuthenticationForm,
            }
        )
        return render_to_response(
            'contact.html',
            obj,
            context_instance=RequestContext(request)
        )
    elif request.method == 'POST':
        form = static_website.forms.CustomerServiceModelForm(request.POST)
        if form.is_valid():
            customer_service = form.save(commit=False)
            customer_service.user = request.user
            customer_service.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('itdonebroke')

def admin(request):
    return render_to_response(
        'admin.html',
        {
            'active': 'admin',
            'customer_services': static_website.models.CustomerService.objects.all(),
            'login_form': AuthenticationForm,
        },
         context_instance=RequestContext(request)

    )

def faq(request):
    return render_to_response(
        'faq.html',
        {
            'active': 'faq',
            'faqs': static_website.models.Faq.objects.all(),
            'login_form': AuthenticationForm,
        },
         context_instance=RequestContext(request)
    )

def services(request):
    return render_to_response(
        'services.html',
        {
            'active': 'services',
            'services': static_website.models.Service.objects.all(),
            'login_form': AuthenticationForm,
        },
         context_instance=RequestContext(request)
    )

def register(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('itdonebroke')
    else:
        form = UserCreationForm()
        return render_to_response(
            'register.html',
            {
                'form': form
            },
            context_instance=RequestContext(request)
        )
