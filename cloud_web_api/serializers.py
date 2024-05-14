from rest_framework import serializers
from .models import Kisi

class KisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kisi
        fields = ['id','KisiMail','KisiPassword']