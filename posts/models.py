from django.db import models
from django.urls import reverse

# Python class setting up database structure


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field"
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    # auto now means everytime it's saved in the database updated will be set
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # whenever it's added into the datebase - set one time
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})
        # return "/posts/%s/" % (self.id)
