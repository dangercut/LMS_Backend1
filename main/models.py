from django.db import models
from django.contrib.auth.models import AbstractUser
from main.manager import UserManager
from django.conf import settings
    
#Video Model

    
class Course(models.Model):
    course_title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    course_duration = models.CharField(max_length=100)
    course_level = models.CharField(max_length=100)
    course_description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=150)
    picture_file = models.ImageField(upload_to='course_pictures/',null=True)

    def __str__(self):
        return self.course_title
class Video(models.Model):
    video_title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return self.video_title




#Student model
class Student(AbstractUser):
    username = None
    email=models.CharField(max_length=100,unique=True)
    full_name=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    mobile_number=models.CharField(max_length=20)
    address=models.TextField()
    interested_category=models.TextField()
    teaching_experience=models.CharField(max_length=100)
    availability =models.CharField(max_length=100)
    expertise_area=models.CharField(max_length=200)
    is_teacher = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects= UserManager()
    def __str__(self):
        return self.full_name



