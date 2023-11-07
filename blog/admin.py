from django.contrib import admin

from .models import Post, Author, Tag, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", "date_created",)
    list_display = ("title", "date_created", "author",)
    search_fields = ("title",)


# class AuthorAdmin(admin.ModelAdmin):
#     pass


# class TagAdmin(admin.ModelAdmin):
#     pass

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)