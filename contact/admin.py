from django.contrib import admin
from . models import *
from django.contrib.admin import ModelAdmin

class CustomeContact(ModelAdmin):
    search_fields = ['pk','name','family']
    list_display = ['pk','name','family','phone']


admin.site.register(Contact,CustomeContact)
