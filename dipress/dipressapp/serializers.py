from rest_framework import serializers
from dipressapp.models import Article


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'date_added', 'query', ]


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

