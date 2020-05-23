# Captain's Log

A simple personal script that uses Spotipy to maintain a song-a-day playlist.

## What it does

1. Requests up to 50 tracks played within the last day
2. Randomly selects one track  
3. Checks if a playlist called "Captain's Log" exists. If not, creates one
4. Adds the selected song to the playlist

## If you want to use it

Install [Spotipy](https://github.com/plamere/spotipy):

`pip install spotipy`

Create a new client ID using the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

### Locally

Add your Spotify client ID, client secret, and redirect URI to `captainslog.py` (for local use only):

```
token = util.prompt_for_user_token(username, scope, client_id='', client_secret='', redirect_uri='')
```

Or save them as environment variables:

```
export SPOTIPY_CLIENT_ID=''
export SPOTIPY_CLIENT_SECRET=''
export SPOTIPY_REDIRECT_URI=''
```

Run the script:

```
python3 captainslog.py <spotify-username>
```

The first time it runs, you will be asked to paste the URL you are redirected to. Then, `.cache-<spotify-username>` will be created in the directory to hold authentication and refresh tokens.

After the first run, execute manually or use a cron job to schedule.

### Heroku

Create `Procfile` and add it to the directory:

```
worker python captainslog.py <spotify-username>
```

Run the script locally to create `.cache-<spotify-username>`.

Commit `Procfile`, `.cache-<spotify-username>`, `requirements.txt`, and `captainslog.py` and push to Heroku.

Add your Spotify client ID, client secret, and redirect URI as config variables.

Use the Heroku scheduler add-on to schedule the script as desired.
