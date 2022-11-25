"""Project Youtube downloader!!!"""

from pytube import YouTube
from pytube import Playlist

p_url = "https://www.youtube.com/watch?v=jevdND1NBVs&list=PLepmdz3mDsCpOcLtmn3r8UKfsjGSeDmma"  # url d'un playlist


def progression(stream, chunk, byte_remaining):
    fichierTelecharger = stream.filesize - byte_remaining
    pourcentage = fichierTelecharger * 100 / stream.filesize
    print("Progression = ", int(pourcentage), "%")


youtube_playlist = Playlist(p_url)

for url in youtube_playlist.video_urls:
    youtube_video = YouTube(url)  # La video correspondant à l'url précédent
    youtube_video.register_on_progress_callback(progression)
    stream = youtube_video.streams.get_highest_resolution()
    print("Téléchargement...")
    stream.download()
print("OK")
