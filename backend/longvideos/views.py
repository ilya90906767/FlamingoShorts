from django.shortcuts import render
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializiers import LongVideoSerializer

class LongVideoUploadView(APIView):
    def post(self, request):
        serializer = LongVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
