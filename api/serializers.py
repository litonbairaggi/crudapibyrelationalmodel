from rest_framework import serializers 
from api.models import Result, Student

class ResultSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Result
        fields = ('__all__')

class StudentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Student
        fields = ('__all__')