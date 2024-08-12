from tkinter import *
from PIL import Image, ImageTk#
import requests
from io import BytesIO#позволяет с вводом и  выводом инфы, а вторая с байтами


def loade_image():
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

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

