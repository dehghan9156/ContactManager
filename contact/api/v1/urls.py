from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'api-v1'

urlpatterns = [
    path("contact/get/",views.ContactGetApiView.as_view(),name="contact-get"),

]