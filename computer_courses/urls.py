from django.urls import path
from computer_courses import views

urlpatterns = [
    # COMPUTER COURSES
    path('courses/',views.ComputerCourseView.as_view()),
    path('courses/<id>',views.ComputerCourseView.as_view()),
    # COMPUTER SUBJECTS
    path('subjects/',views.ComputerSubjectView.as_view()),# TODO: Headers Must Have COURSE ID 
    path('subjects/<id>',views.ComputerSubjectView.as_view()),
    # VIDEOS
    path('videos/',views.ComputerVideoView.as_view()),# TODO: Headers Must Have SUBJECT ID 
    path('videos/<id>',views.ComputerVideoView.as_view()),
    # FILES
    path('files/',views.ComputerFileView.as_view()),# TODO: Headers Must Have SUBJECT ID 
    path('files/<id>',views.ComputerFileView.as_view()),
]