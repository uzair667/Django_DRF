from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from posts.schemas.posts_schema import PostSchema
from .models import Posts
from crud.models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from my_app.exceptions import UnprocessableEntity

# Create your views here.

def fetch_post_data(request):

    data = 'https://jsonplaceholder.typicode.com/posts'
    json_data = requests.get(data)
    result = json.loads(json_data.content)

    for items in result:
        post_user_id = items.get("userId")
        api_title = items.get("title")
        api_body = items.get("body")
        
        validate = PostSchema(data=data)

        post = Posts()
            
        user_instance, created = Users.objects.get_or_create(id=post_user_id)
        post = Posts.objects.create(user_id=user_instance, title=api_title, body=api_body)
        
        if validate.is_valid():
            post.save()

    return JsonResponse(result, safe=False)



class ListPosts(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Posts.objects.all()
    
    def get(self, request):
        queryset = self.get_queryset()
        schema = PostSchema(queryset, many=True)
        return Response(schema.data)
    
    def post(self, request):
        new_data = request.data
        
        check_user = Users.objects.filter(id = new_data.get("user_id")).first()
        if not check_user:
            raise UnprocessableEntity("User_id not found")
        schema = PostSchema(data=new_data)
        if schema.is_valid():
            schema.save()
            return Response(schema.data, status=status.HTTP_200_OK)
        else:
            return Response(schema.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    def put(self, request, pk):
        new_data = request.data

        try:
            instance = Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        schema = PostSchema(instance, data=new_data)

        if schema.is_valid():
            schema.save()
            return Response(schema.data, status=status.HTTP_201_CREATED)
        else:
            return Response(schema.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        

    def delete(self, request, pk):
        try:
            instance = Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response("", status=status.HTTP_204_NO_CONTENT)