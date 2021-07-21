from django.forms import EmailField
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CreateUserForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True,
        help_text=_("Required."),)


    class meta:
        model = User
        fields = ['username','email','password1','password2']

    # def clean(self):
    #    email = self.cleaned_data.get('email')
    #    if User.objects.filter(email=email).exists():
    #         raise ValidationError("This email  is already exists")
    #    return self.cleaned_data

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("This email  is already exists")
            
       username = self.cleaned_data.get('username')
       if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already exists")
       return self.cleaned_data

    


    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


   
