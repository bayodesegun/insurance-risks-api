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
class Choice(models.Model):
    text = models.CharField(max_length=200, unique=True) # since we can assign them to multiple fields, no need for duplicates
    
    def __str__(self):
        return self.text

@python_2_unicode_compatible
class Field(models.Model):
    # this model requires the most flexibility as we can have the the same type and name but different choices
    # unique or unique_together not applicable?    
    type = models.IntegerField(choices=FIELD_TYPES)
    name = models.CharField(max_length=50)

    # Choices
    choices = models.ManyToManyField(Choice, blank=True) # optional
        

    def __str__(self):
        return self.name
    def get_choices(self):
        if self.type == 4:
            return list(self.choices.values_list("text", flat=True))
        else:
            return None

@python_2_unicode_compatible
class Risk(models.Model):
    # Since there will be multiple insurers, there should be something to differentiate them
    insurer = models.ForeignKey('auth.User', related_name='risks', on_delete=models.CASCADE)
    
    # Name of the risk
    name = models.CharField(max_length=50)
    
    # Fields
    fields = models.ManyToManyField(Field) # this, unlike `options`, is required

    class Meta:
        # no point for an insurer to create risks of the same name
        unique_together = ('insurer', 'name')

    def __str__(self):
        return "%s_%s" % (self.insurer, self.name)

    def get_data(self):
        fields = self.fields.all()
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

# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
