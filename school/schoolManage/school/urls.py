from django.urls import path
from .views import   ClassList, ClassDetail,AttendanceList, AttendanceDetail, SubjectList, SubjectDetail, ExamList, ExamDetail, MarksList, MarksDetail  
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserRegistrationView, UserLoginView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    
    #register and login
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # #user
    # path('api/users', UserList.as_view(), name='user-list'),
    # path('api/users/<int:id>/', UserDetail.as_view(), name='user-detail'),

    # #jwt token
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #class
    path('api/classes', ClassList.as_view(), name='class-list'),
    path('api/classes/<int:id>/', ClassDetail.as_view(), name='class-detail'),

    #Attendance
    path('api/attendances', AttendanceList.as_view(), name='attendance-list'),
    path('api/attendances/<int:id>/', AttendanceDetail.as_view(), name='attendance-detail'),

#Subject
    path('api/subjects', SubjectList.as_view(), name='subject-list'),
    path('api/subjects/<int:id>/', SubjectDetail.as_view(), name='subject-detail'),

    #Exam
    path('api/exams', ExamList.as_view(), name='exam-list'),
    path('api/exams/<int:id>/', ExamDetail.as_view(), name='exam-detail'),

    #Marks
    path('api/marks', MarksList.as_view(), name='marks-list'),
    path('api/marks/<int:id>/', MarksDetail.as_view(), name='marks-detail'),
]
