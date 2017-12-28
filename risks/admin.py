# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Risk, Field, Choice

# Register your models here.
admin.site.register([Risk, Field, Choice])
