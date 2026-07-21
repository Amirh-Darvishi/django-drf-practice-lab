from rest_framework import serializers
from blog.models import Post


# class PostSerializer(serializers.Serializer):
#      id = serializers.IntegerField()
#      title = serializers.CharField()
#      author = serializers.EmailField()
#      content = serializers.CharField()
#      status = serializers.BooleanField()
#      category = serializers.CharField()



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ['id', 'title', 'author', 'content',
                'status', 'category', 'published_date']
