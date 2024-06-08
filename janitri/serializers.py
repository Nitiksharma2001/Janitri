from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    # role = serializers.CharField()
    
    def validate(self, data):

        if not data['username'] or not data['email'] or not data['password'] :
            raise serializers.ValidationError('add all details')
            
        if User.objects.filter(email = data['email']).exists():
            raise serializers.ValidationError('user already exists')
        
        return data
    
    def create(self, data):
        user = User.objects.create(email=data['email'], username=data['username'])
        user.set_password(data['password'])
        user.save()
        return data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):

        if not data['username'] or not data['password'] :
            raise serializers.ValidationError('add all details')
            
        if not User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('user not exists')
        
        return data
