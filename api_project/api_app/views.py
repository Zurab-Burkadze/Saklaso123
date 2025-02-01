from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Saklaso
from .serializers import SaklasoSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        serializer = SaklasoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : f'{request.data["title"]} Created'},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    saklasos = Saklaso.objects.all()
    serializer = SaklasoSerializer(instance=saklasos, many=True)
    

    return Response(serializer.data)
