from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        post.content = request.POST.get("content", post.content)
        post.votes = request.POST.get("votes", post.votes)
        post.save()
    return render(request, "blog/blog_post.html", {"post": post})
