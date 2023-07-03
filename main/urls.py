from django.urls import path
from .views import TeacherList , TeacherDetail ,LoginStudentView,RegisterStudentView,GetStudentView,RefreshApiView,LogoutStudentView
urlpatterns = [
    path('teacher/', TeacherList.as_view()),
    path('teacher/<int:pk>/',TeacherDetail.as_view()),
    path('student/signup/', RegisterStudentView.as_view()), 
    path('student/login/',LoginStudentView.as_view()),
    path('student/token/', GetStudentView.as_view(), name='token-check'),
    path('student/token/refresh/',RefreshApiView.as_view()),
    path('student/logout/',LogoutStudentView.as_view())
]