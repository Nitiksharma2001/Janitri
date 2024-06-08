from .models import User, Operation
from .serializers import OperationSerializer, CreateOperationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getPatientsOfDoctor(req):
    try:    
        operations = Operation.objects.filter(doctor = req.user.id)
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def patientOfDoctor(req, patient_id):
    if req.method == 'POST':
        try:
            heart_rate = req.data['heart_rate']
            is_done = req.data.get('is_done', False)  # Default to False if not provided
        except KeyError as e:
            return Response({'error': f'Missing field: {e.args[0]}'}, status=status.HTTP_400_BAD_REQUEST)
        
        data = {
            'doctor': req.user.id,
            'patient': patient_id,
            'heart_rate': heart_rate,
            'is_done': is_done,
        }

        serializer = CreateOperationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if req.method == 'GET':
        operations = Operation.objects.all().filter(doctor=req.user.id, patient=patient_id)
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
