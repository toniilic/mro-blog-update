# blog/urls.py

from django.urls import path
from .views import blog_post, voting_results

urlpatterns = [
    path('post/<int:post_id>/', blog_post, name='blog_post'),
    path('results/', voting_results, name='voting_results'),
]

