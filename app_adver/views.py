from django.shortcuts import render
from django.http import HttpResponse
from .models import Adver


def index(request):
    adver = Adver.objects.all()
    context = {'adver': adver}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')