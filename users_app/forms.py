from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from culture_blog.models import Post
from .models import Post2


class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(help_text="<small>Enter Your First Name Here</small>", label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ""
        self.fields['username'].help_text = "<small> Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>"
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ""

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ""
        self.fields['password2'].help_text = "<small>Enter the same password as before, for verification.</small>"


class BlogPostForms(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ('title', 'text', 'image', 'img_description', 'create_date', 'published_date')
        fields = ('__all__')

        # title = models.CharField(max_length=200)
        # text = models.TextField()
        # image = models.ImageField(null=False, blank=False)
        # img_description = models.CharField(max_length=200, blank=True)
        # create_date = models.DateTimeField(default=timezone.now())
        # published_date = models.DateTimeField(blank=True, null=True)


class BlogPostForms2(forms.ModelForm):
    class Meta:
        model = Post2
        # fields = ('title', 'text', 'image', 'img_description', 'create_date', 'published_date')
        fields = ('__all__')