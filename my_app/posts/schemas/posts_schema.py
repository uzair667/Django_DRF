from rest_framework import serializers
from posts.models import Posts

class PostSchema(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'