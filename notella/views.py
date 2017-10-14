# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404

def index(request):
    return render(request, 'index.html')

def search(request):
    query = request.GET.get('query')
    return render(request, 'search.html', {'query': query})
