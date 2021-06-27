from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm, BlogPostForms, BlogPostForms2


def home(request):
    return render(request, 'authenticate/home.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been login')
            return redirect('home')
        else:
            messages.success(request, 'Error,Try again')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Loged out")
    return redirect('login')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been login')
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'authenticate/register.html', context)


def edit_profile_user(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'You have Edited Your Profile')
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)


def change_password_user(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'You have Edited Your Password')
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)


def blog_post(request):
    if request.method == 'POST':
        form = BlogPostForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # update_session_auth_hash(request, form.user)
            # messages.success(request, 'Post Save')
            print('protik sani data has been save')
            return redirect('home')
        else:
            print('form not valid')
    else:
        form = BlogPostForms()
    return render(request, 'authenticate/blog_post.html', {'form': form})

# def blog_post(request):
#     if request.method == 'POST':
#         form = BlogPostForms2(request.POST)
#         if form.is_valid():
#             form.save()
#             # update_session_auth_hash(request, form.user)
#             # messages.success(request, 'Post Save')
#             print('protik sani data has been save')
#             return redirect('home')
#         else:
#             print('form not valid')
#     else:
#         form = BlogPostForms2()
#     return render(request, 'authenticate/blog_post.html', {'form': form})
