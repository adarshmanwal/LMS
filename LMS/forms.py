from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your forms here.

class NewUserForm(UserCreationForm):
    print(" in the NewUser form ")

    def validate_email(value):
        if User.objects.filter(email = value).exists():
            raise ValidationError((f"{value} is taken."),params = {'value':value})
            
    email = forms.EmailField(required=True,validators = [validate_email])
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
