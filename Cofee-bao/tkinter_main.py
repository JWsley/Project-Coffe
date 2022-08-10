


import posiciona


from tkinter import *
from tkinter import messagebox





from db_estoque import *
from class_fabric import *







def soma(valor):
  if lbl['text']>=0:
    lbl['text'] += valor
    





def subtrai(valor):
  if lbl['text'] - valor <0:
      pass
  else:
    lbl['text'] -= valor



def confirmm():
    var = lbl['text']
    lbl['text'] = 0
    infm = messagebox.showinfo(title='Nice Broh.', message=f'Compra realizada com sucesso! Totalizando um total de:{var} a ser pago ')


  

def reset():
    lbl['text'] = 0





def saveEmp():
    fabrc = Fabric()
    nomEmpr = nfabr.get()
    if nomEmpr == "":
          infm = messagebox.showerror(title='Erro.', message='EAlgo não foi preenchido corretamente.Tente novamente!')
    else:
        fabrc.cadastro_fabric(nomEmpr)
        infm = messagebox.showinfo(title='Nice Broh.', message='Empresa cadastrada com Sucesso!!')
    

def saveProd():
    Estq = Db_estoque()
    nomeProd = desc.get()
    codEmp = codF.get()
    if  (nomeProd == "") or (codEmp == ""):
        nfm = messagebox.showerror(title='Erro.', message='Algo não foi preenchido corretamente.Tente novamente! ')
    else:
        qunt = quant.get()
        Estq.cadastrar_produto(nomeProd,codEmp,qunt)
        if  Estq.verifyx ==True :
            infm = messagebox.showinfo(title='Nice Broh.', message='Produto  cadastrado com Sucesso!!')

        else:
            infm = messagebox.showerror(title='Erro.', message='Empresa inexistente')

        
   


def updateName():
  db = Db_estoque()
  codeT = codp.get()
  name = descp.get()
  db.update_produto(code = codeT,new_name = name)
  infm = messagebox.showinfo(title='Nice Broh.', message=f'Nome alterado com Sucesso!..Codigo do produto:{codeT}|Novo:{name}')




def excluirProdut():
    db = Db_estoque()
    cod = excluir.get()
    db.dropProd(cod)
    if db.ok == True:
        infm = messagebox.showinfo(title='ok', message='Produto Excluido com Sucesso!!!')
    elif db.ok == False:
        infm2 = messagebox.showerror(title='Ops..!', message='Produto não existente..!')






def search():
    Estq = Db_estoque()
    a = proc.get()
    db = Estq.listar_unidade(a)
    if a != '':
        listbx.insert(END, '═══════════════════════════════',db)
    else:
        for y in range(len(Estq.pls)):
            print(len(Estq.pls))
            listbx.insert(END, '═══════════════════════════════',Estq.pls[y])


def clear():
    listbx.delete(0,END)



def startMenu():
  f1.forget()
  f8.pack()

def startEstq():
  f8.forget()
  f2.pack()




def cadWindow():
    f2.forget()
    f3.pack()


def cadFabr():
    f2.forget()
    f4.pack()

def searchw():
    f2.forget()
    f5.pack()

def alterw():
    f2.forget()
    f6.pack()


def delp():
    f2.forget()
    f7.pack()


app = Tk()
app.geometry('1920x1080')
app.resizable(width=False, height=False)
app.title('Café do Bão')
app.configure(bg='black')








#================- = ================================== = ===============================



app.bind('<Button-1>', posiciona.inicio_place)
app.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, app))
app.bind('<Button-2>', lambda arg: posiciona.para_geometry(app))
#======================================================================================





#========= = = ============================= = =======[]
#========= =      =FRAME 1                         = =======[]
#========= = = ============================= = =======[]



f1 = Frame(app)
f1.pack()



phot1 = PhotoImage(file="img/menu.png")


back1 = Label(f1,image=phot1)
back1.pack()



btn1 =  PhotoImage(file="img/btn1.png")

btn = Button(f1,image=btn1,bd=0,command=startMenu)
btn.place(width=424, height=128, x=682, y=487)



#========= = = ============================= = =======[]
#========= =      =FRAME 2                         = =======[]
#========= = = ============================= = =======[]



f2 = Frame(app)

backg2 = PhotoImage(file="img/lmenu.png")

