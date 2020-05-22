
from rest_framework import serializers

from .models import Article

class ArticleSerializer(serializers.Serializer):
    article_title = serializers.CharField(max_length=200)
    article_text = serializers.CharField()
    pub_date = serializers.DateTimeField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.article_title = validated_data.get('article_title', instance.article_text)
        instance.article_text = validated_data.get('article_text', instance.article_text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance
