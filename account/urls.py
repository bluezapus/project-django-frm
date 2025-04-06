from django.urls import path
from django.contrib.auth.views import (
    LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
)

from . import views

app_name = 'account'
urlpatterns = [
    path('', views.index_profiles, name='index'),
    path('update/user/', views.update_Profiles, name='update_profile'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'), #login
    path('logout/', views.LogoutView, name='logout'), #logout
    path('register/', views.register_users, name='register'), #register
    path('password_reset/', PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password_reset"), #form reset password
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"), #form reset done
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"), #confirm password reset
    path('reset/done/', PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"), #complete password reset
    #management password by user account
    path('password_change/', PasswordChangeView.as_view(template_name="registration/password_change_form.html"), name="password_change"), #change password by user
    path('password_change/done/', PasswordChangeView.as_view(template_name="registration/password_change_done.html"), name="password_change_done"), #change password by user

]