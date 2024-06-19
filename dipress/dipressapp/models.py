from django.db import models


class Article(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    query = models.TextField()
    wikipedia_uri = models.TextField()
    content = models.TextField()

    class Meta:
        ordering = ['-date_added']
