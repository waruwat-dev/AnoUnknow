from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from announcement.models import AnnouncementModel, typeOfAnnouncement


class AnnouncementSerializer(ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    
    class Meta:
        model = AnnouncementModel
        fields = ['text', 'type']

    def get_type(self,obj):
        return obj.get_type_display()