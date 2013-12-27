from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.

def index(request):
	if not request.user.is_authenticated():
		return redirect('/login/?next=%s' % request.path)
	else:
		return render(request, 'index.html')

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return redirect('/')
    else:
        # Show an error page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def logout_view(request):
    logout(request)
    return redirect('/')