
from django.contrib import admin
from django.urls import path
from snsapp import views
from accounts import views as accounts_Views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('postcreate', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    # 127.0.0.1:8000/detail/
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),
    path('login/' , accounts_Views.login, name="login"),
    path('logout/' , accounts_Views.logout, name="logout")
]

