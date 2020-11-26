from tkinter import *
import pyautogui
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from tkinter import colorchooser
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.title("the notepad pro")
root.geometry("800x600+0+0")
text_area = Text(undo= True)
text_area.pack(fill=BOTH, expand=1)
#root.maxsize(height=800,width=600)
# Adding Scrollbar
Scroll = Scrollbar(text_area)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=text_area.yview)
text_area.config(yscrollcommand=Scroll.set)
main_menu = Menu()
root.config(menu=main_menu)
photo = PhotoImage(file="images3.png")
root.iconphoto(False,photo)
# adding the filemenu
file_menu = Menu(main_menu, fg="white", bg="black")
main_menu.add_cascade(label="FILE", menu=file_menu)
# adding the edit menu

edit_menu = Menu(main_menu, fg="white", bg="black", )
main_menu.add_cascade(label="EDIT", menu=edit_menu)
# adding the colortheme

color_theme = Menu(main_menu, fg="white", bg="black", )
main_menu.add_cascade(label="COLOR_THEME", menu=color_theme)
# adding the menu inside the filemenu
#function for new file

def newFile():
    global file
    root.title("untitle notepad")
    file = None
    text_area.delete(1.0,END)

#function for open
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, END)
        f = open(file, "r")
        text_area.insert(1.0, f.read())
        f.close()
#cut function
def cut():
    copy()
    text_area.delete("sel.first","sel.last")


#copy function
def copy():
    text_area.clipboard_clear()
    text_area.clipboard_append(text_area.selection_get())
# function for taking screenshot and save it to the file
def screenshot():
    screen_shot1 = pyautogui.screenshot()
    save_file = filedialog.asksaveasfilename(defaultextension = '.png')
    screen_shot1.save(save_file)
#paste function
def paste():
    text_area.insert(INSERT,text_area.clipboard_get())
#function for save only
def save():
    file = asksaveasfilename()

#save function
def saveFile():
    file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                             filetypes=[("All Files", "*.*"),
                                        ("Text Documents", "*.txt")])
    if file =="":
        file = None

    else:
        #Save as a new file
        f = open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()

        root.title(os.path.basename(file) + " - Notepad")
        print("File Saved")
def bold():
    bold_text = font.Font(text_area,text_area.cget("font"))
    bold_text.configure(weight="bold")
    text_area.tag_configure("bold",font=bold_text)
    current_tags = text_area.tag_names("sel.first")
    if "bold" in current_tags:
        text_area.tag_remove("bold","sel.first","sel.last")
    else:
        text_area.tag_add("bold","sel.first","sel.last")

def italics():
    italics_text = font.Font(text_area,text_area.cget("font"))
    italics_text.configure(slant="italic")
    text_area.tag_configure("italic",font=italics_text)
    current_tags = text_area.tag_names("sel.first")
    if "italic" in current_tags:
        text_area.tag_remove("italic","sel.first","sel.last")
    else:
        text_area.tag_add("italic","sel.first","sel.last")
def underlined1():
    underline1_text = font.Font(text_area,text_area.cget("font"))
    underline1_text.configure(underline= 1)
    text_area.tag_configure("underline",font=underline1_text)
    current_tags = text_area.tag_names("sel.first")
    if "underline" in current_tags:
        text_area.tag_remove("underline","sel.first","sel.last")
    else:
        text_area.tag_add("underline","sel.first","sel.last")
def color():
    color = colorchooser.askcolor()
    text_area.clipboard_append(color)
def dark_theme():
    main_color = "black"
    text_color = "white"
    root.config(bg=main_color)
    text_area.config(bg=main_color,fg=text_color)
def white1():
    main_color1 = "white"
    text_color1 = "black"
    root.config(bg=main_color1)
    text_area.config(bg=main_color1,fg=text_color1)
def light_green():
    main_color2 = "light green"
    text_color2 = "black"
    root.config(bg=main_color2)
    text_area.config(bg=main_color2,fg=text_color2)
def blue1():
    main_color3 = "light blue"
    text_color3 = "brown"
    root.config(bg=main_color3)
    text_area.config(bg=main_color3,fg=text_color3)
