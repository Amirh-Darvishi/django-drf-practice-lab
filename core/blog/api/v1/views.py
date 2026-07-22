from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from blog.api.v1.serializers import PostSerializer,CategorySerializer
from blog.models import Post, Category
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView )
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
# FBV 
"""
@api_view(["POST", "GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    try:
        if request.method == "GET":
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        elif request.method == "POST":
            serializer = PostSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({"detail":"post doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
"""   


# CBV
"""
class PostList(APIView):
    # getting a list of posts and creating new posts
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
            # retrieving a list of posts
            try:
                posts = Post.objects.filter(status=True)
                serializer = self.serializer_class(posts, many=True)
                return Response(serializer.data)
            except Post.DoesNotExist:
                return Response({"detail":"post doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
            # creating a post with provided data 
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
"""
"""
class PostList(GenericAPIView):
    queryset= Post.objects.filter(status=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
            # retrieving a list of posts
            try:
                queryset = self.get_queryset()
                serializer = self.serializer_class(queryset, many=True)
                return Response(serializer.data)
            except Post.DoesNotExist:
                return Response({"detail":"post doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
            # creating a post with provided data 
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
"""
"""
class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    queryset= Post.objects.filter(status=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    # Concrete view for listing a queryset.
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    # Concrete view for creating a model instance.
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
"""
class PostList(ListCreateAPIView):
     
    queryset= Post.objects.filter(status=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer







# FBV
"""
@api_view(["PUT", "GET", "DELETE"])
@permission_classes([IsAuthenticated])
def post_detail(request,id):
    try:
        post = Post.objects.get(pk=id)
        if request.method == "GET":
            serializer = PostSerializer(post)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = PostSerializer(post, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == "DELETE":
            post.delete()
            return Response({"detail":"item removed successfully"})
    except Post.DoesNotExist:
        return Response({"detail":"post doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
"""


# CBV

"""
class PostDetail(APIView):
    # getting detail of the post and edit plus removing it
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self, request, id):
        # retrieving the post data
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
       
    def put(self, request, id):
        # editing the post data
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        # deleting the post object
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail":"item removed successfully"})
"""


class PostDetail(RetrieveUpdateDestroyAPIView):

    queryset= Post.objects.filter(status=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    lookup_field= 'id'




"""
class PostViewSet(viewsets.ViewSet):

    queryset= Post.objects.filter(status=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    # A simple ViewSet for listing or retrieving users.

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def create(self, request):
        pass

    def update(self, request, pk):
        pass

    def partial_update(self, request, pk):
        pass

    def destroy(self, request, pk):
        pass
"""
class PostViewSet(ModelViewSet):
    queryset= Post.objects.filter(status=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    @action(methods=['get'], detail=False)
    def get_ok(self, request):
        return Response({'detail':'ok'})



class CategoryViewSet(ModelViewSet):
    queryset= Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer