from __future__ import unicode_literals
import os
from datetime import datetime as dt
import string
import random 
from uuid import uuid4
from django.utils import timezone
from django.db import models, connection, transaction
from django.contrib.auth.models import Permission, Group, User
from django.utils.crypto import get_random_string
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField, GroupedForeignKey
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404
from django.utils.html import format_html
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.contrib.auth.hashers import make_password
from django.dispatch import receiver


def docNumTypeAccount():
    cod = 'TAC-' + get_random_string(10).upper()
    return cod

class TypeAccount(models.Model):
    STATUS_CHOICES = (
        ('A', 'Aktif'),
        ('T', 'Tidak Aktif'),
    )
    code = models.CharField(default=docNumTypeAccount, verbose_name="Document Number", max_length=150, editable=False, null=True)
    name =  models.CharField(max_length=55, )
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="Status", null=True)
    created_at = models.DateTimeField(verbose_name="Create Date", auto_now_add=True, blank=False, null=True)
    updated_at = models.DateTimeField(verbose_name="Last Update", auto_now=True, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name="Created by", null=True, blank=True, on_delete=models.PROTECT)

    
    def __str__(self):
        return self.name