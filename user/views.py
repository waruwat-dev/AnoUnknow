from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from user.models import User


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


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
            context['error'] = "username or password is wrong"
            return render(request, 'signin.html', context)
    else:
        return render(request, 'signin.html')


def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')



# def ban_user(request, user_id):
#     if request.user.admin:
#         admin = request.user.getAdmin()
#     else:
#         redirect('home')
#     if request.method == "POST":
#         user = get_object_or_404(User, pk=user_id)
#         remark = request.POST.get("remark")
#         user.authen_user.ban(admin=admin, remark=remark)
#     return redirect('home')


@login_required(login_url='login')
def main(request):
    return render(request, 'homepage.html')
