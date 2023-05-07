import screeninfo
from agents import *
import tkinter as tk
import PIL
from PIL import ImageTk, Image


def set_topmost():
    screen.attributes("-topmost", True)
    screen.after(100, set_topmost)


monitor = screeninfo.get_monitors()[0]

if monitor.width == 1920:
    screen = tk.Tk()

    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()

    x = (screen_width - 280) // 2
    y = (screen_height - 190) // 2

    screen.geometry(f"280x190+{x}+{y}")
    screen.title("Instalock like PRO")
    screen.eval('tk::PlaceWindow %s center' % screen.winfo_toplevel())
    screen.resizable(False, False)

    #screen.configure(bg='blue')


    #open_icon = Image.open("img/val_icon3.png")
    # new_size = (32, 32)
    # image_icon = open_icon.resize(new_size)
    # icon = ImageTk.PhotoImage(open_icon)



    open_reyna = Image.open("img/reyna.png")
    new_size = (80, 80)
    image_reyna = open_reyna.resize(new_size)
    img_reyna = ImageTk.PhotoImage(image_reyna)


    open_jett = Image.open("img/jett.png")
    new_size = (80, 80)
    image_jett = open_jett.resize(new_size)
    img_jett = ImageTk.PhotoImage(image_jett)

    open_phoenix = Image.open("img/phoenix.png")
    new_size = (80, 80)
    image_phoenix = open_phoenix.resize(new_size)
    img_phoenix = ImageTk.PhotoImage(image_phoenix)

    open_neon = Image.open("img/neon.png")
    new_size = (80, 80)
    image_neon = open_neon.resize(new_size)
    img_neon = ImageTk.PhotoImage(image_neon)

    open_raze = Image.open("img/raze.png")
    new_size = (80, 80)
    image_raze = open_raze.resize(new_size)
    img_raze = ImageTk.PhotoImage(image_raze)

    open_yoru = Image.open("img/yoru.png")
    new_size = (80, 80)
    image_yoru = open_yoru.resize(new_size)
    img_yoru = ImageTk.PhotoImage(image_yoru)

    # gif = Image.open('img/bg1.gif')
    # gif_set = ImageTk.PhotoImage(gif)

    screen.rowconfigure(0, minsize=2)
    screen.rowconfigure(1, minsize=2)
    screen.rowconfigure(2, minsize=2)


    button = tk.Button(screen, image=img_reyna, width=80, height=80, command=reyna_full)
    button.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    button = tk.Button(screen, image=img_jett, width=80, height=80, command=jett_full)
    button.grid(row=2, column=0, sticky="n", padx=0, pady=0)
    button = tk.Button(screen, image=img_neon, width=80, height=80, command=neon_full)
    button.grid(row=1, column=1, sticky="w", padx=0, pady=0)
    button = tk.Button(screen, image=img_phoenix, width=80, height=80, command=phoenix_full)
    button.grid(row=2, column=1, sticky="w", padx=0, pady=0)
    button = tk.Button(screen, image=img_raze, width=80, height=80, command=raze_full)
    button.grid(row=1, column=2, sticky="w", padx=5, pady=0)
    button = tk.Button(screen, image=img_yoru, width=80, height=80, command=yoru_full)
    button.grid(row=2, column=2, sticky="w", padx=5, pady=0)

    screen.after(100, set_topmost)
    screen.mainloop()

# elif monitor.width == 1680:
#
else:
    print("damn")

