# Create your views here.
import cgi
import json
import urllib
from urlparse import parse_qsl
import urlparse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.utils.simplejson import JSONDecoder
from blankpage import twitter_request_tokens,twitter_access_tokens,twitter_request,fb_access_token
from models import TwitterAccount,FacebookAccount



def Accounts(request):
    try:
        twitter = TwitterAccount.objects.get(user=request.user)
    except TwitterAccount.DoesNotExist:
        twitter = None

    try:
        facebook = FacebookAccount.objects.get(user=request.user)
    except FacebookAccount.DoesNotExist:
        facebook = None

    return render_to_response('linked/accounts.html',{'twitter':twitter,'facebook':facebook})


@login_required
def TwitterConnect(request):
    if request.session.get('request_key') and request.session.get('request_secret'):
        request_key = request.session.get('request_key')
        request_secret = request.session.get('request_secret')
    else:
        request_token = twitter_request_tokens(request)
        request_key = request_token['oauth_token']
        request_secret = request_token['oauth_token_secret']
        
    return HttpResponseRedirect('https://api.twitter.com/oauth/authorize?oauth_token='+request_key+'&oauth_token_secret='+request_secret)


@login_required
def Twitter(request):
    if request.session.get('oauth_token') and request.session.get('oauth_token_secret'):
        content = twitter_request('https://api.twitter.com/1/statuses/home_timeline.json','GET',request.session['oauth_token'],request.session['oauth_token_secret'])
        timeline = JSONDecoder().decode(content)
        return render_to_response('linked/twitter.html',{'timeline':timeline})
    else:
        try:
            twitter = TwitterAccount.objects.get(user = request.user,type=1)
            request.session['oauth_token']=twitter.key
            request.session['oauth_token_secret']=twitter.secret
            content = twitter_request('https://api.twitter.com/1/statuses/home_timeline.json','GET',twitter.key,twitter.secret)
            timeline = JSONDecoder().decode(content)
            return render_to_response('linked/twitter.html',{'timeline':timeline})
        except TwitterAccount.DoesNotExist:
            return HttpResponseRedirect('/linked/')


def TwitterCallBack(request):
    if request.method=='GET':
        oauth_token =  request.GET.get('oauth_token')
        oauth_secret = request.session.get('request_secret')
        verifier = request.GET.get('oauth_verifier')
        access_token = twitter_access_tokens(oauth_token,oauth_secret,request,verifier)
        request.session['oauth_token']= access_token['oauth_token']
        request.session['oauth_token_secret'] = access_token['oauth_token_secret']
        return HttpResponseRedirect('/linked/twitter/')
    else:
        return HttpResponseRedirect('/error/')


def FacebookCallback(request):
    if request.method == 'GET':
        if request.GET.get('error'):
            return HttpResponse('Something goes Wrong'+request.GET.get('error'))

        if request.GET.get('code'):
            request.session['fb_code'] = request.GET.get('code')
            token = fb_access_token(request.GET.get('code'))
            access = dict(cgi.parse_qsl(token))
            try:
                fbaccount = FacebookAccount.objects.get(user = request.user)
                fbaccount.access_token = access['access_token']
                fbaccount.save()
            except FacebookAccount.DoesNotExist:
                fbaccount = FacebookAccount()
                fbaccount.user = request.user
                fbaccount.access_token = access['access_token']
                fbaccount.save()

        return HttpResponseRedirect('/linked/facebook/')

@login_required
def FacebookConnect(request):
    APP_ID = 130555633720380

    FACEBOOK_CALLBACK = 'http%3A%2F%2Fblankpage.outlets.pk%2Flinked%2Ffacebook%2Fcallback%2F'
    url ='https://www.facebook.com/dialog/oauth?client_id='+str(APP_ID)+'&redirect_uri='+FACEBOOK_CALLBACK+'&scope=email,read_stream,offline_access'
    return HttpResponseRedirect(url)

@login_required
def FaceBook(request):
    try:
        fbaccount = FacebookAccount.objects.get(user = request.user)
        content = urllib.urlopen('https://graph.facebook.com/me/?access_token='+fbaccount.access_token).read()
        fbprofile = JSONDecoder().decode(content)
        return render_to_response('linked/facebook.html',{'fbprofile':fbprofile})
    except FacebookAccount.DoesNotExist:
        return HttpResponseRedirect('/linked/')
