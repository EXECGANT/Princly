from django.urls import path
from user import views

urlpatterns = [
    path('signup/',views.SignupView.as_view()),
    path('login/',views.LoginView.as_view()),
    path('forgetpassword/',views.ForgetPasswordView.as_view()),
    path('resetpassword/<id>',views.ForgetPasswordView.as_view()),
    
    path('User/',views.UsersView.as_view()),
]