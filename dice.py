from tkinter  import *
from PIL import Image,ImageTk
import random
root = Tk()
root.title("Dice rolling game")
root.geometry("400x400")

mylabel = Label(root,text="Welcome to the game", fg="lightgreen", bg="green", font="helvetica 16 bold").place(x=130,y=29)
# list of images
dice= ['die1.png', 'die2.png', 'die3.png','die4.png', 'die5.png', 'die6.png']

DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

mylabel2 = Label(root,image=DiceImage)
mylabel2.image =DiceImage
mylabel2.place(x=100,y=80)

def roll():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    mylabel2.config(image=DiceImage)
    # keep a reference
    mylabel2.image=DiceImage

btn=Button(root,text="Roll the Dice", width=10,fg="blue",command=roll).place(x=150,y=350)

root.mainloop()
