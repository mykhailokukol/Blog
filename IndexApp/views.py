from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout, login, authenticate
from django.views.generic import View, UpdateView, ListView
from django.views.generic.edit import DeleteView
from IndexApp import models, forms
from .utils import ObjectDetailMixin


class IndexView(ListView):
    paginate_by = 10
    model = models.Post
    query_set = models.Post.objects.all().order_by('-created')
    context_object_name = 'posts'
    template_name = 'IndexApp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = models.PostComment.objects.all()
        context['AddCommentForm'] = forms.AddCommentForm()
        context['PostForm'] = forms.PostForm()
        return context

    # Не актуально. Изменил предка вида с View на ListView в пользу пагинации.
    # def get(self, request):

        # posts = models.Post.objects.all().order_by('-created')
        # comments = models.PostComment.objects.all()
        #
        # AddCommentForm = forms.AddCommentForm()
        # PostForm = forms.PostForm()
        #
        # return render(request, 'IndexApp/index.html', {
        #     'posts': posts,
        #     'comments': comments,
        #     'AddCommentForm': AddCommentForm,
        #     'PostForm': PostForm,
        # })

    def post(self, request):
        PostForm = forms.PostForm(request.POST)
        if PostForm.is_valid():
            new_post = PostForm.save(commit=False)
            new_post.author = request.user
            new_post = PostForm.save()
            return redirect('/')
        else:
            return redirect('/') # очень важный кусок кода

class PostEditView(View):

    def get(self, request, pk):
        current_post = get_object_or_404(models.Post, pk=pk)

        return render(request, 'IndexApp/post_edit.html', {
            'PostForm': forms.PostForm(),
            'post': current_post,
        })

    def post(self, request, pk):
        current_post = get_object_or_404(models.Post, pk=pk)
        form = forms.PostForm(request.POST, instance=current_post)
        if form.is_valid():
            updated_post = form.save()
            return redirect('/')
        else:
            return redirect('/')

        return render(request, 'IndexApp/post_edit.html', {
            'PostForm': form,
            'post': current_post,
        })


class PostDeleteView(DeleteView):
    model = models.Post
    success_url = '/'


class ProfileView(ObjectDetailMixin, View):
    model = models.Profile
    template = 'IndexApp/profile.html'


def add_comment(request, pk):
    if request.method == 'POST':
        AddCommentForm = forms.AddCommentForm(request.POST)
        if AddCommentForm.is_valid():
            text = AddCommentForm.cleaned_data['text']
            post = get_object_or_404(
                models.Post, id=request.POST.get('post_comment_id'))
            comment = models.PostComment.objects.create(
                user=request.user, text=text, post=post)
    else:
        AddCommentForm = forms.AddCommentForm()
    return redirect('/')


@login_required
def like_post(request, pk):
    post = get_object_or_404(models.Post, id=request.POST.get('post_id'))
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('/')


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