def pinktheme():
    main_color4="pink"
    text_color4 = "blue"
    root.config(bg=main_color4)
    text_area.config(bg=main_color4,fg=text_color4)
def orangetheme():
    main_color5 = "orange"
    text_color5 = "blue"
    root.config(bg=main_color5)
    text_area.config(bg=main_color5,fg=text_color5)
def purple_theme():
    main_color6 = "purple"
    text_color6 = "red"
    root.config(bg=main_color6)
    text_area.config(bg=main_color6,fg=text_color6)
def darkgreen_theme():
    main_color6 = "darkgreen"
    text_color6 = "red"
    root.config(bg=main_color6)
    text_area.config(bg=main_color6,fg=text_color6)
def indigo_theme():
    main_color7 = "indigo"
    text_color7 = "yellow"
    root.config(bg=main_color7)
    text_area.config(bg=main_color7,fg=text_color7)
def lime_color():
    main_color8 = "lime"
    text_color8 = "black"
    root.config(bg=main_color8)
    text_area.config(bg=main_color8,fg=text_color8)
def cyan_color():
    main_color9 = "cyan"
    text_color9 = "red"
    root.config(bg=main_color9)
    text_area.config(bg=main_color9,fg=text_color9)

file_menu.add_command(label="NEW ::->:->", font=("Aerial", 15, "bold"),command=newFile)
file_menu.add_separator()
file_menu.add_command(label="OPEN ::->:->", font=("Aerial", 15, "bold"),command=openFile)
file_menu.add_separator()
file_menu.add_command(label="SAVE ::->:->", font=("Aerial", 15, "bold"),command=saveFile)
file_menu.add_separator()
file_menu.add_command(label='SAVE AS ::->:->', font=("Aerial", 15, "bold"))
file_menu.add_separator()
file_menu.add_command(label="EXIT ::->:->", command=root.destroy, font=("Aerial", 15, "bold"))
frame = Frame(root)
frame.pack(side=BOTTOM)

# adding button
button1 = Button(frame, text="NEW", fg="white", bg="black", bd=15, font=("times", 15, "bold"),command=newFile)
button1.pack(side=LEFT)
button2 = Button(frame, text="OPEN", fg="white", bg="black", bd=15, font=("times", 15, "bold"),command=openFile)
button2.pack(side=LEFT)
button7 = Button(frame, text="COPY", fg="white", bg="black", bd=15, font=("times", 15, "bold"),command=copy)
button7.pack(side=LEFT)
button3 = Button(frame, text="SCREENSHOT", fg="white", bg="black", bd=15, font=("times", 15, "bold"),command=screenshot)
button3.pack(side=LEFT)
button4 = Button(frame, text="SAVE", fg="white", bg="black", bd=15, font=("times", 15, "bold"),command=save)
button4.pack(side=LEFT)
button8 = Button(frame, text="PASTE", fg="white", bg="black", bd=15, font=("times", 15, "bold"),command=paste)
button8.pack(side=LEFT)
button9 = Button(frame, text="DARK THEME", fg="white", bg="black", bd=15, font=("times", 15, "bold"),command=dark_theme)
button9.pack(side=LEFT)
button10 = Button(frame, text="BOLD", fg="white", bg="black", bd=15, font=("times", 15, "bold"),command=bold)
button10.pack(side=LEFT)
button11 = Button(frame, text="ITALICS", fg="white", bg="black", bd=15, font=("times", 15, "bold"),command=italics)
button11.pack(side=LEFT)
button12 = Button(frame, text="UNDERLINE", fg="white", bg="black", bd=15, font=("times", 15, "bold"),command=underlined1)
button12.pack(side=LEFT)
button5 = Button(frame, text="CLOSE ALL", fg="white", bg="black", bd=15, command=root.destroy,
                      font=("times", 15, "bold"))
button5.pack(side=RIGHT)

