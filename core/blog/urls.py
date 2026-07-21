from django.urls import path, include
from blog.views import *
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
     # template
     path("index1/", indexView, name='FBV-index'),
     path("index2/", IndexView.as_view(), name='CBV-index'),

     # redirect
     path(
        "go-to-django/",
        RedirectView.as_view(url="https://www.djangoproject.com/"),
        name="redirect-to-django",
    ),
    path(
        "go-to-index/",
        RedirectView.as_view(pattern_name="blog:CBV-index"),
        name="redirect-to-index",
    ),
    path("go-to-maktab1/", maktab, name='redirect-to-maktab'),
    path("go-to-maktab2/", Maktab.as_view(), name='redirect-to-maktab'),

    # list
    path("post/",PostList.as_view(), name="post-list" ),

    # detail
    path("post/<int:pk>",PostDetail.as_view(), name='post-detail' ),

    # form
    path("post/create/", PostCreate.as_view(),name='post-create'),
    path("contact/form/", ContactCreate.as_view(),name='contact-form'),

    path("post/<int:pk>/edit/",PostUpdate.as_view(), name='post-edit' ),

    path("post/<int:pk>/delete/",PostDelete.as_view(), name='post-delete' ),

    # api
    path('api/v1/', include('blog.api.v1.urls'))
]