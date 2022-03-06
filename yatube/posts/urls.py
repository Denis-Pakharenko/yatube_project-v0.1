from django.urls import URLPattern, path
from . import views

app_name = 'posts' 

urlpatterns = [
    path('', views.index, name = 'index'),
    path('group_list.html', views.group_posts, name= 'group_list')
]