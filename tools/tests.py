from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import (APIClient, APIRequestFactory, APITestCase,
                                 force_authenticate)

from .models import Tools
from .views import TagView, ToolsViewSet, UserView


class ToolsTests(APITestCase):
    def setUp(self) -> None:
        Tools.objects.create(
            title = "json-server",
            link = "https://github.com/typicode/json-server",
            description = "Fake REST API based on a json schema.",
            tags = ["api","json","schema","node","github","rest"]
        )
        User.objects.create_user(username='andre2', email='andre@example.com', password='andre1234')

    def test_get_tools_list(self):
        user = User.objects.get(username='andre2')
        request = APIRequestFactory().get("")
        tools_list = ToolsViewSet.as_view({'get': 'list'})
        force_authenticate(request, user=user)
        response = tools_list(request)
        self.assertEqual(response.status_code, 200)
        
    def test_post_tool(self):
        user = User.objects.get(username='andre2')
        data = {   
        "title": "json-server2",   
        "link": "https://github.com/typicode/json-server", 
        "description": "Fake REST API based on a json schema. challenges.", 
        "tags": ["api","json", "schema","node","github","rest"]
        }
        view = ToolsViewSet.as_view({'post': 'create'})
        request = APIRequestFactory().post(path=view,data=data)
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 201)       

    def test_tag_search(self):
        user = User.objects.get(username='andre2')
        request = APIRequestFactory().get("")
        view = TagView.as_view()
        force_authenticate(request, user=user)
        response = view(request, tag='node')
        self.assertEqual(response.status_code, 200)
    
    def test_auth(self):
        request = APIRequestFactory().get("")
        tools_list = ToolsViewSet.as_view({'get': 'list'})
        response = tools_list(request)
        self.assertEqual(response.status_code, 401)