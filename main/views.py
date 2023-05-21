from django.shortcuts import render
from .serializers import TeacherSerializers
from rest_framework import generics,permissions
from . import models

class TeacherDetail(generics.RetrieveDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes=[permissions.IsAuthenticated]
    

class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes=[permissions.IsAuthenticated]