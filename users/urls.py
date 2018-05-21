'''定义leanring_logs的URL模式'''
from django.urls import path
from django.contrib.auth.views import login
'''从当前urls.py模块所在文件夹中导入视图'''
from . import views

app_name = 'users'
urlpatterns = [
    #主页
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
