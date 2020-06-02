from django.db import connection
from django.urls import reverse
from rest_framework.test import APITestCase

from .models import Article, Author

class TestArticlesListAPIView(APITestCase):
    def test_missing_authors(self):
        self.author_ex = Author.objects.create(
            author_name='Adolf Hitler',
            author_email='adik1488@zh.de'
        )
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM articles_author WHERE id = %s', [self.author_ex.id])
        self.exp_authors = [
            {
                "author_name": "Adolf Hitler",
                "author_email": "adik1488@zh.de"
            }
        ]
        resp = self.client.get('http://localhost:8000/api/authors/')
        self.assertListEqual(self.exp_authors, resp.data['author'])

    def test_missing_articles(self):
        self.article_name = Article.objects.create(
            article_title='title',
            article_text='Ttitlle tutle lasasd',
            pub_date='2020-05-21T18:45:00Z',
            author_id='1'
        )

        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM articles_article WHERE id = %s', [self.article_name.id])

        self.exp_articles = [
            {
                'article_text': 'Ttitlle tutle lasasd',
                'article_title': 'title',
                'author_id': 1,
                'pub_date': '2020-05-21T18:45:00Z'
            }
        ]


        resp = self.client.get('http://localhost:8000/api/articles/')
        self.assertListEqual(self.exp_articles, resp.data['articles'])
