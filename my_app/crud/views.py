from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from crud.Schemas.users_schema import UserSchema
from .models import Users
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


def get_token(request):
    instance = User.objects.filter(username='djangouser').first()
    Token.objects.filter(user=instance).delete()
    token = Token.objects.create(user = instance)

    return JsonResponse(f"Token for Authentication is : {token.key}", safe= False)



def fetch_user_data(request):
    data = 'https://jsonplaceholder.typicode.com/users'
    api_data = requests.get(data)
    json_data = json.loads(api_data.content)
    
    for data in json_data:
        name = data.get('name')
        username = data.get('username')
        email = data.get('email')

        validate = UserSchema(data=data)

        user = Users()
        user.name = name
        user.username = username
        user.email = email

        if validate.is_valid():
            user.save()

        
    return JsonResponse(json_data, safe=False)

class ListUsers(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Users.objects.all()
    
    def get(self, request):
        queryset = self.get_queryset()
        schema = UserSchema(queryset, many=True)
        return Response(schema.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        new_data = request.data

        schema = UserSchema(data=new_data)
        if schema.is_valid():
            schema.save()
            return Response(schema.data, status=status.HTTP_200_OK)
        else:
            return Response(schema.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def put(self, request, pk):
        new_data = request.data

        try:
            instance = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        schema = UserSchema(instance, data=new_data)

        if schema.is_valid():
            schema.save()
            return Response(schema.data, status=status.HTTP_201_CREATED)
        else:
            return Response(schema.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        


    def delete(self, request, pk):
        try:
            instance = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response("", status=status.HTTP_204_NO_CONTENT)

