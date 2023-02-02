from rest_framework import serializers

from .models import Tools


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = ['id', 'title', 'link', 'description', 'tags']