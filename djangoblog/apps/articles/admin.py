from django.contrib import admin

from .models  import Article, Comment, Author

# Register your models here.
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)
