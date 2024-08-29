from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPosts, name='posts'),
    # path('post-detail/<int:pk>/', views.post_detail, name='posts_detail'),
]
