from rest_framework import serializers
from post.models import Post, tag_choices
from datetime import datetime


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    view = serializers.IntegerField()
    text = serializers.CharField()
    time = serializers.DateTimeField()
    like = serializers.IntegerField()
    haha = serializers.IntegerField()
    sad = serializers.IntegerField()
    angry = serializers.IntegerField()
    numberOfDistribution = serializers.RelatedField(many=True, read_only=True)
    

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
<<<<<<< HEAD
        instance.numberOfDistribution = validated_data.get('numberOfDistribution', instance.numberOfDistribution)
=======
        instance.tag = validated_data.get('tag', instance.tag)
        instance.number_of_distribution = validated_data.get('number_of_distribution', instance.number_of_distribution)
>>>>>>> parent of 9b48b3e... view all post
        instance.save()
    
        return instance
