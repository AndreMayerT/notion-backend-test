from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Tools


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = ['id', 'title', 'link', 'description', 'tags']

class USerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']