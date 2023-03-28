from tkinter import *
from PIL import Image, ImageTk


def clicked(event):
    button_number = (int(event.y / 60) * 9) + (1 + int(event.x / 60))
    print(f'You clicked button number {button_number}.')


root = Tk()
drawCanv = Canvas(width=632, height=482, bd=0)
drawCanv.bind('<Button-1>', clicked)

button_number = 1
for y in range(2, 480, 60):
    for x in range(2, 480, 60):
        if (x % 120 == 2 and y % 120 == 2) or (x % 120 == 62 and y % 120 == 62):
            color = 'white'
        else:
            color = '#404040'

        rectangle = drawCanv.create_rectangle(x, y, x + 60, y + 60, fill=color,
                                              outline='black')
        button_number += 1
rectangle = drawCanv.create_rectangle(482, 0, 632, 482, fill='#505050',
                                              outline='black')
drawCanv.create_text (557, 241, text = 'CHESS', font=("Arial", 25))
drawCanv.pack()


bp=ImageTk.PhotoImage(file="Chess_pdt60.png")
wp=ImageTk.PhotoImage(file="Chess_plt60.png")

# Add the image in the canvas
bpawns = []
wpawns = []
for var in range(8):
    bpawns.append(drawCanv.create_image(2 + 60*var + 30, 62 + 30, image=bp, anchor="center"))
    wpawns.append(drawCanv.create_image(2 + 60*var + 30, 362 + 30, image=wp, anchor="center"))

# drawCanv.delete(wpawns[4])

root.minsize(632, 482)
mainloop()