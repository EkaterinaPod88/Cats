from tkinter import *
from PIL import Image, ImageTk#
import requests
from io import BytesIO#позволяет с вводом и  выводом инфы, а вторая с байтами

window = Tk()
window.title("Cats!")
window.geometry("600x180")

label = Label()
label.pack()

url = "https://cataas.com/cat"
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()

