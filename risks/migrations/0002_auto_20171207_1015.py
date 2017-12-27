# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import User

def populate_db(apps, schema_editor):

    Risk = apps.get_model('risks', 'Risk')

    user1 = User.objects.create_user(username="geek", password="password") 
    user2 = User.objects.create_user(username="nerd", password="password")  

    risk1 = Risk(insurer_id=user1.id, name='Vehicle')
    risk1.save()
    risk1.field_set.create(type=1, name='Full Name')
    risk1.field_set.create(type=1, name='Vehicle Number')
    risk1.field_set.create(type=2, name='Vehicle Value (USD)')
    field1 = risk1.field_set.create(type=4, name='Insurance Type')    
    field1.choice_set.create(text='Comprehensive')
    field1.choice_set.create(text='Basic Cover')
    field1.choice_set.create(text='Third Party')
    risk1.field_set.create(type=3, name='Insured Date')

    risk2 = Risk(insurer_id=user2.id, name='Phone')
    risk2.save()
    risk2.field_set.create(type=1, name='Owner Name')
    risk2.field_set.create(type=1, name='Model Number')
    field2 = risk2.field_set.create(type=4, name='Phone Type')    
    field2.choice_set.create(text='Andriod')
    field2.choice_set.create(text='iOS')
    field2.choice_set.create(text='Windows')
    risk2.field_set.create(type=2, name='Phone Value (USD)')    
    risk2.field_set.create(type=3, name='Insured Date')

    risk3 = Risk(insurer_id=user1.id, name='Hair')
    risk3.save()
    risk3.field_set.create(type=1, name='Owner Name')
    field3 = risk3.field_set.create(type=4, name='Hair Type')    
    field3.choice_set.create(text='Blonde')
    field3.choice_set.create(text='Red')
    field3.choice_set.create(text='Auburn')
    field3.choice_set.create(text='Brown')
    field3.choice_set.create(text='Black')
    risk3.field_set.create(type=2, name='Hair Value (USD)')    
    risk3.field_set.create(type=3, name='Insured Date')

    risk4 = Risk(insurer_id=user2.id, name='House')
    risk4.save()
    risk4.field_set.create(type=1, name='Owner\'s Name')
    field4 = risk4.field_set.create(type=4, name='Inurance Type')    
    field4.choice_set.create(text='House Only')
    field4.choice_set.create(text='House with Furniture')
    risk4.field_set.create(type=2, name='Total Property Value (USD)')    
    risk4.field_set.create(type=3, name='Insured Date')

class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db),
    ]
