from django.urls import path
from .views import LoginStudentView,VideoCreateView,CourseDetailView,CourseCreateView,SubmitTeacherForm,ChangeStudentPassword,RegisterStudentView,GetStudentView,RefreshApiView
urlpatterns = [
    path('student/signup/', RegisterStudentView.as_view()), 
    path('student/login/',LoginStudentView.as_view()),
    path('student/info/', GetStudentView.as_view(), name='token-check'),
    path('student/token/refresh/',RefreshApiView.as_view()),
    path('student/change_password/',ChangeStudentPassword.as_view()),
    path('teacher/form/',SubmitTeacherForm.as_view()),
    path('courses/create/', CourseCreateView.as_view(), name='course-create'),  
    path('courses/view/<int:pk>/',CourseDetailView.as_view()),
    path('courses/view/',CourseDetailView.as_view()),
    path('videos/create/', VideoCreateView.as_view(), name='create-video'),
]