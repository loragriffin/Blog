from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# view handles the http request and returns a response


def post_home(request):

    return HttpResponse("<h1>Hello</h1")
