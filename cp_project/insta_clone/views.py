from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.db.models import Q, Count

from .forms import UserCreationFormCustom, PhotoUploadForm
from .models import Follow, Photo


@login_required()
def home(request):
    return render(request, 'home.html')


@login_required()
def profile(request, profile_user_id):
    profile_user = User.objects.get(id=profile_user_id)

    follow_counts = Follow.objects.aggregate(
        following=Count('pk', filter=Q(from_user=profile_user)),
        followers=Count('pk', filter=Q(to_user=profile_user)),
    )

    try:
        Follow.objects.get(from_user=request.user, to_user=profile_user)
        request_user_follows_profile_user = True
    except Follow.DoesNotExist:
        request_user_follows_profile_user = False

    photos = Photo.objects.filter(user=profile_user).order_by('-created_at')

    return render(
        request,
        'profile.html',
        context={
            'profile_user': profile_user,
            'follow_counts': follow_counts,
            'request_user_follows_profile_user': request_user_follows_profile_user,
            'photos': photos,
        },
    )


@login_required()
def follow(request, profile_user_id):
    user_to_follow = User.objects.get(id=profile_user_id)
    Follow.objects.create(from_user=request.user, to_user=user_to_follow)

    return redirect('profile', profile_user_id=profile_user_id)


@login_required()
def unfollow(request, profile_user_id):
    follow = Follow.objects.get(from_user=request.user, to_user=profile_user_id)
    follow.delete()

    return redirect('profile', profile_user_id=profile_user_id)


@login_required()
def search_users(request):
    search_string = request.GET.get('search_string')

    users = User.objects.filter(
        Q(username__icontains=search_string) |
        Q(first_name__icontains=search_string) |
        Q(last_name__icontains=search_string)
    ).exclude(id=request.user.id)

    return render(
        request,
        'search_results.html',
        context={
            'users': users,
        },
    )


class SetRequestOnFormMixin:
    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['request'] = self.request
        return form_kwargs


class PhotoUploadView(LoginRequiredMixin, SetRequestOnFormMixin, CreateView):
    model = Photo
    form_class = PhotoUploadForm
    template_name = 'photo_upload.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'profile_user_id': self.request.user.id})


class SignupView(SetRequestOnFormMixin, CreateView):
    model = User
    form_class = UserCreationFormCustom
    template_name = 'signup.html'
    success_url = reverse_lazy('home')



# move signup.html to the templates/registration folder

# home page should have feed of photos of people you follow

# create middleware to require login on all pages (except signup/login/logout)

# reference trwibc (on flash drive) for file uploads
# Photos should be its own model (keys to User)

# add static assets
    # include collecstatic command in README
        # prob don't need this

# write tests
    # note how to run them in README




# treubig/treubig2/...
# christian.treubig@gmail.com
# casepeer

# from django.contrib.auth.models import User
# from insta_clone.models import Follow