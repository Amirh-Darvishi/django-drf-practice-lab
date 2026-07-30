from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
from accounts.models import User
import pytest


@pytest.fixture
def api_client():
    clint = APIClient()
    return clint


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="amirhhdr13832@gmail.com", password="12345@qwe", is_verified=True
    )


@pytest.mark.django_db
class TestPostApi:
    # client = APIClient()

    def test_get_post_response_200_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        # response = self.client.get(url)
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "category": None,
            "published_date": datetime.now(),
        }
        # response = self.client.post(url, data)
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "category": None,
            "published_date": datetime.now(),
        }
        user = common_user
        api_client.force_login(user=user)
        # response = self.client.post(url, data)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(
        self, api_client, common_user
    ):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "category": None,
            "published_date": datetime.now(),
        }
        user = common_user
        api_client.force_login(user=user)
        # response = self.client.post(url, data)
        response = api_client.post(url, data)
        assert response.status_code == 400
