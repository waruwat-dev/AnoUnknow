from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
# from django.contrib.auth.forms import UserCreationForm
class ChangePassForm(forms.Form):
    newpassword=forms.CharField(widget=forms.PasswordInput())
    confirm=forms.CharField(widget=forms.PasswordInput()) 
    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        newpassword = cleaned_data.get("newpassword")
        confirm = cleaned_data.get("confirm")
        if newpassword != confirm:
            self.add_error(None, "New Password do not match.")

class SignUpForm(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'text': forms.Textarea(attrs= {
                'class': 'form-control card-text',
                'rows': '3'
            })
        }
        labels = {
            'username': 'Username',
            'email' : 'Email',
            'password' : 'Password',
        }
    def clean(self):
        user_use = User.objects.all()
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        usernameList = [i.username for i in user_use]
        emailList = [ i.email for i in user_use if i.email != '']
        if username in usernameList:
            self.add_error(None, "Username : '%s' is already use." %username)
        if email in emailList:
            self.add_error(None, "Email : '%s' is already use." %email)
        if password != confirm_password:
            self.add_error(None, "Password do not match.")
    def save(self, commit=True):
        instance = super(SignUpForm, self).save(commit=False)
        instance.set_password(self.cleaned_data['password'])
        if commit:
            instance.save()
        return instance
        

        