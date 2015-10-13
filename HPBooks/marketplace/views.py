from django.shortcuts import render
from .forms import UserRegistrationForm, BookForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms

def listings(request):
	render(request, 'listings.html')

def entry(request):
	if request.method == 'POST':
		form = BookForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commmit=False)
			if not instance.subject:
				instance.subject = ''
			if not instance.title:
				instance.title = ''
			instance.save()
			return HttpResponseRedirect('list/')
		context = {
			"form": form,
		}
		return render(request, 'home.html', context)


