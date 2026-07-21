from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from blog.api.v1.serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


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
