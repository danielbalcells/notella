import musicbrainzngs as mbn
from .models import Song

# Set MB user agent data for API identification
mbn.set_useragent('Notella','dev')

# Queries MB API for a given song title, returns a list of results
def search_song_by_title(song_query, limit=10):
    query_results = mbn.search_recordings(query=song_query, limit=limit,
            status='official')
    result_list = query_results['recording-list']
    song_list = []
    for result in result_list:
        title = result['title']
        artist = result['artist-credit-phrase']
        mbid = result['id']
        album = result['release-list'][0]['title']
        song = Song(title=title,
                    artist=artist,
                    mbid=mbid,
                    album=album)
        song_list.append(song)
    return song_list
