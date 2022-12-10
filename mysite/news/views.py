from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

from .models import News

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': "Список новостей"
    }
    return render(request, 'news/index.html', context)

