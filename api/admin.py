from django.contrib import admin

# Register your models here.
# from poormanstwitter.api.models import Tweet
from .models import Tweet

admin.site.register(Tweet)