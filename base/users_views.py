from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import User 
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.http import Http404


@login_required(login_url='/login/?next')
def user_list(request):
	users = User.objects.filter()
	return render(request,'users.html', {'users': users})

@login_required(login_url='/login/?next')
def user_detail(request,id):
	user_id = get_object_or_404(User,pk=id)
	return render(request,'user_detail.html', {'user_id': user_id})
