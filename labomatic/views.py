# Django
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Forms
from .forms import ContactForm

# Email
from django.core.mail import send_mail

def index(request):
	if request.method == "GET":
		form = ContactForm()
		context = {"form": form}
		return render(request, "labomatic/index.html", context)
	else:
		return HttpResponse("Not allowed")

def contact(request):
	if request.method == "POST":
		# Fill form with incoming data
		form = ContactForm(request.POST)
		if form.is_valid():
			# Retrieve data from form
			form_data = form.__dict__["cleaned_data"]
			# Extract the data
			name = form_data["name"]
			email = form_data["email"]
			phone = form_data["phone"]
			message = form_data["message"]
			print("Form data: {} {} {} [}".format(name, email, phone, message))
			# Send mail
			send_mail("LABOMATIC",
								";".join([name, email, phone, message]),
								"labomaticAlpha@gmail.com",
								["labomaticAlpha@gmail.com"],
								fail_silently=False,)
		# Return a response
		return HttpResponseRedirect("/thanks")
	# Load form into webpage
	form = ContactForm()
	context = {"form": form}
	return render(request, "labomatic/index.html", context)	

def thanks(request):
	if request.method == "POST":
		return HttpResponseRedirect("/")
	return render(request, "labomatic/thanks.html")

