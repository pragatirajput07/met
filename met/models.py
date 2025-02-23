from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


# Create your models here.

class Tweet(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(max_length=300)
    photo=models.ImageField(upload_to='photoss/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}-{self.text[:100]}'
    @staticmethod
    def search_tweets(query):
        """
        Searches tweets containing the given query (case-insensitive).
        Works with SQLite.
        """
        return Tweet.objects.filter(text__icontains=query)
