# Demonstration of a minimal app with a GUI implemented using Tkinter library
from tkinter import *
from tkinter.messagebox import showinfo

class ControlBlock:    # shared variables
    def __init__(self):
        self.canvas = None
        self.fillColour = "green"  # text colour for free list
        self.title="GUI demo"
        # version number
        self.verStr = "1.0"
        # licence information
        self.licenceStr = \
            "GNU General Public License\n\n" \
            + "This program is free software; you can redistribute it and/or modify it under the terms of the " \
            + "GNU General Public License as published by the Free Software Foundation; " \
            + "either version 2 of the License, or (at your option) any later version.\n\n" \
            + "This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; " \
            + "without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  " \
            + "See the GNU General Public License for more details.\n\n" \
            + "You should have received a copy of the GNU General Public License along with this program; if not, " \
            + "write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA."


global cb  # controlBlock


def popupShowinfo():
    showinfo("About " + cb.title, "Version: " + cb.verStr
             + " March 2022\n\nAuthor: <author name>\n\n"
             + cb.licenceStr)

def main():
    global cb
    cb = ControlBlock()
    # root configuration
    root = Tk()
    root.title(cb.title)
    # https://stackoverflow.com/questions/30965033/python-tkinter-application-fit-on-screen
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry('%dx%d+0+0' % (width, height))
    root.resizable(True, True)

    # Frame
    # frame = Frame(root, bd=2, relief=SUNKEN)
    frame = Frame(root)

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # menus
    menubar = Menu(root)
    # File
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    # About
    menubar.add_command(label="About", command=popupShowinfo)

    root.config(menu=menubar)

    visibleWidth = 1200; visibleHeight = 700
    
    # create a canvas for drawing on

    cb.canvas = Canvas(frame, bd=0, width=visibleWidth, height=visibleHeight)

    cb.canvas.grid(row=0, column=0, sticky=N + S + E + W)     

    frame.pack()
    
    cb.canvas.create_rectangle( (200,200,400,400), tag = "rectangle",width = 1, fill = cb.fillColour)

    root.mainloop()


# end main()

if __name__ == "__main__":
    main()