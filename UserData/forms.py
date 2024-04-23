from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserSignupForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields=['username','password','gender','skill']
		def save(self, commit=True):
			user = super().save(commit=False)
			if commit:
				user.save()
			return user
