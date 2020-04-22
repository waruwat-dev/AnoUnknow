from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user.models import User, Authen_User
from user.forms import SignUpForm
from post.form import PostForm
from post.models import Post
from comment.models import Comment
from django.http.response import HttpResponse

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'form':form})
        # else:
        #     form = SignUpForm()
        #     return render(request, 'signup.html', {'form': form})
            # return render(request, 'signup.html', {'form': form})
    # else:
    #     form = SignUpForm()
    #     return render(request, 'signin.html', {'form': form})
    return HttpResponse(status=404)


def signin(request):
    context = {}
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next','/'))
        else:
            context['username'] = username
            print(user)
            context['error'] = "username or password is wrong"
            return render(request, 'signin.html', context)
    else:
        form = SignUpForm()
        # print(form)
        return render(request, 'signin.html', {'form': form})


def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

def user_list(request):
    if request.user.authen_user.admin:
        admin = Authen_User.objects.filter(admin=True)
        all_user = User.objects.filter(is_active=True).exclude(pk__in=admin) 
        # all_user = Userทั้งหมดที่ไม่ใช่adminและยังไม่ถูกแบน
        context={'all_user':all_user}
        return render(request, 'user_list.html',context=context)
    else:
        return redirect('home')

def ban_use(request, user_id):
    if request.user.authen_user.admin:
        admin = Authen_User.objects.get(user_id=request.user.id).getAdmin() 
        print(admin.user)
    if request.method == "POST":
        user = get_object_or_404(User, pk=user_id)
        print(user)
        remark = request.POST.get("remark")
        print(remark)
        user.authen_user.ban(admin=admin, remark=remark)
        user.is_active = False
        user.save()
    return redirect('user_list')


@login_required(login_url='login')
def main(request):
    return render(request, 'homepage.html')

@login_required(login_url='login')
def profile(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(createBy__user=user)
    # print(posts)
    context={
        'posts': posts,
        'form': PostForm()}
    return render(request, 'profile.html',context=context)