from gc import get_objects
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from post.models import Post
from post.serializers import PostSerializer


class PostViewSet(viewsets.ViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    print('Get API')

    def list(self, request):
        serializer = PostSerializer(self.queryset, many=True)
        return Response(serializer.data)

        
    def create(self, request):
        print('Create new post')
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = PostSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = PostSerializer(
            instance=instance,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = PostSerializer(
            instance=instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        print('Delete post')
        instance = get_object_or_404(self.queryset, pk=pk)
        instance.delete()
        return Response("DONE")
    
