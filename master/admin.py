from __future__ import unicode_literals
import os
from datetime import datetime as dt
import string
import random 
from django.contrib import admin
from uuid import uuid4
from django.utils import timezone
from django.db import models, connection, transaction
from django.contrib.auth.models import Permission, Group, User
from django.utils.crypto import get_random_string
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField, GroupedForeignKey
from django.forms import TextInput, Textarea
from master.models import *
from reversion.admin import VersionAdmin

class TypeAccountAdmin (VersionAdmin):
    # list_display = ['name', 'types', 'parent', 'currency']
    list_display = ['code','name', 'status','created_at','updated_at','user']
    search_fields = ['name',]

    readonly_fields=('created_at', 'updated_at','user')
    list_per_page = 25

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':55})}
    }

    def save_model(self, request, obj, form, change, commit=True):
        super(TypeAccountAdmin, self).save_model(request, obj, form, change)
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
            if commit:
                obj.save()

admin.site.register(TypeAccount, TypeAccountAdmin)