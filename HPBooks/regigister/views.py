from django.shortcuts import render
from django.shortcuts import render
from .forms import UserForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms


def register(request):
	form = UserForm(request.POST or None)
	registered = False
	context = {
	"form": form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		context = {
		"title": "Thank you"
		}
		registered = True

	return render(
		request,
		'register.html',
		context
		)