from pytube import YouTube

link = input("Write or paste video link : ")
x = YouTube(link)

videos = x.streams.all()
a=0
for i in videos:
    print(a,"--->", i)
    a+=1

Quality = int(1)

video = videos[Quality-1]
y = input("Enter the path : ")
video.download(y)

print("Video download successfully")