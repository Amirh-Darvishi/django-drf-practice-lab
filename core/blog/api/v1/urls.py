from django.urls import path, include
from blog.api.v1.views import *
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('post', PostViewSet)
router.register('category', CategoryViewSet)
urlpatterns = router.urls

#urlpatterns = [
    
    #apiview/genericview
    #path("post/", PostList.as_view(), name='post-list'),
    #path("post/<int:id>", PostDetail.as_view(), name='post-detail'),

    # viewset
    #path("post/", PostViewSet.as_view({'get': 'list', 'post':'create'}), name='post-list'),
    #path("post/<int:id>", PostViewSet.as_view({'get': 'retrieve',
    #         'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name='post-detail'),


#]