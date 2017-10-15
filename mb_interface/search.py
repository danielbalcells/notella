import musicbrainzngs as mbn
from .models import Song

# Set MB user agent data for API identification
mbn.set_useragent('Notella','dev')

# Queries MB API for a given song title, returns a list of results
def search_song_by_title(song_query, limit=20):
    try:
        # Oversearch, prune later to remove duplicates
        query_results = mbn.search_recordings(query=song_query, limit=2*limit)
        result_list = query_results['recording-list']
        song_list = []
        song_string_list = []
        for result in result_list:
            title = result['title']
            artist = result['artist-credit-phrase']
            mbid = result['id']
            album = result['release-list'][0]['title']
            song = Song(title=title,
                        artist=artist,
                        mbid=mbid,
                        album=album)
            if str(song) not in song_string_list:
                song_string_list.append(str(song))
                song.save()
                song_list.append(song)
        return song_list[:limit]
    except (mbn.ResponseError):
        return []
