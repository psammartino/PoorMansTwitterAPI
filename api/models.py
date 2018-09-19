from django.db import models


class Tweet(models.Model):
    name = models.CharField(max_length=70)
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
