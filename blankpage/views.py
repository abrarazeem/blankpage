from accounts.forms import SignUpForm

__author__ = 'Abrar'

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


def Index(request):
    if request.user.is_authenticated():
        return render_to_response('dashboard/dashboard.html',{'user':request.user})
    else:
        form = SignUpForm
        return render_to_response('home.html',{'form':form})