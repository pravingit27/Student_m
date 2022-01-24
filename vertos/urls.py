from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('student/',views.StudentView.as_view(),name='Student_Detail'),
    path('student/<int:pk>',views.StudentDetailView.as_view(),name='Single_Student'),
    path('user',views.UserView.as_view(),name='UserDetail'),
    path('user/<int:pk>/',views.UserDetailView.as_view(),name='Single_User'),
    path('standard',views.StandardView.as_view(),name='Standard_Detail'),
    path('standard/<int:pk>',views.StandardDetailView.as_view(),name='Single_Standard'),
    path('section',views.SectionView.as_view(),name='Section_Detail'),
    path('section/<int:pk>',views.SectionDetailView.as_view(),name='Single_Student'),
    path('major',views.MajorView.as_view(),name='Major_Details'),
    path('major/<int:pk>',views.MajorDetailView.as_view(),name='Single_Major'),
    path('class',views.ClassView.as_view(),name='Class_Details'),
    path('class/<int:pk>',views.ClassDetailView.as_view(),name='Single_Class'),
    path('staff',views.StaffView.as_view(),name='Staff_Details'),
    path('staff/<int:pk>',views.StaffDetailView.as_view(),name='Single_Staff'),
    path('staff/teaching',views.TeachingStaffView.as_view(),name='Teaching_Staff_Details'),
    path('staff/teaching/<int:pk>',views.TeachingStaffDetailView.as_view(),name='Single_Teaching_Staff'),
    path('subject',views.SubjectView.as_view(),name='subject_details'),
    path('subject/<int:pk>',views.SubjectDetailView.as_view(),name='single_subject_details'),
    path('exam',views.ExamView.as_view(),name='ExamDetail'),
    path('exam/<int:pk>',views.ExamDetailView.as_view(),name='SingleExam'),
    path('exam/category',views.ExamCategoryView.as_view(),name='ExamCategoryDetails'),
    path('exam/category/<int:pk>',views.ExamCategoryDetailView.as_view(),name='SingleExamCategory'),
    path('result',views.ResultView.as_view(),name='Result_Detail'),
    path('result/<int:pk>',views.ResultDetailView.as_view(),name='Single_Result'),
    path('school',views.SchoolView.as_view(),name='School_Detail'),
    path('school/<int:pk>',views.SchoolDetailView.as_view(),name='Single_School'),
    path('logout',views.LogoutView.as_view(),name = 'logout'),
]
