from django.urls import path, include
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("api/v1/", include("accounts.api.v1.urls")),
    path("api/v2/", include("djoser.urls")),
    path("api/v2/", include("djoser.urls.jwt")),
    path("test/", views.test, name="test"),
    path("send-email/", views.send_email, name="send-email"),
]
