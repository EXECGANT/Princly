from django.urls import path
from admins import views

urlpatterns = [
    path('admin_data/',views.AdminsView.as_view()),
    path('category/',views.CategoryView.as_view()),
    path('category/<id>',views.CategoryView.as_view()),
]