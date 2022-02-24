from django.db import models

# Create your models here.

class Post(models.Model):  #defenir un Modelo = Post.
    title=models.CharField(max_length=250)
    content=models.TextField()  # agregando un post.

    def __str__(self):   # agregando un post.
        return self.title