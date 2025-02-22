from django.urls import path
from competitive_exam import views

urlpatterns = [
    # COMPETITRIVE EXAMS: 
    path('exams/',views.CompetitiveExamsView.as_view()),
    path('exams/<id>',views.CompetitiveExamsView.as_view()),
    # SUBJECTS
    path('subjects/',views.ExamSubjectsView.as_view()),# TODO: Headers Must Have EXAM ID 
    path('subjects/<id>',views.ExamSubjectsView.as_view()),
    # VIDEO
    path('videos/',views.ExamVideoView.as_view()),# TODO: Headers Must Have SUBJECT ID 
    path('videos/<id>',views.ExamVideoView.as_view()),
    # PDF FILES
    path('files/',views.ExamFileView.as_view()),# TODO: Headers Must Have SUBJECT ID 
    path('files/<id>',views.ExamFileView.as_view()),
]