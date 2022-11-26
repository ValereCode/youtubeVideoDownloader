"""Project Youtube downloader!!!"""

from pytube import YouTube
from pytube import Playlist

p_url = "https://www.youtube.com/watch?v=PAvn_jBNVNE&list=PLFMhxiCgmMR9Pu0v-VjNdEaRLcoUqHLFT"  # url d'un playlist



def progression(stream, chunk, byte_remaining):
    """
    Fonction qui définit la progression d'un téléchargement
    :param stream: le stream en cours
    :param chunk:
    :param byte_remaining: le nombre de byte restant
    :return:
    """
    fichierTelecharger = stream.filesize - byte_remaining
    pourcentage = fichierTelecharger * 100 / stream.filesize
    print("Progression = ", int(pourcentage), "%")


youtube_playlist = Playlist(p_url)
print(youtube_playlist.video_urls)
i = 1
for url in youtube_playlist.video_urls:
    youtube_video = YouTube(url)  # La video correspondant à l'url précédent
    youtube_video.register_on_progress_callback(progression)
    stream = youtube_video.streams.get_highest_resolution()
    print("Téléchargement", i, "...")
    i += 1
    stream.download()

print("OK")
