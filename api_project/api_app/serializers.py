from rest_framework import serializers
from .models import Saklaso
import datetime

class SaklasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saklaso
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.title = instance.title.upper()
        instance.create_date = datetime.datetime.now()
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.write_date = datetime.datetime.now()
        instance.edited = True
        instance.save()
        return instance

    