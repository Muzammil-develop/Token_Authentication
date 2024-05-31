from rest_framework import serializers
from home.models import Factory

class FactorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'