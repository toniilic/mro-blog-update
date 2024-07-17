
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        if "content" in request.POST:
            post.content = request.POST.get("content", post.content)
        if "votes" in request.POST:
            post.votes = request.POST.get("votes", post.votes)
        post.save()
    return render(request, "blog/blog_post.html", {"post": post})

def voting_results(request):
    posts = BlogPost.objects.all()
    return render(request, "blog/voting_results.html", {"posts": posts})

