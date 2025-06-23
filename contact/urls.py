from django.contrib import admin
from django.urls import path,include

app_name = 'contact'

urlpatterns = [
  path("api/v1/",include("contact.api.v1.urls",namespace="api-v1")),
]