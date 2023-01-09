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

class Comment(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    message = models.TextField (max_length=300)

    def __str__(self) -> str:
        return self.message

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

