from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Q, Count

from .forms import UserCreationFormCustom
from .models import Follow


@login_required()
def home(request):
    return render(request, 'home.html')


@login_required()
def my_profile(request):
    follow_counts = Follow.objects.aggregate(
        following=Count('pk', filter=Q(from_user=request.user)),
        followers=Count('pk', filter=Q(to_user=request.user)),
    )

    # TODO: other user profiles will probably share same template
    return render(
        request,
        'my_profile.html',
        context={
            'follow_counts': follow_counts,
        },
    )


class SignupView(CreateView):
    model = User
    form_class = UserCreationFormCustom
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['request'] = self.request
        return form_kwargs




# home page should have feed of photos of people you follow

# M2M for follower relations probably

# for the search, one text entry field; Q objects to do or on all the User fields

# create middleware to require login on all pages (except signup/login/logout)

# reference trwibc (on flash drive) for file uploads
# Photos should be its own model (keys to User)

# add static assets
    # include collecstatic command in README

# write tests
    # note how to run them in README




# treubig/treubig2/...
# christian.treubig@gmail.com
# casepeer

# from django.contrib.auth.models import User
# from insta_clone.models import Follow