from django.urls import path
from django.contrib.auth import views as login_view
from . import views

urlpatterns = [
    # path('', views.users, name='Users'),
    path('people/', views.UserListView.as_view(), name='People'),
    path('profile/', views.profile, name='Profile'),
    path('profile/<int:pk>', views.profile, name='NamedProfile'),
    path('explore/', views.explore, name='Explore'),
    path('login/', login_view.LoginView.as_view(template_name='users/login.html'), name='Login'),
    path('logout/', login_view.LogoutView.as_view(template_name='users/logout.html'), name='Logout'),
    path('register/', views.register, name='Register')
]
