from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Adver
from .forms import AdverForm
from django.urls import reverse


def index(request):
    adver = Adver.objects.all()
    context = {'adver': adver}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')


def adver_post(request):
    if request.method == "POST":
        form = AdverForm(request.POST, request.FILES)
        if form.is_valid():
            adver = Adver(**form.cleaned_data)
            adver.user = request.user
            adver.save()
            url = reverse('main-page')
            return redirect(url)

    else:
        form = AdverForm()
        context = {'form': form}
        return render(request, 'advertisement-post.html', context)


