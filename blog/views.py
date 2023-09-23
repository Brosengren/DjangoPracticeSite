from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Post
from .forms import CommentForm
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse

# blog_entries={
#    "Nature is Lit": {
#         "pic": "flower.webp",
#         "desc": "Do you see how dope these flowers are?",
#     },
#     "What's for Dinner?":{
#         "pic": "stove.jpg",
#         "desc": "I've been eating all kinds of different foods",
#     },
#     "Cars are Kinda Cool":{
#         "pic": "mustang.webp",
#         "desc": "I saw this car and though it was kinda neat.",
#     },
# }

# all_posts = [
#     {
#         "slug": "hike-in-the-mountains",
#         "image": "mustang.webp",
#         "author": "Braden",
#         "date": date(2021, 1, 31),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothing like the views when hiking in the mountains and I wasn't even prepared for what happened next",
#         "content": """
#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """,
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "flower.webp",
#         "author": "Maximilian",
#         "date": date(2022, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "stove.jpg",
#         "author": "Maximilian",
#         "date": date(2020, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "hike-in-the-mountains2",
#         "image": "mustang.webp",
#         "author": "Braden",
#         "date": date(2017, 1, 31),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothing like the views when hiking in the mountains and I wasn't even prepared for what happened next",
#         "content": """
#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """,
#     },
#     {
#         "slug": "programming-is-fun2",
#         "image": "flower.webp",
#         "author": "Maximilian",
#         "date": date(2018, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods2",
#         "image": "stove.jpg",
#         "author": "Maximilian",
#         "date": date(2019, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
# ]

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
            "comment_form":CommentForm()
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
            "comment_form": comment_form
        }
        return render(request, "blog/post-detail.html", context)