import os

def download(link):
    command = f'youtube-dl --geo-bypass --limit-rate 1000M --download-archive ".\\archive.txt" --ffmpeg-location "..\\ffmpeg.exe" --extract-audio --audio-format mp3 --audio-quality 0 -f "bestaudio" --embed-thumbnail --add-metadata -o "%(title)s.%(ext)s" "{link}"'
    
    os.system(command)