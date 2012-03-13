# Create your views here.
from encodings.utf_8_sig import encode
import urllib
import urlparse
import json
import ast
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.simplejson import JSONEncoder,JSONDecoder
import oauth2 as oauth
from dashboard.blankpage import Application
from dashboard.forms import WorkForm, EducationForm
from dashboard.models import Client
def Home(request):
    if request.session.get('oauth_token'):
        return HttpResponseRedirect('/dashboard/')
    else:
        return render_to_response('home.html')


def Connect(request):
    """
    This instantiate pplication and get request token for the application that are used to authorize and get
     access tokens
    """
    APP_KEY='UqYr97gbEuL4XEytuj'
    APP_SECRET='ArqTPgS4GmcDhhjw9SAv9ab4QsY9dY7j'
    CALL_BACK = 'http://dashboard.outlets.pk/dashboard/callback/'
    REQUEST_TOKEN_URL = "http://blankpage.outlets.pk/oauth/request_token/"
    AUTHENTICATE_URL = "http://blankpage.outlets.pk/oauth/authorize/"
    ACCESS_TOKEN_URL =  "http://blankpage.outlets.pk/oauth/access_token/"

    consumer = oauth.Consumer(APP_KEY,APP_SECRET)
    client = oauth.Client(consumer)

    resp, content = client.request(REQUEST_TOKEN_URL,'GET',parameters={'oauth_callback':CALL_BACK})
    #resp_status = dict(urlparse.parse_qsl(resp))
    if resp['status']!='200':
        return HttpResponseRedirect('/client/error/')

    request_token = dict(urlparse.parse_qsl(content))
    clt = Client()
    clt.oauth_token = request_token['oauth_token']
    clt.oauth_token_secret = request_token['oauth_token_secret']
    clt.verified = 0
    clt.save()
    return HttpResponseRedirect(AUTHENTICATE_URL+'?oauth_token='+request_token['oauth_token']+'&oauth_token_secret='+request_token['oauth_token_secret'])


def CallBack(request):
    """
    After call it is going to check the response is access token or the request token and verifier
    """
    APP_KEY='UqYr97gbEuL4XEytuj'
    APP_SECRET='ArqTPgS4GmcDhhjw9SAv9ab4QsY9dY7j'
    CALL_BACK = 'http://dashboard.outlets.pk/dashboard/callback/'
    REQUEST_TOKEN_URL = "http://blankpage.outlets.pk/oauth/request_token/"
    AUTHENTICATE_URL = "http://blankpage.outlets.pk/oauth/authorize/"
    ACCESS_TOKEN_URL =  "http://blankpage.outlets.pk/oauth/access_token/"

    if request.GET.get('oauth_token_secret'):
        token = request.GET.get('oauth_token')
        secret = request.GET.get('oauth_token_secret')
        request.session['oauth_token'] = token
        request.session['oauth_token_secret'] = secret
        token = oauth.Token(token,secret)
        consumer = oauth.Consumer(APP_KEY,APP_SECRET)
        client = oauth.Client(consumer,token)
        resp, content = client.request('http://blankpage.outlets.pk/api/work/','GET')
        return  HttpResponseRedirect('/authorize/')

    else:
        oauth_verifier = request.GET.get('oauth_verifier')
        oauth_token= request.GET.get('oauth_token')
        clt = Client.objects.get(oauth_token=oauth_token)
        oauth_token_secret  = clt.oauth_token_secret
        token = oauth.Token(oauth_token,oauth_token_secret)
        token.set_verifier(oauth_verifier)
        consumer = oauth.Consumer(APP_KEY,APP_SECRET)
        client = oauth.Client(consumer,token)
        resp, content = client.request(ACCESS_TOKEN_URL,'POST')
        if resp['status']!='200':
            return HttpResponseRedirect('/client/error/')

        access_token = dict(urlparse.parse_qsl(content))
        request.session['oauth_token'] = access_token['oauth_token']
        request.session['oauth_token_secret'] = access_token['oauth_token_secret']
        token = oauth.Token(access_token['oauth_token'],access_token['oauth_token_secret'])
        client = oauth.Client(consumer,token)
        resp, content = client.request('http://blankpage.outlets.pk/api/work/','GET')
        
        

    return render_to_response('application.html',{'content':content},context_instance = RequestContext(request))


def Authorized(request):
    return render_to_response('dashboard.html',context_instance=RequestContext(request))