back2 = Label(f2,image=backg2)
back2.pack()

cadProd = PhotoImage(file='img/botao_produto.png')

prodbt = Button(f2,image=cadProd,bd=0,command=cadWindow)
prodbt.place(width=422, height=122, x=153, y=344)


botao_voltar = PhotoImage(file='img/voltar.png')

voltar = Button(f2, image=botao_voltar, bd=0, command=lambda: [f8.pack(), f2.pack_forget()])
voltar.place(width=62, height=89, x=53, y=23)

fabt = PhotoImage(file="img/fabricbt1.png")

fabrbt = Button(f2,image=fabt,bd=0,command=cadFabr)
fabrbt.place(width=420, height=124,x=706, y=343)

schbt = PhotoImage(file='img/searchbt1.png')

searchbt = Button(f2,image=schbt,bd=0,command=searchw)
searchbt.place(width=422, height=124, x=1274, y=344)


altrbt = PhotoImage(file="img/alterprodbt1.png")

altbt = Button(f2,image=altrbt,bd=0,command=alterw)
altbt.place(width=420, height=124, x=383, y=591)

delimg = PhotoImage(file="img/delbt1.png")

delbt = Button(f2,image=delimg,bd=0,command=delp)
delbt.place(width=420, height=124, x=1021, y=592)



#========= = = ============================= = =======[]
#========= =      =FRAME 3                         = =======[]
#========= = = ============================= = =======[]

f3 = Frame(app)

backg3 = PhotoImage(file="img/cadProdt.png")
cadastrar = PhotoImage(file='img/cadastrar.png')

back3 = Label(f3,image=backg3)
back3.pack() 

voltar = Button(f3, image=botao_voltar, bd=0, command=lambda: [f2.pack(), f3.pack_forget()])
voltar.place(width=62, height=89, x=53, y=23)

botao_cadastrar = Button(f3, image=cadastrar, bd=0,command=saveProd)
botao_cadastrar.place(width=327, height=70, x=733, y=843)

desc = Entry(f3, bd=0)
desc.config(font='Arieal 20')
desc.place(width=742, height=45, x=578, y=376)

codF = Entry(f3, bd=0)
codF.config(font='Arieal 20')
codF.place(width=742, height=45, x=578, y=500)

quant = Entry(f3, bd=0)
quant.config(font='Arieal 20')
quant.place(width=742, height=45, x=578, y=626)

#========= = = ============================= = =======[]
#========= =      =FRAME 4                        = =======[]
#========= = = ============================= = =======[]

f4 = Frame(app)


backg4 = PhotoImage(file='img/cadFabr.png')

back4 = Label(f4,image=backg4)
back4.pack()

voltar = Button(f4, image=botao_voltar, bd=0, command=lambda: [f2.pack(), f4.pack_forget()])
voltar.place(width=62, height=89, x=53, y=23)

botao_cadastrar = Button(f4, image=cadastrar, bd=0,command=saveEmp)
botao_cadastrar.place(width=335, height=77, x=738, y=842)

nfabr = Entry(f4, bd=0,font='Arieal 20')

nfabr.place(width=742, height=45, x=654, y=505)


#========= = = ============================= = =======[]
#========= =      =FRAME 5                         = =======[]
#========= = = ============================= = =======[]

f5 = Frame(app)


backg5 = PhotoImage(file='img/search.png')


back5 = Label(f5,image=backg5)
back5.pack()


imgsearch = PhotoImage(file='img/codigo_produtobt.png')


voltar = Button(f5, image=botao_voltar,background='#FBCAAA',activebackground='#FBCAAA', bd=0, command=lambda: [f2.pack(), f5.pack_forget()])
voltar.place(width=70, height=95, x=53, y=23)




procbt = Button(f5,image=imgsearch,bd=0,command=search)
procbt.place(width=380, height=75, x=226, y=335)

proc = Entry(f5, bd=0)
proc.config(font='Arieal 20')
proc.place(width=742, height=45, x=679, y=356)


liximg = PhotoImage(file='img/clearbt.png')

lixeira = Button(f5,image=liximg,bd=0,command=clear)
lixeira.place(width=59, height=68, x=541, y=915)


listbx = Listbox(f5,font='Arial 30',justify=CENTER,background='#F4B87B',bd=5,selectbackground='#241726',selectforeground='white',borderwidth=5)
listbx.place(width=820, height=315, x=644, y=642)


