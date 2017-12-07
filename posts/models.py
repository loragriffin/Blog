from django.db import models

# Python class setting up database structure


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    # auto now means everytime it's saved in the database updated will be set
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # whenever it's added into the datebase - set one time
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
