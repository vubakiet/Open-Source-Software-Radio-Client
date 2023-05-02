# from tkinter import *
# from urllib.request import urlopen
# from PIL import ImageTk, Image
# from io import BytesIO

# # Tạo cửa sổ chính
# root = Tk()

# url = "https://scontent.fsgn2-7.fna.fbcdn.net/v/t1.6435-9/110317078_108873884247194_8632694263271216467_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=CYkmKjjJ3K8AX8vLrAb&_nc_ht=scontent.fsgn2-7.fna&oh=00_AfBiwiyFddEmezj0zF8kj61iY3RTbmJluODDF6b12I6c5A&oe=6476F918"
# image_bytes = urlopen(url).read()

# image = Image.open(BytesIO(image_bytes))
# img_width, img_height = image.size

# # Tính đường kính của hình tròn
# diameter = min(img_width, img_height)

# # Crop hình ảnh thành hình tròn
# img = image.crop((0, 0, diameter, diameter))
# img = img.resize((300, 300))

# photo = ImageTk.PhotoImage(img)

# label = Label(root, image=photo)
# label.pack()

# root.mainloop()

# from playsound import playsound

# # for playing note.wav file
# playsound('/path/note.wav')
# print('playing sound using  playsound')


# import vlc
# import os
# os.add_dll_directory(os.getcwd())
# p = vlc.MediaPlayer("http://localhost:5000/play-music/1683005873.149153.mp3")
# p.play()

# import vlc
# from time import sleep
# sleep(5)
# Instance = vlc.Instance('--fullscreen')
# player = Instance.media_player_new()
# Media = Instance.media_new(
#     'http://localhost:5000/play-music/1683005873.149153.mp3')
# Media.get_mrl()
# player.set_media(Media)
# player.play()

# import pygame
# from pydub import AudioSegment
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load('sample.mp3')
# audSeg = AudioSegment.from_mp3("sample.mp3")
# audSeg.export("hello.wav", format="wav")


# pygame.event.wait()
