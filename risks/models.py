# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

FIELD_TYPES = (
    (1, 'text'),
    (2, 'number'),
    (3, 'date'),
    (4, 'enum'),
)

@python_2_unicode_compatible
class Risk(models.Model):
    # Since there will be multiple insurers, there should be something to differentiate them
    insurer = models.ForeignKey('auth.User', related_name='risks', on_delete=models.CASCADE)

    # Name of the risk
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return "%s_%s" % (self.insurer, self.name)

    def get_data(self):
        fields = self.field_set.all()
        fields_array = []
        for field in fields:
            field_data = {
                "name": field.name,
                "type": field.type,
                "options": field.get_choices()
            }
            if field_data['options'] == None:
                field_data.pop('options', None) 
            fields_array.append(field_data)
        data = {
            "risk": self.name,
            "fields": fields_array
        }

        return data


@python_2_unicode_compatible
class Field(models.Model):
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    type = models.IntegerField(choices=FIELD_TYPES)
    name = models.CharField(max_length=200)
    def __str__(self):
        return "%s_%s" % (self.risk, self.name)
    def get_choices(self):
        if self.type == 4:
            return list(self.choice_set.values_list("text", flat=True))
        else:
            return None 

@python_2_unicode_compatible
class Choice(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    text = models.TextField()
    def __str__(self):
        return "%s_%s" % (self.field, self.text)

# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
