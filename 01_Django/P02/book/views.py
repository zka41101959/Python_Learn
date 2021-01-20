import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        pass


class ReceiveView(View):
    def get(self, request):
        data = json.loads(request.body.dacode())
        username = data.get('username')
        password = data.get('password')
        return JsonResponse({'data': {'username': username}})
