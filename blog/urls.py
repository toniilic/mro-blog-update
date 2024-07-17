from django.urls import path
from .views import blog_post

urlpatterns = [
    path('post/<int:post_id>/', blog_post, name='blog_post'),
]
