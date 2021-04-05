from django.shortcuts import render

# Create your views here.
from api.models import Student, Result
from .serializers import StudentSerializer
from .serializers import ResultSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ResultList(APIView):
    def get(self, request):
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResultDetail(APIView):
    def get_object(self, pk):
        try:
            return Result.objects.get(pk=pk)
        except Result.DoesNotExist:
            return Response()

    def get(self, request, pk):
        results = self.get_object(pk)
        serializer = ResultSerializer(results)
        return Response(serializer.data)

    def put(self, request, pk):
        results = self.get_object(pk)
        serializer = ResultSerializer(results, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        results = self.get_object(pk)
        results.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        


