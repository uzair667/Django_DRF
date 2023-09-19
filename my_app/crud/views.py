from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from crud.Schemas.users_schema import UserSchema
from crud.Schemas.posts_schema import PostSchema
from .models import Users,Posts

def hello(request):
    data = 'https://jsonplaceholder.typicode.com/users'
    api_data = requests.get(data)
    json_data = json.loads(api_data.content)

    # schema = UserSchema(data=json_data, many=True)
    for data in json_data:
        name = data.get('name')
        username = data.get('username')
        email = data.get('email')

    
        user = Users()
        user.name = name
        user.username = username
        user.email = email
        user.save()

    
    return HttpResponse(json_data)

