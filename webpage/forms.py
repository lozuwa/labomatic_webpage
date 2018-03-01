# Django libraries
from django import forms 

# Contact form
class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Your name"}), label="Enter your name", max_length=20)
	email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Your email"}), label="Enter your email", max_length=30)
	phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Your phone"}), label="Enter your phone", max_length=20)
	message = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Please, leave us a message"}), label="Leave us a message", max_length=100)

