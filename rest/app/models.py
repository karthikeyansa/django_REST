from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    owner = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.title} {self.body} {self.owner}'