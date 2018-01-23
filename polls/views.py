from django.shortcuts import render
from django.http import HttpResponse
from polls.models import BookInfo, HeroInfo
# Create your views here.


def index(request):
    # return HttpResponse("Welcome to Django!")
    context = {'title': BookInfo.objects.get(id=1).title, 'hero': HeroInfo.objects.get(book=BookInfo.objects.get(id=1)).name}
    return render(request, template_name='polls/index.html', context=context)


def booklist(request):
    return render(request, template_name='polls/booklist.html')
