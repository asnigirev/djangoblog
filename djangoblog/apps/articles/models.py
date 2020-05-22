from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Author(models.Model):
    author_name = models.CharField('Имя автора',max_length=255)
    author_email = models.EmailField('Email')

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length = 200)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - timezone.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length = 50)
    comment_text = models.CharField('Комментарий', max_length = 200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
