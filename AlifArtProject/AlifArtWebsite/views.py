from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery


# Create your views here.

def index(response):
    return render(response, 'templates/AlifArtWebsite/index.html', {})

def about_us(response):
    return render(response, 'templates/AlifArtWebsite/about_us.html', {})

def gallery(response):
    images = Gallery.objects.all()
    return render(response, 'templates/AlifArtWebsite/gallery.html', {'images': images})

def contact_us(response):
    return render(response, 'templates/AlifArtWebsite/contact_us.html', {})