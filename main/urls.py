from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('email/',views.email,name='email'),
    path('contact',views.contact,name='contact'),
    path('login',views.user_login,name='user_login'),
    path('result',views.result,name='result'),
    path('contact',views.contact,name='contact'),
    path('admission_form',views.admission_form,name='admission_form'),
    path('gallery',views.gallery,name='gallery'),
    path('te_result',views.te_result,name='te_result'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('computer_department',views.comp_department,name='comp_dept'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="reset/password_reset.html"),name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="reset/password_reset_sent.html"),name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="reset/password_reset_form.html"),name="password_reset_confirm"),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="reset/password_reset_done.html"),name="password_reset_complete"),
]
