'''
Created on Sep 9, 2011

@author: Abrar
'''
from piston.handler import BaseHandler,AnonymousBaseHandler
from accounts.models import *
from piston.utils import rc, require_mime, require_extended


class ProfileHandler(BaseHandler):
    allowed_methods = ('GET','POST','PUT')
    model = UserProfile
    fields = ('screen_name', 'about','web','gender', ('user', ('id', 'first_name')))


    def read(self, request, id=None):
        """
        Return the Profile of the User using application
        """
        base = UserProfile.objects
        if id:
            return base.get(pk=id)
        else:
            return base.filter(user=request.user)



class WorkHandler(BaseHandler):
    allowed_methods = ('GET','POST','PUT','DELETE')
    model = Work
    fields = ('id','employer_name', 'designation','employer_country','employment_year', ('user', ('username', 'first_name')))
    def read(self, request,id=None):
        """
        Return all work records if option id is not provided
        If parameter id set than return the work record of the given id
        """
        base = Work.objects
        if id:
            return base.get(pk=id,user=request.user)
        else:
            return base.filter(user=request.user)

    def update(self, request, id):
        """
        Update the work record of the provided id
        """
        work = Work.objects.get(pk=id)
        if not request.user == work.user:
            return rc.FORBIDDEN

        work.employer_country = request.PUT.get('employer_country')
        work.employer_name = request.PUT.get('employer_name')
        work.designation = request.PUT.get('designation')
        work.employment_year = request.PUT.get('employment_year')
        work.save()
        return work


    def delete(self, request,id):
        """
        Delete the work record of the provided id
        """
        work = Work.objects.get(pk=id)
        if not request.user == work.user:
            return rc.FORBIDDEN

        work.delete()
        return rc.DELETED

    def create(self,request):
        """
        This is the method create new entry of work to requested user
        """
        attrs = self.flatten_dict(request.POST)
        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            work = Work(
                employer_name=attrs['employer_name'],
                designation = attrs['designation'],
                employer_country = attrs['employer_country'],
                employment_year = attrs['employment_year'],
                user = request.user,
                )
    
            work.save()

        return work



class EducationHandler(BaseHandler):
    allowed_methods = ('GET','POST','DELETE','PUT')
    model = Education
    @classmethod
    def content_length(cls, education):
        return len(education.content)


    def read(self, request, id=None):
        """
        This is the method to GET Education detail  from api
        """
        base= Education.objects
        if id:
            return base.get(pk=id)
        else:
            return base.filter(user=request.user)


    def create(self, request):
        attrs = self.flatten_dict(request.POST)
        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            education = Education(
                user = request.user,
                institute_name = attrs['institute_name'],
                institute_country = attrs['institute_country'],
                institute_year = attrs['institute_year'],
                education_level = attrs['education_level']
            )

            education.save()
            return education

class ContactHandler(BaseHandler):
    allowed_methods = ('GET','PUT',)
    fields = ('address','city','state','country',('user',('username','first_name')))
    model = Contact

    def read(self, request):
        """
        This is the method to GET work history from api
        """
        base = Contact.objects
        return base.get(user=request.user)