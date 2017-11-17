# from django.shortcuts import render
from django.http import HttpResponse


def feed(request):
    return HttpResponse('Hello, world. You are at the feed index.')
