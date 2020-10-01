import sys
import time
import random

import spotipy
import spotipy.util as util

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-read-recently-played playlist-modify-public playlist-read-private playlist-read-collaborative'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    timestamp = int(round(time.time() * 1000)) - 86400000

    results = sp.current_user_recently_played(limit=50, after=timestamp)

    if len(results) == 0:
        sys.exit()

    uri_list = []
    for i, item in enumerate(results['items']):
        uri_list.append(item['track']['uri'])

    max_index = len(uri_list)
    chosentrack = uri_list[random.randint(0,max_index)]
    chosentrack_id = []
    chosentrack_id.append(chosentrack.replace("spotify:track:", ""))

    user_profile = sp.me()
    user_id = user_profile['id']

    playlists = sp.user_playlists(user_id, limit=50, offset=0)
    captains_log = ''
    playlist_names = []
    for i, item in enumerate(playlists['items']):
        playlist_names.append(item['name'])
        if item['name'] == '''Captain's Log''':
            captains_log = item['id']
    if '''Captain's Log''' not in playlist_names:
            new_playlist = sp.user_playlist_create(user_id, '''Captain's Log''', True, '')
            captains_log = new_playlist['id']

    sp.user_playlist_add_tracks(username, captains_log, chosentrack_id)

else:
    print("Can't get token for", username)
