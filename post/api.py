import random
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from post.models import Post
from post.serializers import PostCreateSerializer


def post_list(request):
    if request.method == 'GET':
        posts = list(Post.objects.filter(numberOfDistribution__gte=1))
        posts = reduce_distribute(posts)
        lenght = len(posts)
        if lenght < 5:
            allPosts = list(Post.objects.all().order_by('-time'))
            posts += allPosts[:5-lenght]
            print('Post by Time')
        random.shuffle(posts)
        serializer = PostCreateSerializer(set(posts), many=True)
        print('Get Post', serializer.data)
        return JsonResponse(serializer.data, safe=False)

def distribute_post(request, post_id):
    user = request.user
    check = Post.objects.filter(pk=post_id ,distributeUser__user__id=user.id)
    if check:
        print("You've already distributed this post")
    else:
        post = Post.objects.get(pk=post_id)
        post.numberOfDistribution += 5
        post.save()
        post.distributeUser.add(user.authen_user.randomName())
        print("distributed post")
    return HttpResponse(200)

def reduce_distribute(posts):
    random.shuffle(posts)
    for post in posts[:5]:
        post.numberOfDistribution -= 1
        post.save()
    return posts[:5]