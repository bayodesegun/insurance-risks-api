# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import User

def populate_db(apps, schema_editor):

    Risk = apps.get_model('risks', 'Risk')
    user1 = User.objects.create_user(username="geek", password="password") 
    user2 = User.objects.create_user(username="nerd", password="password")  
    risk = Risk(insurer_id=user1.id, name='Vehicle')
    risk2 = Risk(insurer_id=user2.id, name='House')
    risk.save()
    risk2.save()

    field1 = risk.field_set.create(type=1, name='Full Name')
    field2 = risk.field_set.create(type=1, name='Vehicle Number')
    field3 = risk.field_set.create(type=2, name='Vehicle Value (USD)')
    field4 = risk.field_set.create(type=4, name='Insurance Type')
    field5 = risk.field_set.create(type=3, name='Insured Date')
    
    choice1 = field4.choice_set.create(text='Comprehensive')
    choice2 = field4.choice_set.create(text='Basic Cover')
    choice3 = field4.choice_set.create(text='Third Party')

class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db),
    ]
