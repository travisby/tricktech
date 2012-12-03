from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return '%s -- $%sl' % (self.name, self.price)


class CustomerService(models.Model):
    user = models.ForeignKey(User)
    service = models.ForeignKey(Service)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return (
            "%s %s bought %s at %s" %
            (self.person_first_name,self.person_last_name, self.service, self.date)
        )

class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

class Chat(models.Model):
    user = models.ForeignKey(User)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
