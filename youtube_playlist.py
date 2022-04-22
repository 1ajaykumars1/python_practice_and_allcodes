from pytube import *
url = input(" inter url here : ")
playlist_name = input(" put playlist name")
Playlist = Playlist(url)

print(" number of videos : %s " % len(Playlist . video_urls))
for video in Playlist.videos:
    video.streams.get_highest_resolution().download(playlist_name)
    print("download completed")
