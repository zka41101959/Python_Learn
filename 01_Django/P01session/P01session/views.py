from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class setSession(View):
    def get(self,request):
        request.session['name']='itcast'
        return HttpResponse('set success')