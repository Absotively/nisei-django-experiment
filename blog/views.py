from django.shortcuts import render
from django.http import HttpResponse
from django.utils import translation
import datetime

from .models import Post, PostTranslation

def index(request):
  return HttpResponse("Blog!")

def detail(request, slug):
  pt = PostTranslation.objects.filter(language=translation.get_language()).select_related('post').filter(post__publication_date__lte=datetime.datetime.now()).filter(post__publish=True).get(slug=slug)
  return HttpResponse(pt.title)
