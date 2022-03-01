from django.conf.urls import url
from . import views

urlpatterns = [
    url('regist_user', views.RegistUser.as_view(), name='regist_user'),
    url('applogin',views.AppLogin.as_view(), name='app_login'),
]