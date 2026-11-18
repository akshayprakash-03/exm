from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import student
from student.models import Student
from student.permissions import IsSuperUserOrReadOnly
from student.serializers import StudentSerializer


# Create your views here.
class ListCreateStudents(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsSuperUserOrReadOnly]
    def get(self,request):
        s=Student.objects.all()
        serializer_instance=StudentSerializer(s,many=True)
        return Response(serializer_instance.data)
    def post(self,request):
        serializer_instance=StudentSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class RetriveUpdateDeleteStudent(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]
    def get(self,request,i):
        s=get_object_or_404(Student,id=i)
        serializer_instance=StudentSerializer(s)
        return Response(serializer_instance.data)
    def put(self,request,i):
        s=get_object_or_404(Student,id=i)
        serializer_instance=StudentSerializer(s,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,i):
        s=get_object_or_404(Student,id=i)
        s.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)