from django.shortcuts import render
from .serializers import TeacherSerializers, StudentSerializers
from rest_framework import generics,permissions
from . import models
from rest_framework_simplejwt.authentication import JWTAuthentication

class TeacherDetail(generics.RetrieveDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes =[JWTAuthentication]
    

class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes =[JWTAuthentication]

class StudentDetail(generics.RetrieveDestroyAPIView):
    lookup_field='pk'
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class StudentListGet(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class StudentListPost(generics.CreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializers
