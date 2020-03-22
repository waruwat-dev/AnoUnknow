from rest_framework import serializers
from post.models import Post, tag_choices
from datetime import datetime


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    view = serializers.IntegerField(default=0, required=False)
    text = serializers.CharField()
    time = serializers.DateTimeField(default=datetime.now)
    like = serializers.IntegerField(default=0, required=False)
    haha = serializers.IntegerField(default=0, required=False)
    sad = serializers.IntegerField(default=0, required=False)
    angry = serializers.IntegerField(default=0, required=False)
    tag = serializers.ChoiceField(choices=tag_choices)
    number_of_distribution = serializers.IntegerField(default=0, required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """

        instance.view = validated_data.get('view', instance.view)
        instance.text = validated_data.get('text', instance.text)
        instance.time = validated_data.get('time', instance.time)
        instance.like = validated_data.get('like', instance.like)
        instance.haha = validated_data.get('haha', instance.haha)
        instance.sad = validated_data.get('sad', instance.sad)
        instance.angry = validated_data.get('angry', instance.angry)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.number_of_distribution = validated_data.get('number_of_distribution', instance.number_of_distribution)
        instance.save()
    
        return instance
