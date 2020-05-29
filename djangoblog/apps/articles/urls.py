from django.urls import path
from . import views
from .views import ArticleView


app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
#    path('<int:article_id>/published_by/', views.published_by, name = 'published_by'),
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
]
