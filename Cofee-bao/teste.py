from tkinter import *



app = Tk()
app.geometry('600x600')



lista = ['objeto1', "objeto2", 'objeto3', 'objeto4', 'objeto5', 'objeto6', 'objeto7', 'objeto8',
         'objeto8', 'objeto8', 'objeto8', 'objeto8', 'objeto8', 'objeto8', 'objeto8', 'objeto8']


listbx = Listbox(app,bg='black',foreground='white')
for i in lista:
    listbx.insert(END, i)


listbx.pack(anchor=E)

app.mainloop()
