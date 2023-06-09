from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from userprofile.models import Profile
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'slug', 'title', 'intro', 'body', 'image',)
        

    widgets = {
         'image': forms.ImageField(),
         'slug': forms.TextInput(attrs={
              'placeholder': 'type the tiele back in with no spaces between'
         })
    }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', )


class UserProfileForm(forms.ModelForm):
     class Meta:
          model = Profile
          fields = ('nickname', 'bio', 'image',)
          widgets = {
               'image': forms.ImageField()
          }
          


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', )
    
    def save(self, commit=True):
            user = super(SignupForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            
            if commit:
                user.save()
            return user
        