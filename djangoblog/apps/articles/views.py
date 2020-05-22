from django.shortcuts import render
from .models import Article, Comment
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArticleSerializer
from rest_framework.generics import get_object_or_404

# Create your views here.


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Article not found.")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Article not found.")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({'articles': serializer.data})

    def post(self, request):
        article = request.data.get('article')

        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"Success": "Article {} created successfully".format(article_saved.article_title)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        return Response({"success": "Article '{}' updated successfully".format(article_saved.article_title)})

    def delete(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)}, status=204)
