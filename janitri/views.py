from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from .serializers import RegisterSerializer, LoginSerializer

@api_view(['GET','POST'])
def getOrCreateUser(req):
    if req.method == 'POST':
        serializer = RegisterSerializer(data=req.data)
        
        if not serializer.is_valid():
            return Response({
                'success': False,
                'message': 'user not created',
            }, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({'success': True, 'message': 'user created'}, status=status.HTTP_201_CREATED)
                
    else:
        username = req.GET.get('username', '')
        password = req.GET.get('password', '')
        
        data = {
            'username': username, 
            'password': password
        }
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'success': False,
                'message': 'add all details',
            }, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=serializer.data['username'],  password = serializer.data['password'])

        if user is None:
            return Response({
                'success': False,
                'message': 'invalid credentials',
            }, status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'success': True, 'message': 'logged in successfully', 'token': str(token)}, status=status.HTTP_200_OK)