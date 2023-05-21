from django.urls import path,include
from .views import TeacherList , TeacherDetail
urlpatterns = [
    path('teacher/', TeacherList.as_view()),
    path('teacher/<int:pk>/',TeacherDetail.as_view()),
    path('api-auth',include('rest_framework.urls'))
]