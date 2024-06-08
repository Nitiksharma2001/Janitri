from rest_framework import serializers
from .models import Operation
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email']

class OperationSerializer(serializers.ModelSerializer):
    doctor = UserSerializer()
    patient = UserSerializer()
    
    class Meta:
        model = Operation
        fields = "__all__"
        depth = 1

class CreateOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"
        depth = 1
        
