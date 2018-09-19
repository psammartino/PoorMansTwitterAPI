from rest_framework import serializers

from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id', 'name', 'content', 'created')

    def create(self, validated_data):
        return Tweet.objects.create(**validated_data)

