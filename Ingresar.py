from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox


class Ingresar:
    letras = {0:"P)",1:"Q)",2:"R)",3:"S)",4:"T)",5:"U)",6:"V)",7:"W)",8:"X)"}
    def __init__(self,ventana_ingresar,preposiciones,lista_p):
        self.ventana = ventana_ingresar
        self.ventanaPrincipal = preposiciones
        self.preposiciones = lista_p
        self.ventana.geometry("1280x832")
        self.ventana.configure(background = "#ACACAC")
        self.set_header()
        self.set_elements()
        
    
    

    
    
    def set_header(self):
        frame = Frame(self.ventana, background="#C8C8C8",width=1280,height=95)
        frame.pack()
        titleLable = Label(frame,text="    Preposiciones",font="Consolas 48",fg="#060B24",bg="#C8C8C8")
        titleLable.place(x=280,y=10)
        button_volver = Button(frame,text="Volver",font="Consolas 20",background="#060B24",fg="#FFFFFF",command= self.volver)
        button_volver.place(x=0, y=25)

    
    def set_elements(self):
        global e
        global mostrar
        global agregar
        textLabel = Label(self.ventana, text="Ingrese Preposiciones: ", font="Consolas 32",fg="#060B24",background="#ACACAC")
        textLabel.pack(pady=25)

        e = Entry(self.ventana, width=30,font="Consolas 32",background="#D9D9D9",fg="#060B24")
        e.pack(pady=15)
        
        agregar = Button(self.ventana,text="Agregar",background="#060B24",fg="#FFFFFF",font="Consolas 32",command=self.agregar_preposicion)
        agregar.pack(pady=20)

        mostrar = Frame(self.ventana,width=630,height=350,background="#C8C8C8")
        mostrar.pack(pady=20)
        s = ""
        for i in range(len(self.preposiciones)):
            s += self.letras[i] + self.preposiciones[i] + "\n"
        l = Label(mostrar,text=s, background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",wraplength=600)
        l.place(y=40,x=65)
        if len(self.preposiciones) >=8:
            agregar.configure(state="disabled")
            e.configure(state="disabled")
    
    def agregar_preposicion(self): 
        global l
        global mostrar
        mostrar.destroy()
        mostrar = Frame(self.ventana,width=630,height=350,background="#C8C8C8")
        mostrar.pack(pady=20)    
        p = e.get()
        s = ""
        for i in range(len(self.preposiciones)):
            s += self.letras[i] + self.preposiciones[i] + "\n"

        l = Label(mostrar,text=s, background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",wraplength=600)
        l.place(y=40,x=65)


        if len(self.preposiciones) >=8:
            agregar.configure(state="disabled")
            e.configure(state="disabled")
        if (len(p) <= 0):
            messagebox.showerror("error","Debes ingresar una preposicion")
        
        
            
        else:
            self.preposiciones.append(p)
            e.delete(0,END)
            s = ""
            for i in range(len(self.preposiciones)):
                s += self.letras[i] + self.preposiciones[i] + "\n"
            l = Label(mostrar,text=s, background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",wraplength=600)
            l.place(y=40,x=65)
    
    def volver(self):
        self.ventana.withdraw()
        self.ventanaPrincipal.deiconify()
        