import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "60b8432f04c24b7d8d015545425a0664"
CLIENT_SECRET = "fff32429da3a4f4681da4d51a7dbe9ec"

date = input("Which year would you like to travel to?\nType the date in the format of YYYY-MM-DD.\n")
response = requests.get(url=f"{BILLBOARD_URL}{date}/")

soup = BeautifulSoup(response.text, "html.parser")
song_name = soup.select("li ul li h3")
song_name_list = [song.getText().strip() for song in song_name]
print(song_name_list)

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = spotify.current_user()["id"]
# song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_name_list:
    try:
        result = spotify.search(q=f"track:{song} year:{year}", type="track")
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_id = spotify.user_playlist_create(user=user_id, public=False, name=f"{date} Billboard 100")["id"]
playlist = spotify.user_playlist_add_tracks(playlist_id=playlist_id, tracks=song_uris, user=user_id)
print(f"\nNew playlist {date} Billboard 100 has been successfully created.")