def GetData(request):
    APP_KEY='UqYr97gbEuL4XEytuj'
    APP_SECRET='ArqTPgS4GmcDhhjw9SAv9ab4QsY9dY7j'
    base = 'http://blankpage.outlets.pk/api/'+request.GET.get('fetch')+'/'
    consumer = oauth.Consumer(APP_KEY,APP_SECRET)
    token = oauth.Token(request.session.get('oauth_token'),request.session.get('oauth_token_secret'))
    client = oauth.Client(consumer,token)
    resp, content = client.request(base,'GET')
    return HttpResponse(content,mimetype="application/json")
    #return render_to_response('application.html',{'content':content},context_instance=RequestContext(request))


def PostData(request):
    APP_KEY='UqYr97gbEuL4XEytuj'
    APP_SECRET='ArqTPgS4GmcDhhjw9SAv9ab4QsY9dY7j'
    base = 'http://blankpage.outlets.pk/api/'+request.GET.get('post')+'/'
    consumer = oauth.Consumer(APP_KEY,APP_SECRET)
    token = oauth.Token(request.session.get('oauth_token'),request.session.get('oauth_token_secret'))
    client = oauth.Client(consumer,token)
    resp, content = client.request(base,'POST')


def AddWork(request):

    if request.method =='POST':
        jsondata = json.dumps(request.POST)
        jsondata = ast.literal_eval(jsondata)
        app = Application()
        work = app.build_request("http://blankpage.outlets.pk/api/work/","POST",request,data=urllib.urlencode(jsondata))

#        APP_KEY='6kyABmV5hZ4mfYS6LE'
#        APP_SECRET='pnMSWFHx4hkxpm6HuyWNurFxmwJEQ5jZ'
#        #base = 'http://blankpage.outlets.pk/api/'+request.GET.get('post')+'/'
#        consumer = oauth.Consumer(APP_KEY,APP_SECRET)
#        token = oauth.Token(request.session.get('oauth_token'),request.session.get('oauth_token_secret'))
#        client = oauth.Client(consumer,token)
#        resp, content = client.request("http://blankpage.outlets.pk/api/work/","POST",body = urllib.urlencode(jsondata))
#        print content
        messages.success(request,'Work info Added successfuly ')
        return HttpResponseRedirect('/dashboard/work/')
    else:
        form = WorkForm()
    return render_to_response('addwork.html',{'form':form},context_instance=RequestContext(request))

def DeleteWork(request,id):
    app = Application()
    work = app.build_request('http://blankpage.outlets.pk/api/work/'+id+'/','DELETE',request)
    messages.success(request,'work deleted successfuly')
    return HttpResponseRedirect('/dashboard/work/')

def UpdateWork(request,id):
    if request.method=='POST':
        jsondata = json.dumps(request.POST)
        jsondata = ast.literal_eval(jsondata)
        app = Application()
        work = app.build_request("http://blankpage.outlets.pk/api/work/"+id+"/","PUT",request,data=urllib.urlencode(jsondata))
        if work is None:
            return HttpResponse('Not completed')
        messages.success(request,'Work updated successfully')
        return HttpResponseRedirect('/dashboard/work/')
    else:
        app = Application()
        work = app.build_request('http://blankpage.outlets.pk/api/work/'+id+'/','GET',request)
        work = JSONDecoder().decode(work)
        form  = WorkForm(work)
        return render_to_response('updatework.html',{'form':form})
def Work(request):
    client = Application()
    work = client.build_request('http://blankpage.outlets.pk/api/work/','GET',request)
    works  = JSONDecoder().decode(work)
    return  render_to_response('works.html',{'works':works},context_instance=RequestContext(request))

def Dashboard(request):
    return render_to_response('dashboard.html')

def Profile(request):
    client = Application()
    profile = client.build_request('http://blankpage.outlets.pk/api/profile/','GET',request)
    profiles  = JSONDecoder().decode(profile)
    return  render_to_response('profile.html',{'profiles':profiles})

def Education(request):
    client = Application()
    education = client.build_request('http://blankpage.outlets.pk/api/education/','GET',request)
    educations  = JSONDecoder().decode(education)
    return render_to_response('education.html',{'educations':educations})

def AddEducation(request):
    if request.method=='POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            jsondata = json.dumps(request.POST)
            jsondata = ast.literal_eval(jsondata)
            app = Application()
            education = app.build_request('http://blankpage.outlets.pk/api/education/','POST',request,data=urllib.urlencode(jsondata))
            if education is None:
                return HttpResponse('Education Error')
            messages.success(request,'work deleted successfuly')
        return HttpResponseRedirect('/dashboard/education/')

    else:
        form = EducationForm
        return render_to_response('addeducation.html',{'form':form},context_instance=RequestContext(request))

