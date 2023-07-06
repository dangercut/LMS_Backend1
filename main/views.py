from django.shortcuts import render
from main.serializers import TeacherSerializers, StudentSerializers
from rest_framework import generics,permissions
from . import models
from rest_framework.authentication import get_authorization_header
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Student
from rest_framework.exceptions import AuthenticationFailed,APIException
import jwt
from datetime import datetime, timedelta
from main.serializers import StudentSerializers,ChangePasswordSerializer
from main.authentication import create_access_token,create_refresh_token,decode_access_token,decode_refresh_token


class TeacherDetail(generics.RetrieveDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializers
     

class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializers
    

class StudentDetail(generics.RetrieveDestroyAPIView):
    lookup_field='pk'
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.IsAuthenticated]


class RegisterStudentView(APIView):
    def post(self,request):
        serializer = StudentSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginStudentView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = Student.objects.filter(email=request.data['email']).first()

        if not user:
            raise APIException('Invalid credentials!')

        if not user.check_password(request.data['password']):
            raise APIException('Invalid credentials!')
        access_token=create_access_token(user.id)
        refresh_token=create_refresh_token(user.id)
        response=Response()
        response.data={
            'access_token':access_token,
            'refresh_token':refresh_token
        }
        return response

class GetStudentView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()
        print(auth)
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = Student.objects.filter(pk=id).first()

            return Response(StudentSerializers(user).data)

        raise AuthenticationFailed('unauthenticated')   

class RefreshApiView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')  
        id=decode_refresh_token(refresh_token) 
        access_token=create_access_token(id)
        return Response({
            "accessToken":access_token,
        })

class ChangeStudentPassword(APIView):
    def post(self, request):
        auth = get_authorization_header(request).split()
        print(auth)
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = Student.objects.filter(pk=id).first()
            serializer = ChangePasswordSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            old_password = request.data.get('old_password')
            new_password = request.data.get('new_password')

            if not user.check_password(old_password):
                raise APIException('Wrong old password!')
            user.set_password(new_password)
            user.save()

            return Response({'message': 'Password changed successfully.'})

        raise AuthenticationFailed('unauthenticated')

