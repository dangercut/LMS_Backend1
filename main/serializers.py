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