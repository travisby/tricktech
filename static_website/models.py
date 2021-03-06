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
    message = models.TextField(blank=True)

    def __unicode__(self):
        return (
            "%s %s bought %s at %s ---- %s" %
            (self.person_first_name,self.person_last_name, self.service, self.date, self.message)
        )


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __unicode__(self):
        return self.question
