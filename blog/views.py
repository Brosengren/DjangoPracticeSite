from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Post, Comment
from .forms import CommentForm
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def get_date(post):
    return post['date']

# def starting_page(request):
#   # data = list(blog_entries.items())
#   # return render(request, "blog/starting_page.html", {"blog_entries":blog_entries}
#     # sorted_posts = sorted(all_posts, key=get_date)
#     # latest_posts = sorted_posts[-3:]
#     latest_posts = Post.objects.all().order_by("-date_created")[:3] #Django does not support doing this by [:-3]
#     return render(request, "blog/starting_page.html", {"posts":latest_posts})

#Doing this to practice class views
class StartingPageView(ListView):
    template_name = "blog/starting_page.html"
    model = Post
    ordering = ["-date_created"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# def posts(request):
#     # sorted_posts = sorted(all_posts, key=get_date, reverse=True)
#     sorted_posts = Post.objects.all().order_by("-date_created")
#     return render(request, "blog/all-posts.html", {"posts":sorted_posts})
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date_created"]
    context_object_name = "posts"


# def post_detail(request, slug):
#     # identified_post = next(post for post in all_posts if post['slug'] == slug)
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {"post": identified_post})
class SinglePostView(View):
    template_name = "blog/post-detail.html"
    model = Post

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags":post.tags.all(),
            "comment_form":CommentForm(),
            "comments":post.comments.all().order_by("-id") # type: ignore
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form  = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags":post.tags.all(),
            "comment_form": comment_form,
            "comments":post.comments.all().order_by("-id") # type: ignore
        }
        return render(request, "blog/post-detail.html", context)