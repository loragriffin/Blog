from django.contrib import admin

# Register your models here.
from .models import Post

# adds Post to admin site
admin.site.register(Post)
