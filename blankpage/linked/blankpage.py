import re
import urlparse
from django.core.cache import params
from urllib2 import urlopen
from json import JSONDecoder
from django.http import HttpResponseRedirect, HttpResponse
from linked.models import TwitterAccount

__author__ = 'Abrar'
import oauth2,urllib



###twitter application keys and urls to get access token and user permissions###

ACCESS = "sJ8xgOH5wkmjstP07Z3oCA"
SECRET = "w8wrhM5xsxNuQkaQ4thtJerxNV0zamWKZnZ7b4tvs"
REQUEST_TOKEN_URL='https://api.twitter.com/oauth/request_token'
AUTHORIZE_ = 'https://api.twitter.com/oauth/authorize'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'

###Facebook application key and secret and urls get access tokens###
APP_ID = 130555633720380
APP_KEY = 'e2a1407764b735ab04f23217efa43588'
FACEBOOK_CALLBACK = 'http://blankpage.outlets.pk/linked/facebook/callback/'



###############################################################
# Twitter related functions
###############################################################
def twitter_request(url, method,oauth_token,oauth_token_secret):

    """
    Function used to make each signed reauest to the twitter 
    """
    consumer = oauth2.Consumer(key=ACCESS, secret=SECRET)
    token = oauth2.Token(oauth_token,oauth_token_secret)
    client = oauth2.Client(consumer,token)
    resp, content = client.request(url,method)
    return content


def twitter_request_tokens(request):
    consumer = oauth2.Consumer(ACCESS,SECRET)
    client = oauth2.Client(consumer)
    resp, content = client.request(REQUEST_TOKEN_URL,'GET')
    if resp['status']=='200':
        request_token = dict(urlparse.parse_qsl(content))
        request.session['request_key'] = request_token['oauth_token']
        request.session['request_secret'] = request_token['oauth_token']
        return request_token
    else:
        return False



def twitter_access_tokens(oauth_token,oauth_token_secret,request,verifier):
    consumer = oauth2.Consumer(ACCESS,SECRET)
    token = oauth2.Token(oauth_token,oauth_token_secret)
    token.set_verifier(verifier)
    client = oauth2.Client(consumer,token)
    resp,content = client.request(ACCESS_TOKEN_URL,'GET')

    if resp['status'] == '200':
        access_token = dict(urlparse.parse_qsl(content))
        twitter = TwitterAccount()
        twitter.key = access_token['oauth_token']
        twitter.secret = access_token['oauth_token_secret']
        twitter.user = request.user
        twitter.type=1
        twitter.twitter_id = access_token['user_id']
        twitter.screen_name = access_token['screen_name']
        twitter.save()
        return access_token
    else:
        return HttpResponseRedirect('/linked/error/')

########################################################################
#Facebook relates function to get token and all the other stuff
########################################################################
def fb_access_token (code):
    content = urllib.urlopen('https://graph.facebook.com/oauth/access_token?client_id='+str(APP_ID)+'&redirect_uri=http%3A%2F%2Fblankpage.outlets.pk%2Flinked%2Ffacebook%2Fcallback%2F&client_secret='+APP_KEY+'&code='+code).read()
    return content