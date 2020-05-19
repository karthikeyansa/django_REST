from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.body} {self.owner}'