from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from user.models import User, Authen_User, BanUser, NormalUser
from user.forms import SignUpForm, ChangePassForm
from post.form import PostForm
from post.models import Post
from comment.models import Comment
from django.http.response import HttpResponse
from django.contrib.auth.models import Group
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
            context['form'] = SignUpForm()
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

@login_required(login_url='login')
def changePassword(request):
    if request.method == 'POST':
        form = ChangePassForm(request.POST)
        if form.is_valid():
            new_pass = form.cleaned_data.get('newpassword')
            request.user.set_password(new_pass)
            request.user.save()
            update_session_auth_hash(request, request.user) #save new password and keep user stay logged in
            return redirect('home')
    else:
        form = ChangePassForm()
    return render(request, 'changePassword.html', {'form':form})


@login_required(login_url='login')
@permission_required('user.view_authen_user', raise_exception=True)
def user_list(request):
    if request.user.authen_user.admin:
        admin = Authen_User.objects.filter(admin=True)
        all_user = User.objects.filter(is_active=True).exclude(pk__in=admin) 
        # all_user = Userทั้งหมดที่ไม่ใช่adminและยังไม่ถูกแบน
        context={'all_user':all_user}
        return render(request, 'user_list.html',context=context)
    else:
        return redirect('home')

@login_required(login_url='login')
@permission_required('user.view_authen_user', raise_exception=True)
def ban_list(request):
    if request.user.authen_user.admin:
        admin = Authen_User.objects.filter(admin=True)
        all_ban_user = BanUser.objects.all()
        context={'all_ban_user':all_ban_user}
        return render(request, 'ban_list.html',context=context)
    else:
        return redirect('home')

@login_required(login_url='login')
@permission_required('user.add_banuser', raise_exception=True)
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
@permission_required('user.view_profile', raise_exception=True)
def profile(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(createBy__user=user)
    # print(posts)
    context={
        'posts': posts,
        'form': PostForm()}
    return render(request, 'profile.html',context=context)

def score(request, user_id):
    norm = NormalUser.objects.get(pk=user_id)
    user = User.objects.get(pk=user_id)
    print(norm.user, '(score : ', norm.score, ')')
    norm.score += 1
    norm.save()
    # ให้ 20 ไว้ก่อนอิอิ
    if norm.score >= 20 and norm.user.has_perm('post.view_all_post') == False:
        my_group = Group.objects.get(name='Special') 
        my_group.user_set.add(user)
    return HttpResponse(status=201)