from django.forms import ModelForm
from static_website.models import CustomerService, Chat

class CustomerServiceModelForm(ModelForm):
    class Meta:
        model = CustomerService
        exclude = ('user',)


class ChatModelForm(ModelForm):
    class Meta:
        model = Chat
        exclude = ('user',)
