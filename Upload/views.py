from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import FileSerializer
from .models import File

class FileUploadView(APIView):
    permission_classes = []
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileFetchView(APIView):
    permission_classes = []

    def get(self,request):

        all_files = File.objects.all()
        serializer = FileSerializer(all_files,many=True)

        return Response(serializer.data)

# End point for uploading any file
"http://127.0.0.1:8000/api/files"