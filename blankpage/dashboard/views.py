from json.decoder import JSONDecoder
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from accounts.models import *
from dashboard.forms import *
from linked.blankpage import twitter_request
from linked.models import *

@login_required
def Profile(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():

            model =  UserProfile()
            model.user = request.user
            model.screen_name = form.cleaned_data['screen_name']
            model.about = form.cleaned_data['about']
            model.gender = form.cleaned_data['gender']
            model.web = form.cleaned_data['web']
            model.country = form.cleaned_data['country']
            model.save()
            return render_to_response('dashboard/profile.html',{'profile':model})
    try:
        profile = UserProfile.objects.get(user=request.user)
        return render_to_response('dashboard/profile.html',{'profile':profile})
    except UserProfile.DoesNotExist:
        profile = ProfileForm()
        return render_to_response('dashboard/profile_edit.html',{'profile':profile})
@login_required
def ProfileEdit(request):
    model =  UserProfile.objects.get(user=request.user)
    form = ProfileForm(instance=model)
    return render_to_response('dashboard/profile_edit.html',{'profile':form})

@login_required
@csrf_exempt
def AddWork(request):
    if request.method=='POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            m =  form.save(commit=False)
            m.user = request.user
            m.save()
            return HttpResponseRedirect('/dashboard/work/')
    form = WorkForm
    return  render_to_response('dashboard/addwork.html',{'form':form},context_instance=RequestContext(request))

@login_required
def Works(request):
    works = Work.objects.filter(user = request.user)
    return render_to_response('dashboard/works.html',{'works':works})

@login_required
def DeleteWork(request,work_id):
    work_id = int(work_id)
    work = Work.objects.get(pk=work_id)

@login_required
@csrf_exempt
def AddEducation(request):
    if request.method=='POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            m =  form.save(commit=False)
            m.user = request.user
            m.save()
            return HttpResponseRedirect('/dashboard/education/')
    form = EducationForm
    return  render_to_response('dashboard/addeducation.html',{'form':form})

@login_required
def Educations(request):
    educations = Education.objects.filter(user = request.user)
    return render_to_response('dashboard/education.html',{'educations':educations})


@login_required
@csrf_exempt
def AddEmail(request):
    if request.method=='POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            m =  form.save(commit=False)
            m.user = request.user
            m.status = 0
            m.save()
            return HttpResponseRedirect('/dashboard/email/')
    form = EmailForm
    return  render_to_response('dashboard/addemail.html',{'form':form})

@login_required
def Emails(request):
    emails = EmailAccount.objects.filter(user = request.user)
    return render_to_response('dashboard/emails.html',{'emails':emails})


@login_required
def Dashboard(request):
    return render_to_response('dashboard/dashboard.html',context_instance=RequestContext(request))
