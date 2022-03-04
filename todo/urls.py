from django.conf.urls import url
from . import views

urlpatterns = [
    url('create', views.TaskCreate.as_view(), name='create'),
    url('select', views.TaskCreate.as_view(), name='select')
]