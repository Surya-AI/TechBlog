from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='Blog'),
    path('blog/create/', views.BlogCreateView.as_view(), name='Blog Create'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='Post'),
    path('post/create/', views.PostCreateView.as_view(), name='Post Create'),
    path('about/', views.about, name='About')
]
