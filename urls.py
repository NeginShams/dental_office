from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_page,name='home_page'),
    path('login/',views.login_page,name='login_page'),
    path('user_panel/',views.user_panel,name="user_panel"),
    path('create/',views.create_account, name="create_account")
    ]