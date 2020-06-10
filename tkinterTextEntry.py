import tkinter as tk

def set_full_name():
    print("You clicked me")
    f_name = entryOne.get()
    l_name = entryTwo.get()
    #entryThree.insert(0,f_name+" "+l_name)
    fullnameVar.set(f_name+" "+l_name)

form =tk.Tk()

form.title("Text boxes")
fullnameVar = tk.StringVar()
labelOne = tk.Label(form,text = "First Name")
entryOne = tk.Entry(form, relief = "raised")


labelTwo = tk.Label(form,text="Last Name")
entryTwo = tk.Entry(form)


labelThree = tk.Label(form,text = "Full Name")
entryThree = tk.Entry(form, relief = "flat",textvariable = fullnameVar)

btnFullName = tk.Button(form,text = "Full name",command = set_full_name)

labelOne.grid(row = 0,column = 0,padx = 15,pady =15)
entryOne.grid(row = 0,column = 1,padx = 15,pady = 15)


labelTwo.grid(row = 1 , column = 0 ,padx = 15)
entryTwo.grid(row = 1,column = 1)


labelThree.grid(row = 2,column = 0,padx = 15,pady =15)
entryThree.grid(row = 2,column = 1,padx = 15,pady = 15)

btnFullName.grid(columnspan = 2, padx = 15, pady = 15)

form.mainloop()