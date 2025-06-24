from rest_framework import serializers
from contact.models import Contact

class ContactSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name','family','gender','job','phone']