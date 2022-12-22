from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
  except:
    print("There has been an error in downloading your youtube video, check your url and try again")
  print("This download has completed! Follow me on github @mosespace")

link = input("Put your youtube link here!! URL: ")
Download(link)