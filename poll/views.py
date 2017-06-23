from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache

def index(request):
    cache.set("foo", "bar", timeout=None)
    print(cache.get("foo"))
    return render(request, 'index.html')

def poll(request):
    return HttpResponse("A poll should appear here!")
