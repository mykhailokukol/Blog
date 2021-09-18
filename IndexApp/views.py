from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout, login, authenticate
from django.views.generic import View
from datetime import date
from IndexApp import models, forms
from .utils import ObjectDetailMixin


class IndexView(View):

    def get(self, request):

        posts = models.Post.objects.all().order_by('-created')
        comments = models.PostComment.objects.all()

        AddCommentForm = forms.AddCommentForm()
        CreatePostForm = forms.CreatePostForm()

        return render(request, 'IndexApp/index.html', {
            'posts': posts,
            'comments': comments,
            'AddCommentForm': AddCommentForm,
            'CreatePostForm': CreatePostForm,
        })

    def post(self, request):
        CreatePostForm = forms.CreatePostForm(request.POST)
        if CreatePostForm.is_valid():
            # TODO: Проверка на уникальность поста
            new_post = CreatePostForm.save(commit=False)
            new_post.author = request.user
            new_post = CreatePostForm.save()
            return redirect('/')


def add_comment(request, pk):
    if request.method == 'POST':
        AddCommentForm = forms.AddCommentForm(request.POST)
        if AddCommentForm.is_valid():
            text = AddCommentForm.cleaned_data.get('text')
            post = get_object_or_404(
                models.Post, id=request.POST.get('post_comment_id'))
            comment = models.PostComment.objects.create(
                user=request.user, text=text, post=post)
            # comment.save()
    else:
        AddCommentForm = forms.AddCommentForm()
    return redirect('/')


def like_post(request, pk):
    post = get_object_or_404(models.Post, id=request.POST.get('post_id'))
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('/')


class ProfileView(ObjectDetailMixin, View):
    model = models.Profile
    template = 'IndexApp/profile.html'
    # TODO: BELOW.
    # Формула расчета возраста
    # age = date.today().year - profile.birth_date.year - ((date.today().month, date.today().day) < (profile.birth_date.month, profile.birth_date.day))


@login_required
def profile_edit(request):
    if request.method == 'POST':
        UserEditForm = forms.EditUserForm(request.POST, instance=request.user)
        ProfileEditForm = forms.EditProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if UserEditForm.is_valid() and ProfileEditForm.is_valid():
            user_form = UserEditForm.save()
            custom_form = ProfileEditForm.save(commit=False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('/profile/')
    else:
        UserEditForm = forms.EditUserForm(instance=request.user)
        ProfileEditForm = forms.EditProfileForm(instance=request.user.profile)

    return render(request, 'IndexApp/profile_edit.html', {
        'UserEditForm': UserEditForm,
        'ProfileEditForm': ProfileEditForm,
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    logout(request)

    username = password = ''
    if request.method == 'POST':
        LoginForm = forms.LoginForm(request.POST)
        if LoginForm.is_valid():
            username = request.POST['username']
            raw_password = request.POST['password']
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
    else:
        LoginForm = forms.LoginForm()

    return render(request, 'IndexApp/login.html', {
        'LoginForm': LoginForm,
    })


def signup_view(request):
    logout(request)

    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/profile/%s' % (user.profile.pk))
    else:
        form = forms.SignupForm()

    return render(request, 'IndexApp/signup.html', {
        'SignupForm': form,
    })


def about_us(request):

    misha = models.Profile.objects.get(
        user=models.User.objects.get(username='admin'))

    return render(request, 'IndexApp/about_us.html', {
        'user': request.user,
        'misha': misha,
    })
