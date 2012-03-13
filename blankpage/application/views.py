# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from piston.models import Consumer
from application.forms import ApplicationForm
from django.db import connection, transaction

@login_required
@csrf_exempt
def add_app(request):
    if request.method == 'POST':
        form  = ApplicationForm(request.POST)
        if form.is_valid():
            new_data = request.POST.copy()
            form.save(new_data,request.user)
            return HttpResponseRedirect('/applications/')
    else:
        form = ApplicationForm
    return render_to_response('application/add_app.html',{'form':form})



def thanks(request):
    return render_to_response('application/thanks.hrml')

@login_required
def application(request,app_id):
    app_id  = int(app_id)
    application = Consumer.objects.filter(pk=app_id,user=request.user)
    return render_to_response('application/application.html',{'application':application})


@login_required
def applications(request):
    #applications = Consumer.objects.get(user=request.user)
    applications = Consumer.objects.filter(user=request.user)
    return render_to_response('application/applications.html',{'applications':applications})