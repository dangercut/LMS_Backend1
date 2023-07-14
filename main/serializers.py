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


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['teaching_experience', 'availability','expertise_area']

class VideoSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField()

    class Meta:
        model = models.Video
        fields = ['video_title', 'video_file', 'course_id']

class CourseSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)
    user = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ['course_title', 'price', 'picture_file', 'course_duration', 'course_level', 'course_description', 'user', 'category', 'videos']

    def get_user(self, obj):
        if obj.user:
            return obj.user.full_name
        return None

    def create(self, validated_data):
        videos_data = validated_data.pop('videos')
        course = models.Course.objects.create(**validated_data)
        videos = []
        for video_data in videos_data:
            video_data['course'] = course
            videos.append(models.Video(**video_data))
        models.Video.objects.bulk_create(videos)
        return course

    
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)