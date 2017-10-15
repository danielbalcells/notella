# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from mb_interface.search import search_song_by_title
from mb_interface.recommend import recommend_from_song
from mb_interface.models import Song, Link

# Create your views here.
from django.http import HttpResponse, Http404

def index(request):
    return render(request, 'index.html')

def search(request):
    query = request.GET.get('query')
    song_list = search_song_by_title(query)
    context = { 'query': query, 'song_list': song_list}
    return render(request, 'search.html', context)

def song(request, mbid):
    song = get_object_or_404(Song, pk=mbid)
    links = recommend_from_song(song)
    context = {'song': song, 'links': links}
    return render(request, 'song.html', context)
