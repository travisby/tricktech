# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

import static_website.models
import static_website.forms

def index(request):
    services = static_website.models.Service.objects.order_by('?')[:3]
    return render_to_response(
        'index.html',
        {
            'active': 'index',
            'services': services,
        }
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
            'active': 'faq',
            'faqs': static_website.models.Faq.objects.all(),
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

def chat(request):
    if request.method == 'GET':
        obj = {}
        obj.update(
            {
                'active': 'chat',
                'chat': static_website.models.Chat.objects.all(),
                'form': static_website.forms.ChatModelForm,
            }
        )
        return render_to_response(
            'chat.html',
            obj
        )
    elif request.method == 'POST':
        form = static_website.forms.ChatModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/chat/')
        else:
            return HttpResponse('itdonebroke')

def ajax_chat(request, last_message=0):
    return render_to_response(
        'chat_message.html',
        {
            'messages': static_website.models.Chat.objects.filter(pk__gt=last_message)
        }
    )