#========= = = ============================= = =======[]
#========= =      =FRAME 6                         = =======[]
#========= = = ============================= = =======[]

f6 = Frame(app)


backg6 = PhotoImage(file='img/alter.png')

alterar = PhotoImage(file='img/alterar.png')


back6 = Label(f6,image=backg6)
back6.pack()

voltar = Button(f6, image=botao_voltar, bd=0,background='#FBCAAA',activebackground='#FBCAAA', command=lambda: [f2.pack(), f6.pack_forget()])
voltar.place(width=65, height=89, x=57, y=23)

botao_alterar = Button(f6, image=alterar, bd=0,command=updateName)
botao_alterar.place(width=313, height=74, x=747, y=841)

codp = Entry(f6, bd=0)
codp.config(font='Arieal 20')
codp.place(width=742, height=45, x=649, y=461)

descp = Entry(f6, bd=0)
descp.config(font='Arieal 20')
descp.place(width=742, height=45, x=649, y=590)

#========= = = ============================= = =======[]
#========= =      =FRAME 7                         = =======[]
#========= = = ============================= = =======[]
f7 = Frame(app)

backg7 = PhotoImage(file='img/excluir.png')

excluirimg = PhotoImage(file='img/excluirBt.png')

back7 = Label(f7, image=backg7)
back7.pack()

voltar = Button(f7, image=botao_voltar, bd=0, command=lambda: [f2.pack(), f7.pack_forget()])
voltar.place(width=62, height=89, x=53, y=23)

botao_excluir = Button(f7, image=excluirimg, bd=0,command=excluirProdut)
botao_excluir.place(width=315, height=77, x=746, y=838)

excluir = Entry(f7, bd=0)
excluir.config(font='Arieal 20')
excluir.place(width=742, height=45, x=648, y=460)





#========= = = ============================= = =======[]
#========= =      =FRAME 8                         = =======[]
#========= = = ============================= = =======[]









f8 = Frame(app)



backg8 = PhotoImage(file = 'img/menu_select.png')







back8 = Label(f8,image=backg8)
back8.pack()




boxestq = PhotoImage(file = 'img/estqopen.png')



voltar = Button(f8, image=botao_voltar,background='#FBCAAA',activebackground='#FBCAAA', bd=0, command=lambda: [f1.pack(), f8.pack_forget()])
voltar.place(width=70, height=95, x=53, y=23)



boxestq2 = Button(f8,image=boxestq,bd=0,command=startEstq)
boxestq2.place(width=121, height=100, x=1773, y=19)

# .place(width=121, height=98, x=1773, y=19)


somimg = PhotoImage(file='img/soma.png')
subimg = PhotoImage(file='img/sub.png')
confimg = PhotoImage(file='img/confirm2.png')
clearimg = PhotoImage(file = 'img/clearbt.png')


btsoma_whater = Button(f8,image=somimg,bd=0,command=lambda:[soma(5)])
btsoma_whater.place(width=72, height=68, x=606, y=822)

btsub_whater = Button(f8,image=subimg,bd=0,command=lambda:[subtrai(5)])
btsub_whater.place(width=78, height=58, x=497, y=821)




btsoma_cap = Button(f8,image=somimg,bd=0,command = lambda:[soma(10)])
btsoma_cap.place(width=72, height=68, x=981, y=821)

btsub_cap = Button(f8,image=subimg,bd=0,command=lambda:[subtrai(10)])
btsub_cap.place(width=67, height=53, x=872, y=826)




btsoma_cheese = Button(f8,image=somimg,bd=0,command=lambda:[soma(12)])
btsoma_cheese.place(width=72, height=68, x=1352, y=821)

btsub_cheese= Button(f8,image=subimg,bd=0,command=lambda:[subtrai(12)])
btsub_cheese.place(width=73, height=54, x=1242, y=826)



lbl = Label(f8,text=0,font='Arial 40',bd=0,foreground='white',background='#81645D')
lbl.place(width=204, height=82, x=1573, y=818)

btconf = Button(f8,image=confimg,bd=0,command=confirmm)
btconf.place(width=63, height=95, x=1833, y=875)





clearbox = Button(f8,image=clearimg,bd=0,command=reset)
clearbox.place(width=56, height=79, x=363, y=854)

app.mainloop()