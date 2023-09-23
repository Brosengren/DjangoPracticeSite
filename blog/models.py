from ctypes.wintypes import tagSIZE
import email
from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name      = models.CharField(max_length=64)
    last_name       = models.CharField(max_length=128)
    email_address   = models.EmailField(max_length=128)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Tag(models.Model):
    tag = models.CharField(max_length=32)

    def __str__(self):
        return self.tag


class Post(models.Model):
    title               = models.CharField(max_length=128, null=False)
    excerpt             = models.CharField(max_length=256, null=False)
    image               = models.ImageField(upload_to="posts", null=True)
    date_created        = models.DateTimeField(auto_now_add=True)
    date_last_modified  = models.DateTimeField(auto_now=True)
    slug                = models.SlugField(unique=True, db_index=True)
    content             = models.TextField(validators=[MinLengthValidator(16)])
    author              = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags                = models.ManyToManyField(Tag, related_name="posts")

    def get_url(self):
        return reverse("post-details", args=[self.slug])

    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name   = models.CharField(max_length=64)
    user_email  = models.EmailField(max_length=128)
    text        = models.TextField(max_length=1024)
    post        = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

