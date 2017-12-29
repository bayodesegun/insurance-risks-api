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
    fullName = risk1.fields.create(type=1, name='Full Name')
    risk1.fields.create(type=1, name='Vehicle Number')
    insValue = risk1.fields.create(type=2, name='Insured Value (USD)')
    insType = risk1.fields.create(type=4, name='Insurance Type')    
    comprehensive = insType.choices.create(text='Comprehensive')
    basicCover = insType.choices.create(text='Basic Cover')
    insType.choices.create(text='Third Party')
    insDate = risk1.fields.create(type=3, name='Insured Date')

    # re-use some of the existing fields or choices
    risk2 = Risk(insurer_id=user2.id, name='Phone')
    risk2.save()
    risk2.fields.add(fullName)
    risk2.fields.create(type=1, name='Model Number')
    phoneType = risk2.fields.create(type=4, name='Phone Type')    
    phoneType.choices.create(text='Andriod')
    phoneType.choices.create(text='iOS')
    phoneType.choices.create(text='Windows')
    risk2.fields.add(insValue)    
    risk2.fields.add(insDate)

    risk3 = Risk(insurer_id=user1.id, name='Hair')
    risk3.save()
    risk3.fields.add(fullName)
    hairType = risk3.fields.create(type=4, name='Hair Type')    
    hairType.choices.create(text='Blonde')
    hairType.choices.create(text='Red')
    hairType.choices.create(text='Auburn')
    hairType.choices.create(text='Brown')
    hairType.choices.create(text='Black')
    risk3.fields.add(insValue)    
    risk3.fields.add(insDate)

    risk4 = Risk(insurer_id=user2.id, name='House')
    risk4.save()
    risk4.fields.add(fullName)
    coverType = risk4.fields.create(type=4, name='Cover Type')    
    coverType.choices.add(basicCover)
    coverType.choices.add(comprehensive)
    risk4.fields.add(insValue)    
    risk4.fields.add(insDate)

class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db),
    ]
