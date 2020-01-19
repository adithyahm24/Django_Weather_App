from rest_framework import serializers
from .models import wapp


class wappserializer(serializers.ModelSerializer):
    class Meta:
        model= wapp
        fields=('id','name','language','price')