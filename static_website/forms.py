from django.forms import ModelForm
from static_website.models import CustomerService, Chat

class CustomerServiceModelForm(ModelForm):
    class Meta:
        model = CustomerService
        exclude = ('user',)
