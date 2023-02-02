from django.shortcuts import render
from rest_framework import response, views, viewsets

from .models import Tools
from .serializers import ToolSerializer

# Create your views here.


class ToolsViewSet(viewsets.ModelViewSet):
    serializer_class = ToolSerializer
    queryset = Tools.objects.all()

class TagView(views.APIView):

    def get(self, request, *args, **kwargs):
        tag = kwargs.get('tag', None)
        tools_with_tags = [ToolSerializer(tool).data for tool in Tools.objects.filter(tags__contains=tag)]
        return response.Response(tools_with_tags)
