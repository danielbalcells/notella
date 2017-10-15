import musicbrainzngs as mbn
import numpy as np

from .models import Song, Link

# Set MB user agent data for API identification
mbn.set_useragent('Notella','dev')

# Top-level function. Returns songs connected to the given Song
def recommend_from_song(from_song, num_links=15):
    # Get artists credited to this song, include links
    from_mbid = from_song.mbid
    query_results = mbn.browse_artists(
                        recording=from_mbid,
                        includes = ['artist-rels']
                        )
    # For each credited artist, find connected songs and make links
    links = []
    for from_artist in query_results['artist-list']:
        links.append(get_links_from_connected_artist(from_song, from_artist,
            max_links=num_links))
    if len(links) > num_links:
        links = np.random.choice(links, num_links, replace=False)
    return links

# Finds a few songs for each artist connected to from_artist.
# Makes a link for each song
def get_links_from_connected_artist(from_song, artist_connections,
                                    songs_per_artist=5,
                                    max_links=1000):
    from_artist = artist_connections['name']
    links = []
    # Iterate connected artists, find songs for each one
    # Randomize order of artists, stop when we have enough links
    randomized_connections = np.random.permutation(
        artist_connections['artist-relation-list'])
    for connected_artist in randomized_connections:
        conn_type = connected_artist['type']
        if 'direction' in connected_artist.keys():
            conn_direction = connected_artist['direction']
        else:
            conn_direction = 'forward'
        to_artist = connected_artist['artist']['name']
        to_artist_id = connected_artist['artist']['id']
        to_recordings = mbn.browse_recordings(artist=to_artist_id,
            limit=songs_per_artist)
        if to_recordings['recording-list']:
            links += make_links(from_song, from_artist,
                to_artist, to_recordings['recording-list'],
                conn_type, conn_direction)
        if len(links) >= max_links:
            break
    return links

# Creates Link objects for a given set of parameters
def make_links(from_song, from_artist, to_artist, to_recordings,
                conn_type, conn_direction):
    # Iterate destination recordings.
    # For each one, make a Song object and a Link with the specified parameters
    links = []
    for to_recording in to_recordings:
        # Check if the song is already in the DB
        to_song_id = to_recording['id']
        existing_song = Song.objects.filter(pk=to_song_id)
        if existing_song:
            to_song = existing_song[0]
        else:
            to_song = Song(title=to_recording['title'],
                        artist=to_artist,
                        mbid=to_recording['id']
                        )
            to_song.save()
        if conn_direction == 'forward':
            link_phrase = from_artist + ' - ' + conn_type + ' - ' + to_artist
        else:
            link_phrase = to_artist + ' - ' + conn_type + ' - ' + from_artist

        link = Link( from_song=from_song,
                     to_song=to_song,
                     link_phrase=link_phrase)
        links.append(link)
    return links
        
