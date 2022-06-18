from django.contrib import admin
from .models import Post
# Register your models here.
class PostDB(admin.ModelAdmin):
    list_display = [
        "post_title", "text", "author", "created_date", "published_date"
    ]