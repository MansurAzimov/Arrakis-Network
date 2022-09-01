from tabnanny import verbose
from django.db import models

class Post (models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField (max_length=250)
    body = models.TextField ()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

