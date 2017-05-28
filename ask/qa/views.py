from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')
