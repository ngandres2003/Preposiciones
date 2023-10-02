from tkinter import *
from Ingresar import Ingresar
from Crear import Crear
from Calcular import Calcular
from tkinter import simpledialog
from tkinter import messagebox

class Preposiciones:
    preposiciones = []
    
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry("1280x832")
        self.ventana.configure(background ="#ACACAC")
        self.set_header()
        self.set_button()
    

    def set_header(self):
        frame = Frame(self.ventana, background="#C8C8C8",width=1280,height=95).pack()
        titleLable = Label(frame,text="Operaciones de Proposiciones",font="Consolas 48",fg="#060B24",bg="#C8C8C8")
        titleLable.place(x=180,y=10)
    

    def set_button(self):
        labelT = Label(self.ventana,text="  Preposiciones: ",font="Consolas 40",fg="#FFFFFF",background="#ACACAC").pack(pady=90)
        button_ingresar = Button(self.ventana,text="Ingresar",background="#060B24",fg="#FFFFFF",font="Consolas 34",width=20,command=self.ir_ventana_ingresar)
        button_ingresar.pack()
        button_crear = Button(self.ventana,text="Creacion Automatica",background="#060B24",fg="#FFFFFF",font="Consolas 34",width=20,command=self.ir_ventana_crear)
        button_crear.pack(pady=50)
        button_calcular = Button(self.ventana,text="Calcular Operaciones",background="#FFFFFF",fg="#060B24",font="Consolas 36",width=21,command=self.ir_ventana_calcular)
        button_calcular.pack(pady=10)
    
    def ir_ventana_ingresar(self):
        self.ventana.withdraw()
        ventana_ingresar = Toplevel(self.ventana)
        ventana_ingresar.resizable(False,False)
        app_ingresar = Ingresar(ventana_ingresar, self.ventana,self.preposiciones)
    
    def ir_ventana_crear(self):
        self.ventana.withdraw()
        ventana_crear = Toplevel(self.ventana)
        ventana_crear.resizable(False,False)
        app_crear = Crear(ventana_crear, self.ventana,self.preposiciones)
    
    def ir_ventana_calcular(self):
        if (len(self.preposiciones) > 0):
            self.ventana.withdraw()
            ventana_calcular = Toplevel(self.ventana)
            ventana_calcular.resizable(False,False)
            app_calcular = Calcular(ventana_calcular, self.ventana,self.preposiciones)
        else:
            messagebox.showerror("Error","Debes crear preposiciones")

        
    


        
        