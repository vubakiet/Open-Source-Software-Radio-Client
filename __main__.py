# !/usr/bin/python3

import tkinter
from tkinter import messagebox

# Create an instance of tkinter frame
win = tkinter.Tk()

# Set the geometry
win.geometry("800x500")
win.configure(bg='blue')

win.eval('tk::PlaceWindow . center')

paned_window = tkinter.PanedWindow(win, orient="horizontal")
paned_window.pack(fill="both", expand=True)

fr_left = tkinter.PanedWindow(paned_window, width=450, height=500)
fr_left.pack(fill="both", expand=True)
fr_right = tkinter.PanedWindow(paned_window, width=350, height=500)
fr_right.pack(fill="both", expand=True)

paned_window.add(fr_left)
paned_window.add(fr_right)

paned_window1 = tkinter.PanedWindow(fr_left, orient="vertical", bg='#2f2234')
pnDisk = tkinter.PanedWindow(
    paned_window1, width=450, height=350, bg='#2f2234')
pnAction = tkinter.PanedWindow(
    paned_window1, width=450, height=150, bg='#2f2234')

# paned_window1.add(pnDisk)
# paned_window1.add(pnAction)
fr_left.add(paned_window1)

# img = tkinter.PhotoImage("")
# lb = tkinter.Label(pnDisk, image=img)
# lb.pack()
# img = tkinter.PhotoImage(file=r"C:\\Users\\ASUS\\Downloads\\sesumaru.jpg")
btnNext = tkinter.Button(pnAction, text="Next")
# btnPre = tkinter.Label(pnAction, text="Previous", image=img)
btnPlay = tkinter.Button(pnAction, text="Pause", width=20, height=20)
# pnAction.add(btnPre)
pnAction.add(btnPlay)
pnAction.add(btnNext)

# img1 = img.subsample(2, 2)
# tkinter.Label(win, image=img1).grid(row=0, column=2,
#                                     columnspan=2, rowspan=2, padx=5, pady=5)
# label = tkinter.Label(win, text="DISK")
# btnNext = tkinter.Button(win, text="next", command=handleButton)
# label.grid(row=0, column=0, sticky='w')
# btnPre.grid(row=1, column=0, sticky='w', pady=2)
# btnPlay.grid(row=1, column=1, sticky='w', pady=2)
# btnNext.grid(row=1, column=2, sticky='w', pady=2)

win.mainloop()
