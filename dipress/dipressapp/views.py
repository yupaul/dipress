from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dipressapp.models import Article
from dipressapp.serializers import ListSerializer, ArticleSerializer
from dipressapp.lib.gen import generate


@api_view(['GET'])
def list_all(request, format=None):
    article_ids_queries = Article.objects.all()
    s = ListSerializer(article_ids_queries, many=True)
    return Response(s.data)


@api_view(['GET'])
def read(request, pkey, format=None):
    try:
        article = Article.objects.get(pk=pkey)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    s = ArticleSerializer(article)
    return Response(s.data)


@api_view(['POST'])
def create(request, format=None):
    if not request.data or 'query' not in request.data or len(request.data['query']) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)
    generated = generate(request.data['query'])
    if not generated:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {
        'query': request.data['query'],
        'wikipedia_uri': generated[0],
        'content': generated[1],
    }
    s = ArticleSerializer(data=data)
    if s.is_valid():
        s.save()
        return Response(s.data, status=status.HTTP_201_CREATED)
    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
