# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from accounts.forms import SignUpForm
from accounts.models import UserProfile


@csrf_exempt
def Signup(request):
    if request.method == 'POST':
        form  = SignUpForm(request.POST)
        if form.is_valid():
            new_data = request.POST.copy()
            form.save(new_data)
            return HttpResponseRedirect('accounts/thanks')
    else:
        form = SignUpForm
    return render_to_response('accounts/signup.html',{'form':form})

def MyLogout(request):
    state = "You successfully Logged Out"
    if request.user.is_authenticated():
        logout(request)
        return render_to_response('accounts/login.html',{'state':state})

    state = "You are not Logged In"
    return render_to_response('accounts/login.html',{'state':state})


def thanks(request):
    return render_to_response('thanks.hrml')



@csrf_exempt
def MyLogin(request):

    state = "Please login below"
    username = password = ""
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "" or password=="":
            state = "Username and Password cannot be blank"
            return render_to_response('accounts/login.html',{'state':state,'username':username})
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state="You are successfully logged in"
                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST['next'])

                return HttpResponseRedirect('/')
            else:
                state = "Your account is not active please activate it from the email link"
        else:
            state = "Your username or password is incorrect"

    return render_to_response('accounts/login.html',{'state':state,'username':username,'next':request.GET.get('next')},RequestContext(request))