from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox


class Crear:
    letras = {0:"P)",1:"Q)",2:"R)",3:"S)",4:"T)",5:"U)",6:"V)",7:"W)",8:"X)"}
    def __init__(self,ventana_crear,ventana_principal,preposiciones):
        self.ventana = ventana_crear
        self.ventanaPrincipal = ventana_principal
        self.preposiciones = preposiciones
        self.ventana.geometry("1280x832")
        self.ventana.configure(background = "#ACACAC")
        self.set_header()
        self.set_elements()
    

    
    def set_header(self):
        frame = Frame(self.ventana, background="#C8C8C8",width=1280,height=95)
        frame.pack()
        titleLable = Label(frame,text="Preposiciones Automaticas",font="Consolas 48",fg="#060B24",bg="#C8C8C8")
        titleLable.place(x=220,y=10)
        button_volver = Button(frame,text="Volver",font="Consolas 20",background="#060B24",fg="#FFFFFF",command= self.volver)
        button_volver.place(x=0, y=25)
    def set_elements(self):
        global e
        global mostrar
        global agregar
        textLabel = Label(self.ventana, text="Ingrese 1-9 numero de preposiciones: ", font="Consolas 32",fg="#060B24",background="#ACACAC")
        textLabel.pack(pady=25)
        
        e = Entry(self.ventana, width=15,font="Consolas 32",background="#D9D9D9",fg="#060B24")
        e.pack(pady=15)
        agregar = Button(self.ventana,text="Crear",background="#060B24",fg="#FFFFFF",font="Consolas 32",command=self.crear_preposiciones)
        agregar.pack(pady=20)
        mostrar = Frame(self.ventana,width=630,height=350,background="#C8C8C8")
        mostrar.pack(pady=20)
        s = ""
        for i in range(len(self.preposiciones)):
            s += self.letras[i] + self.preposiciones[i] + "\n"
        l = Label(mostrar,text=s, background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",wraplength=600)
        l.place(y=40,x=65)
    
    def crear_preposiciones(self):
        global mostrar
        lista = ["Pedro corre un maraton","Jose es super fuerte","La vinotinto va al mundial","Mi perro es muy grande","Hoy llovera","Londres esta frio","Lima es la capital de peru","Dos es un numero par","Rusia esta en guerra"]
        # if len(self.preposiciones) >=8:
        #     agregar.configure(state="disabled")
        #     e.configure(state="disabled")
        self.preposiciones.clear()
        mostrar.destroy()
        mostrar = Frame(self.ventana,width=630,height=350,background="#C8C8C8")
        mostrar.pack(pady=20)
        if (int(e.get()) <= 9):

            for i in range(int(e.get())):
                self.preposiciones.append(lista[i])
            s = ""
            for i in range(len(self.preposiciones)):
                s += self.letras[i] + self.preposiciones[i] + "\n"
            l = Label(mostrar,text=s, background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",wraplength=600)
            l.place(y=40,x=65)

        
            
        else:
            messagebox.showerror("Error","Maximo 9 preposiciones")
            
                
    
    def volver(self):
        self.ventana.withdraw()
        self.ventanaPrincipal.deiconify()
        