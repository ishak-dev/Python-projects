from pytube import YouTube
SAVE_PATH = "C:\Users\Isko\Desktop\Github projects"
link = input("link")

try:
    yt = YouTube(link)
except:
    print("Conection Error")

mp4 = yt.filter("mp4")
video= yt.get(mp4[-1].extension,mp4[-1].resolution)
try:
    video.download(SAVE_PATH)
except:
    print("some error")
print("Task complete")