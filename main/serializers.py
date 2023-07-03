from . import models
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id','full_name', 'email', 'password', 'qualification', 'mobile_number', 'address', 'interested_category']
        extra_kwargs={
            "password": {"write_only": True} # to allow write only for the password
        }
    def create(self,validated_data):
        password=validated_data.pop('password',None)
        student =models.Student(**validated_data)
        if password is not None:
            student.set_password(password)
        student.save()
        return  student


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields =('id','full_name', 'email', 'password', 'qualification', 'mobile_number', 'address')

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields ="__all__"

class CourseCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model= models.CourseCategory
        fields= "__all__"