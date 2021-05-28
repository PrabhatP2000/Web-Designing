from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('email/',views.email,name='email'),
    path('login_signup/',views.login_signup,name='login_signup'),
    path('result',views.result,name='result'),
    path('te_result',views.te_result,name='te_result'),
]
