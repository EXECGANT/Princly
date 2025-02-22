from django.urls import path
from school import views

urlpatterns = [
    # SCHOOL
    path('schools/',views.SchoolView.as_view()),
    path('schools/<id>',views.SchoolView.as_view()),
    # CLASSES
    path('classes/',views.SchoolClassView.as_view()),# TODO: Headers Must Have CLASS ID 
    path('classes/<id>',views.SchoolClassView.as_view()),
    # SUBJECTS
    path('subjects/',views.SchoolSubjectsView.as_view()),# TODO: Headers Must Have CLASS ID 
    path('subjects/<id>',views.SchoolSubjectsView.as_view()),
    # VIDEOS
    path('videos/',views.SchoolVideoView.as_view()),# TODO: Headers Must Have SUBJECT ID 
    path('videos/<id>',views.SchoolVideoView.as_view()),
    # PDF FILES
    path('files/',views.SchoolFileView.as_view()),# TODO: Headers Must Have SUBJECT ID 
    path('files/<id>',views.SchoolFileView.as_view()),
]