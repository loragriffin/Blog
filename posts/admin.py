from django.contrib import admin

# Register your models here.
from .models import Post

# ModelAdmin is referring to admin inside models.py
# these settings and variables are found from the documentation


class PostAdmin(admin.ModelAdmin):
    # this determines what fields are displayed in the post list on admin site
    list_display = ["__str__", "updated", "timestamp"]
    # list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    # list_editable = ["title"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post


# adds Post to admin site
admin.site.register(Post, PostAdmin)
