from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path("", views.starting_page, name="starting-page"),
    path("", views.StartingPageView.as_view(), name="starting-page"),
    # path("posts", views.posts, name="posts-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    # path("posts/<slug:slug>", views.post_detail, name="post-detail-page"), 
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),
    #blog/my-first-post slug:slug makes sure only urls with a correct path will trigger
    path("read-later", views.ReadLaterView .as_view(), name="read-later")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
