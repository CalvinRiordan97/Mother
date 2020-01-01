from tkinter import *


def close(event):
    sys.exit()  # if you want to exit the entire thing


def file_write():
    """f = open("texts\\"+command[1].lower(), "w")
    f.write("This is a test file")
    f.close()"""


def pop_up(event):
    top = Toplevel()
    top.overrideredirect(True)  # Remove border
    top.configure(background='black')
    top.geometry("500x500+500+300")

    l = Label(top, text="Input", fg="green", bg="black", font=('System', 18, "bold"))
    l.pack()

    entryFrame = Frame(top, width=454, height=20)
    entryFrame.pack()

    box = Entry(top, fg="green", bg="black", font=('System', 18, "bold"),
                borderwidth=5, highlightbackground="green", highlightcolor="green", highlightthickness=2)

    box.grid(row=1, column=0, sticky="W")


def read_input(event):
    """First you must check if a command was sent such as mk.
    If there isn't such a command then it must be something in the text folder.
    If that's not the case then return an error message"""

    command = textbox.get().lower().split()

    # Create new text files (Logs, bio, etc.)
    if command[0] == "mk":
        pop_up(None)

    elif textbox.get() == "xenomorph":
        response.config(text="Xenomorph x121, commonly refereed to as simply the xenomorph\n"
                             "And know colloquially as the alien, is a highly aggressive endoparasitoid\n"
                             "extraterrestrial species.".upper(), anchor=W)
    else:
        f = open("texts\\" + command[0].lower(), "r")
        response.config(text=f.read())
        f.close()

    """if textbox.get() == "xenomorph":
        response.config(text="Xenomorph x121, commonly refereed to as simply the xenomorph\n"
                             "And know colloquially as the alien, is a highly aggressive endoparasitoid\n"
                             "extraterrestrial species.".upper())
    elif textbox.get() == "uh oh":
        response.config(text="Uh oh... stinky! Poop! Hahahahahaha! Poopies! \n"
                             "Funny poopies a-lalalala-ha ha! Funny poop! Poop funny... \n"
                             "wee! Haha, yay for poopy! Good poopy! \n"
                             "Poopy funny hahaha-ha haha poo poo poo poo poo poo poop funny, yay!\n"
                             "Fun fun poop, hee hee hee. Poop-poopy, yay! Poop make me happy, happy hap-ay ahahahahahaha..."
                             "Uh oh! I think I made a poopy! Pooping pants,\n"
                             "no diapah, that’s funny! Haha-hahahahahaha. Oopsie...\n"
                             "poopy underwear now! snickering We want poopies... \n"
                             "we want poopies! Hahahahahahahahahahahaha... hahahahahaha,\n"
                             "POO-OO-oo- dry coughing poop!")
    else:
        response.config(text="ERROR: INVALID COMMAND")"""
    textbox.delete(0, 'end')


window = Tk()
window.configure(background='black')
window.geometry("500x500")

window.attributes("-fullscreen", True)
window.title("MOTHER")

frame1 = Frame(window, highlightbackground="green", highlightcolor="green", bg="green", highlightthickness=1, width=100,
               height=100, bd=0)
frame1.pack(anchor=W, fill=X)

title_label = Label(frame1, text="MU//TH//ER", fg="green", bg="black", font=('System', 18, "bold"))
title_label.pack()

label = Label(window, text="ENTER QUERY", fg="green", bg="black", font=('System', 18, "bold"))
label.pack(anchor=W)

textbox = Entry(window, fg="green", bg="black", font=('System', 18, "bold"),
                borderwidth=.5, highlightbackground="green", highlightcolor="green", highlightthickness=1)

textbox.bind('<Return>', read_input)
textbox.pack(anchor=W)

response = Label(window, fg="green", bg="black", font=('system', 18, "bold"), anchor="w")
response.pack(anchor=W)

window.bind('<Escape>', close)


window.mainloop()



