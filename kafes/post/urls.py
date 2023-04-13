from django.urls import path
from .views import *

app_name = 'post'
urlpatterns = [

    path(r'index/',post_index, name='index'),
    path(r'create/',post_create, name='create'),
    path('detail/<slug:slug>', post_detail, name='detail'),
    path('update/<slug:slug>', post_update, name='update'),
    path('delete/<slug:slug>', post_delete, name='delete'),
]