from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import response, views, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Tools
from .serializers import ToolSerializer, USerSerializer

# Create your views here.


class ToolsViewSet(viewsets.ModelViewSet):
    serializer_class = ToolSerializer
    queryset = Tools.objects.all()
    permission_classes = [IsAuthenticated]

class TagView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        tag = kwargs.get('tag', None)
        tools_with_tags = [ToolSerializer(tool).data for tool in Tools.objects.filter(tags__contains=tag)]
        return response.Response(tools_with_tags)

class UserView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return response.Response(status='201')