# adding the sub menu inside the color theme
color_theme.add_command(label="DARK:::->:::-> ", font=("Aerial", 15, "bold"),command=dark_theme)
color_theme.add_separator()
color_theme.add_command(label="WHITE::->:->", font=("Aerial", 15, "bold"),command=white1)
color_theme.add_separator()
color_theme.add_command(label="LIGHT_GREEN :->:->", font=("Aerial", 15, "bold"),command=light_green)
color_theme.add_separator()
color_theme.add_command(label="BLUE :::->::->", font=("Aerial", 15, "bold"),command=blue1)
color_theme.add_separator()
color_theme.add_command(label="PINK ::->::->",font=("Aerial", 15, "bold"),command=pinktheme)
color_theme.add_separator()
color_theme.add_command(label="ORANGE ::->:->",font=("Aerial", 15, "bold"),command=orangetheme)
color_theme.add_separator()
color_theme.add_command(label="PURPLE ::->:->",font=("Aerial", 15, "bold"),command=purple_theme)
color_theme.add_separator()
color_theme.add_command(label="DARK GREEN ::->:->",font=("Aerial", 15, "bold"),command=darkgreen_theme)
color_theme.add_separator()
color_theme.add_command(label="INDIGO ::->:->",font=("Aerial", 15, "bold"),command=indigo_theme)
color_theme.add_separator()
color_theme.add_command(label="LIME ::_>:_>",font=("Aerial", 15, "bold"),command=lime_color)
color_theme.add_separator()
color_theme.add_command(label="CYAN ::->:->",font=("Aerial", 15, "bold"),command=cyan_color)
# adding the menu inside  the edit menu

edit_menu.add_command(label="COPY ::->:->", font=("Aerial", 15, "bold"),command=copy)
edit_menu.add_separator()
edit_menu.add_command(label="PASTE ::->:->", font=("Aerial", 15, "bold"),command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="CUT ::->:->", font=("Aerial", 15, "bold"),command=cut)
edit_menu.add_separator()
edit_menu.add_command(label="REDO::->:->", font=("Aerial", 15, "bold"),command=text_area.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="UNDO::->:->", font=("Aerial", 15, "bold"),command=text_area.edit_undo)
edit_menu.add_separator()
edit_menu.add_command(label="CLEAR ALL :->:", font=("Aerial", 15, "bold"), command=root.destroy)


# adding the menu

about = Menu(main_menu, fg="white", bg="black")
main_menu.add_cascade(label="ABOUT", menu=about)
des = ('''This is the text editor that is made\n by Er. Sunil Kumar gupta.\n
He is the student of BBDU. He is third year student that is design 
this new version of notepad pro.''')
about.add_command(label=des, font=("Aerial", 10, "bold"))

# adding the help menu
help = Menu(main_menu, fg="white", bg="black", )
main_menu.add_cascade(label="HELP", menu=help)

#making the menu for the size selection for the text
size = Menu(main_menu,fg="white",bg="black")
main_menu.add_cascade(label="SIZE SELECTION",menu=size)
size.add_command(label=" ::-> 10 ->::", font=("Aerial", 15, "bold"))
size.add_separator()
size.add_command(label=" ::-> 12 ->::", font=("Aerial", 15, "bold"))
size.add_separator()
size.add_command(label=" ::-> 14 ->::", font=("Aerial", 15, "bold"))
size.add_separator()
size.add_command(label=" ::-> 16 ->::", font=("Aerial", 15, "bold"))
size.add_separator()
size.add_command(label=" ::-> 18 ->::", font=("Aerial", 15, "bold"))
size.add_separator()
size.add_command(label=" ::-> 20 ->::", font=("Aerial", 15, "bold"))
size.add_separator()
size.add_command(label=" ::-> 22 ->::", font=("Aerial", 15, "bold"))
size.add_separator()
size.add_command(label=" ::-> 22 ->::", font=("Aerial", 15, "bold"))
size.add_separator()
size.add_command(label=" ::-> 24 ->::", font=("Aerial", 15, "bold"))
size.add_separator()
size.add_command(label=" ::-> 26 ->::", font=("Aerial", 15, "bold"))
size.add_separator()
size.add_command(label=" ::-> 28 ->::", font=("Aerial", 15, "bold"))
size.add_separator()
size.add_command(label=" ::-> 30 ->::", font=("Aerial", 15, "bold"))
size.add_separator()
size.add_command(label=" ::-> 32 ->::", font=("Aerial", 15, "bold"))
text_area.focus()
root.resizable()
root.mainloop()