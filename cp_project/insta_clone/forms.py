from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import Photo, Comment


class UserCreationFormCustom(UserCreationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            auth_user = authenticate(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password1']
            )
            login(self.request, auth_user)

        return user


class PhotoUploadForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    comment = forms.CharField()

    class Meta:
        model = Photo
        fields = ('image', 'comment')

    def save(self, commit=True):
        photo = super().save(commit=False)
        photo.user = self.request.user
        comment_text = self.cleaned_data['comment']

        if commit:
            photo.save()
            Comment.objects.create(
                text=comment_text,
                poster=self.request.user,
                photo=photo,
            )

        return photo
