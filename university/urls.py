from django.urls import path
from university import views

urlpatterns = [
    # UNIVERSITY  
    path('university/',views.UniversityViews.as_view()),
    path('university/<id>',views.UniversityViews.as_view()), 
    # COURSE
    path('courses/',views.UniversityCourseView.as_view()),# TODO: Headers Must Have UNIVERSITY ID 
    path('courses/<id>',views.UniversityCourseView.as_view()), 
    # DEGREE
    path('degree/',views.CourseDegreeView.as_view()), # TODO: Headers Must Have COURSE ID 
    path('degree/<id>',views.CourseDegreeView.as_view()),
    # YEAR
    path('year/',views.DegreeYearView.as_view()), # TODO: Headers Must Have DEGREE ID 
    path('year/<id>',views.DegreeYearView.as_view()),
    # SEMSTER
    path('semester/',views.SemesterView.as_view()), # TODO: Headers Must Have YAER ID 
    path('semester/<id>',views.SemesterView.as_view()),
    # SUBJECTS
    path('subjects/',views.SemesterSubjectsView.as_view()), # TODO: Headers Must Have SEMESTER ID 
    path('subjects/<id>',views.SemesterSubjectsView.as_view()),
    # VIDEOS
    path('videos/',views.UniversityVideoView.as_view()), # TODO: Headers Must Have SUBJECT ID 
    path('videos/<id>',views.UniversityVideoView.as_view()),
    # PDF FILES
    path('files/',views.UniversityFileView.as_view()), # TODO: Headers Must Have SUBJECT ID 
    path('files/<id>',views.UniversityFileView.as_view()), 
]