from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def login(request):
    return HttpResponseRedirect(reverse('login'))
