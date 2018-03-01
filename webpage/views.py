# Django
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Forms
from .forms import ContactForm

# Email
from django.core.mail import send_mail

# Others
import numpy as np

def index(request):
	if request.method == "GET":
		form = ContactForm()
		context = {"form": form}
		return render(request, "webpage/index.html", context)
	else:
		return HttpResponse("Not allowed")

def contact(request):
	form = ContactForm()
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			# Get the data from the form
			form_data = form.__dict__["cleaned_data"]
			# Extract the data
			name = form_data["name"]
			email = form_data["email"]
			phone = form_data["phone"]
			message = form_data["message"]
			print(name, email, phone, message)
			# Send mail
			send_mail(
			    "LABOMATIC",
			    ";".join([name, email, phone, message]),
			    "labomaticAlpha@gmail.com",
			    ["labomaticAlpha@gmail.com"],
			    fail_silently=False,
			)
			# Return a response
			return HttpResponseRedirect("/thanks")
	else:
		pass
	context = {"form": form}
	return render(request, "webpage/index.html", context)

def thanks(request):
	if request.method == "POST":
		return HttpResponseRedirect("/")
	return render(request, "webpage/thanks.html")

