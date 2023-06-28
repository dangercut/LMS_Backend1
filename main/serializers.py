from . import models
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('full_name', 'email', 'password', 'qualification', 'mobile_number', 'address', 'interested_category')

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