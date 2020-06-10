from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk

filename = " "


def parseline(line):
    parse_line = line.strip()
    space_pos = parse_line.rfind(" ")
    new_text_line = parse_line[space_pos:] + " " + parse_line[:space_pos]
    return new_text_line.strip()

def open_file():
    global filename
    filename= filedialog.askopenfilename(initialdir="/",
                                          title="Open file",
                                          filetypes=(
                                              ("Text Files", "*.txt"), ("Music Files", "*.mp3"), ("All Files", "*.*"))
                                          )
    textarea.delete('1.0', tk.END)
    try:

        if filename:
            the_file = open(filename)

            #textarea.insert(tk.END, the_file.read())
            counter = 0
            for line in the_file.readlines():

                textline = parseline(line)
                textarea.insert(tk.END, textline + "\n")
                counter += 1

            the_file.close()
            # print(filename)
            print(counter)
            loop_message = 'Total number of line in text is ', counter
            messagebox.showinfo('result', loop_message)

            the_file = open(filename, 'r')
            longg = ''
            for line in the_file:
                if len(line) > len(longg):
                    longg = line
            messagebox.showinfo('longest word','The longest word is '+longg)
            return longg

        elif filename == "":
            messagebox.showinfo('warning', "You clicked cancel")
    except:
        print("You didn't open anything bro ")
        messagebox.showinfo("Error", "Couldn't open file")

# print("File open")
# messagebox.showinfo("Confirmation","File open")
def save_file():
    global filename
    try:
        if filename:
            text_area = textarea.get(1.0, "end-1c")
            save_text = open(filename, "w")
            save_text.write(text_area)
            save_text.close()
            messagebox.showinfo('Sucesss', "File saved")
        else:
            messagebox.showinfo('warning', "You clicked cancel")
    except:
        messagebox.showinfo('warning', "You didn't open anything dude!!!!!!!!!")

def save_file_as():

    try:
        save_text_as = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if save_text_as:
            text_area = textarea.get(1.0, "end-1c")
            save_text_as.write(text_area)
            save_text_as.close()
            messagebox.showinfo('Sucesss', "File saved")
        else:
            messagebox.showinfo('warning', "You clicked cancel")
    except:
        messagebox.showinfo('warning', "You didn't open anything dude!!!!!!!!!")
def close_text_area():
    textarea.delete(1.0,tk.END)
form = tk.Tk()

form.title("Menus")

menuBar = tk.Menu(form)

fileMenuItem = tk.Menu(menuBar, tearoff=0)

editMenuItem = tk.Menu(menuBar, tearoff=0)

fileMenuItem.add_command(label="open", command=open_file)

fileMenuItem.add_command(label="Save", command=save_file)

fileMenuItem.add_command(label="Save as", command=save_file_as)

fileMenuItem.add_separator()

fileMenuItem.add_command(label="close text-area", command=close_text_area)

fileMenuItem.add_command(label="close", command=form.quit)

editMenuItem.add_command(label="cut", command=open_file)

editMenuItem.add_command(label="copy", command=open_file)

editMenuItem.add_command(label="paste", command=open_file)

editMenuItem.add_command(label="rename", command=open_file)

menuBar.add_cascade(label="File", menu=fileMenuItem)

menuBar.add_cascade(label="Edit", menu=editMenuItem)

form.config(menu=menuBar)

textarea = tk.Text(form, height=12, width=80, wrap=tk.WORD)
textarea.insert(tk.END, "This is the default text")
# textarea.delete('1.0',tk.END)
textarea.configure(font=("Arial", 14, "bold", "italic"))
scrollV = tk.Scrollbar(form, orient=tk.VERTICAL)
scrollV.config(command=textarea.yview())  # refresh view when to scroll
textarea.configure(yscrollcommand=scrollV.set)  # attaches it to text area
scrollV.pack(side=tk.RIGHT, fill=tk.Y)  # it fills the whole area

scrollH = tk.Scrollbar(form, orient=tk.HORIZONTAL)
scrollH.config(command=textarea.xview())
textarea.configure(xscrollcommand=scrollH.set)
scrollH.pack(side=tk.BOTTOM, fill=tk.X)

textarea.pack()

tk.mainloop()
