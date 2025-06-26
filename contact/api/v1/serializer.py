from rest_framework import serializers
from contact.models import Contact

class ContactSerilizer(serializers.ModelSerializer):
    relative_url = serializers.URLField(source='get_absolute_url',read_only=True)
    full_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Contact
        fields = ['name','family','gender','job','phone','relative_url','full_url']
        read_only_field =['relative_url','full_url']


    def get_full_url(self,obj):
        request = self.context.get('request')
        self.context['test']='test'
        if request:
            return request.build_absolute_uri(obj.get_absolute_url())
        return None