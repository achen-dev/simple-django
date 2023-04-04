from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Post

class NumberForm(forms.Form):

    number = forms.IntegerField(
        max_value=100,
        min_value=0,
        help_text="Please enter an integer",
        required=True
    )


class MLForm(forms.Form):
    image = forms.FileField(
        help_text="Please upload an image in .jpg format and is less than 5 Megabytes",
    )


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)


class BlogUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'status')


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'status')
