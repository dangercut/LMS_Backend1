from django.urls import path,include
from .views import TeacherList , TeacherDetail ,StudentListGet,StudentDetail,StudentListPost
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('teacher/', TeacherList.as_view()),
    path('teacher/<int:pk>/',TeacherDetail.as_view()),
    path('student/',StudentListGet.as_view()),
    path('student/signup/',StudentListPost.as_view()),
    path('student/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('student/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
]