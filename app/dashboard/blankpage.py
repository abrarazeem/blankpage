
from django.core.cache import params
from django.http import HttpResponse
__author__ = 'Abrar'
import oauth2,urllib

class Application:

    def build_request(self,url, method,request,data=None):
        ACCESS = "UqYr97gbEuL4XEytuj"
        SECRET = "ArqTPgS4GmcDhhjw9SAv9ab4QsY9dY7j"
        consumer = oauth2.Consumer(key=ACCESS, secret=SECRET)
        token = oauth2.Token(request.session.get('oauth_token'),request.session.get('oauth_token_secret'))
        client = oauth2.Client(consumer,token)
        if data is None:
            resp , content = client.request(url,method)
            if resp['status']=='200':
                return content
            else:
                return None
        else:
            resp, content = client.request(url,method,body=data)
            if resp['status']=='200':
                return content
            else:
                return None