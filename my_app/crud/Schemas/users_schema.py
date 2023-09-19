from rest_framework import serializers
from ..models import Users

class UserSchema(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','name','username','email','password']
