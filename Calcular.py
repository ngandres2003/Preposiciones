from tkinter import *


class Calcular:
    letras = {0:"P)",1:"Q)",2:"R)",3:"S)",4:"T)",5:"U)",6:"V)",7:"W)",8:"X)"}
    letrasOperaciones = {"P":0,"Q":1,"R":2,"S":3,"T":4,"U":5,"V":6,"W":7,"X":8}
    operaciones = {"^" : "y","v":"o","|":"si y solo si,", "-":"si", "~":"no es cierto que","(":" ",")":" "}
    def __init__(self,ventana_calcular,ventana_principal,preposiciones):
        self.ventana = ventana_calcular
        self.ventanaPrincipal = ventana_principal
        self.preposiciones = preposiciones
        self.ventana.geometry("1280x832")
        self.ventana.configure(background = "#ACACAC")
        self.set_header()
        self.mostrar_preposiciones()
        self.mostrar_resultados()
        self.calculadora()
    
    
        
    
    
    def set_header(self):
        frame = Frame(self.ventana, background="#C8C8C8",width=1280,height=95)
        frame.pack()
        titleLable = Label(frame,text="Operacion de Preposiciones",font="Consolas 48",fg="#060B24",bg="#C8C8C8")
        titleLable.place(x=280,y=10)
        button_volver = Button(frame,text="Volver",font="Consolas 20",background="#060B24",fg="#FFFFFF",command= self.volver)
        button_volver.place(x=0, y=25)
    

    def mostrar_preposiciones(self):
        global mostrar
        titleLable = Label(self.ventana,text="Preposiciones Existentes: ",font="Consolas 28",fg="#060B24",bg="#ACACAC")
        titleLable.place(x=40,y=130)
        mostrar = Frame(self.ventana,width=550,height=350,background="#C8C8C8")
        mostrar.place(x = 40, y = 190)
        # s = ""
        # for i in range(len(self.preposiciones)):
        #     s += self.letras[i] + self.preposiciones[i] + "\n"
        # l = Label(mostrar,text=s, background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",wraplength=600)
        # l.place(y=40,x=15)

        size = len(self.preposiciones)
        self.generar(size)
      
    def insertar(self,letra):
        
        e.insert(END,letra)
        
        
    def generar(self,size):
        global mostrar
        mostrar.destroy()
        mostrar = Frame(self.ventana,width=550,height=380,background="#C8C8C8")
        mostrar.place(x = 40, y = 190)

        if size == 1:
            l1 = Label(mostrar,text="P)"+self.preposiciones[0],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l1.place(y=20,x=15)
            l1.bind("<Button-1>",lambda _ : self.insertar("P"))
        elif size ==2:
            l1 = Label(mostrar,text="P)"+self.preposiciones[0],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l1.place(y=20,x=15)
            l1.bind("<Button-1>",lambda _ : self.insertar("P"))
            l2 = Label(mostrar,text="Q)"+self.preposiciones[1],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l2.place(y=60,x=15)
            l2.bind("<Button-1>",lambda _ : self.insertar("Q"))
        elif size ==3:
            l1 = Label(mostrar,text="P)"+self.preposiciones[0],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l1.place(y=20,x=15)
            l1.bind("<Button-1>",lambda _ : self.insertar("P"))
            l2 = Label(mostrar,text="Q)"+self.preposiciones[1],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l2.place(y=60,x=15)
            l2.bind("<Button-1>",lambda _ : self.insertar("Q"))
            l3 = Label(mostrar,text="R)"+self.preposiciones[2],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l3.place(y=100,x=15)
            l3.bind("<Button-1>",lambda _ : self.insertar("R"))
        elif size == 4:
            l1 = Label(mostrar,text="P)"+self.preposiciones[0],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l1.place(y=20,x=15)
            l1.bind("<Button-1>",lambda _ : self.insertar("P"))
            l2 = Label(mostrar,text="Q)"+self.preposiciones[1],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l2.place(y=60,x=15)
            l2.bind("<Button-1>",lambda _ : self.insertar("Q"))
            l3 = Label(mostrar,text="R)"+self.preposiciones[2],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l3.place(y=100,x=15)
            l3.bind("<Button-1>",lambda _ : self.insertar("R"))
            l4 = Label(mostrar,text="S)"+self.preposiciones[3],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l4.place(y=140,x=15)
            l4.bind("<Button-1>",lambda _ : self.insertar("S"))
        elif size == 5:
            l1 = Label(mostrar,text="P)"+self.preposiciones[0],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l1.place(y=20,x=15)
            l1.bind("<Button-1>",lambda _ : self.insertar("P"))
            l2 = Label(mostrar,text="Q)"+self.preposiciones[1],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l2.place(y=60,x=15)
            l2.bind("<Button-1>",lambda _ : self.insertar("Q"))
            l3 = Label(mostrar,text="R)"+self.preposiciones[2],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l3.place(y=100,x=15)
            l3.bind("<Button-1>",lambda _ : self.insertar("R"))
            l4 = Label(mostrar,text="S)"+self.preposiciones[3],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l4.place(y=140,x=15)
            l4.bind("<Button-1>",lambda _ : self.insertar("S"))
            l5 = Label(mostrar,text="T)"+self.preposiciones[4],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l5.place(y=180,x=15)
            l5.bind("<Button-1>",lambda _ : self.insertar("T"))
        elif size == 6:
            l1 = Label(mostrar,text="P)"+self.preposiciones[0],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l1.place(y=20,x=15)
            l1.bind("<Button-1>",lambda _ : self.insertar("P"))
            l2 = Label(mostrar,text="Q)"+self.preposiciones[1],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l2.place(y=60,x=15)
            l2.bind("<Button-1>",lambda _ : self.insertar("Q"))
            l3 = Label(mostrar,text="R)"+self.preposiciones[2],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l3.place(y=100,x=15)
            l3.bind("<Button-1>",lambda _ : self.insertar("R"))
            l4 = Label(mostrar,text="S)"+self.preposiciones[3],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l4.place(y=140,x=15)
            l4.bind("<Button-1>",lambda _ : self.insertar("S"))
            l5 = Label(mostrar,text="T)"+self.preposiciones[4],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l5.place(y=180,x=15)
            l5.bind("<Button-1>",lambda _ : self.insertar("T"))
            l6 = Label(mostrar,text="U)"+self.preposiciones[5],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l6.place(y=220,x=15)
            l6.bind("<Button-1>",lambda _ : self.insertar("U"))
        elif size == 7:
            l1 = Label(mostrar,text="P)"+self.preposiciones[0],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l1.place(y=20,x=15)
            l1.bind("<Button-1>",lambda _ : self.insertar("P"))
            l2 = Label(mostrar,text="Q)"+self.preposiciones[1],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l2.place(y=60,x=15)
            l2.bind("<Button-1>",lambda _ : self.insertar("Q"))
            l3 = Label(mostrar,text="R)"+self.preposiciones[2],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l3.place(y=100,x=15)
            l3.bind("<Button-1>",lambda _ : self.insertar("R"))
            l4 = Label(mostrar,text="S)"+self.preposiciones[3],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l4.place(y=140,x=15)
            l4.bind("<Button-1>",lambda _ : self.insertar("S"))
            l5 = Label(mostrar,text="T)"+self.preposiciones[4],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l5.place(y=180,x=15)
            l5.bind("<Button-1>",lambda _ : self.insertar("T"))
            l6 = Label(mostrar,text="U)"+self.preposiciones[5],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l6.place(y=220,x=15)
            l6.bind("<Button-1>",lambda _ : self.insertar("U"))
            l7 = Label(mostrar,text="V)"+self.preposiciones[6],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l7.place(y=260,x=15)
            l7.bind("<Button-1>",lambda _ : self.insertar("V"))
        elif size == 8:
            l1 = Label(mostrar,text="P)"+self.preposiciones[0],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l1.place(y=20,x=15)
            l1.bind("<Button-1>",lambda _ : self.insertar("P"))
            l2 = Label(mostrar,text="Q)"+self.preposiciones[1],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l2.place(y=60,x=15)
            l2.bind("<Button-1>",lambda _ : self.insertar("Q"))
            l3 = Label(mostrar,text="R)"+self.preposiciones[2],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l3.place(y=100,x=15)
            l3.bind("<Button-1>",lambda _ : self.insertar("R"))
            l4 = Label(mostrar,text="S)"+self.preposiciones[3],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l4.place(y=140,x=15)
            l4.bind("<Button-1>",lambda _ : self.insertar("S"))
            l5 = Label(mostrar,text="T)"+self.preposiciones[4],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l5.place(y=180,x=15)
            l5.bind("<Button-1>",lambda _ : self.insertar("T"))
            l6 = Label(mostrar,text="U)"+self.preposiciones[5],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l6.place(y=220,x=15)
            l7.bind("<Button-1>",lambda _ : self.insertar("U"))
            l7 = Label(mostrar,text="V)"+self.preposiciones[6],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l7.place(y=260,x=15)
            l7.bind("<Button-1>",lambda _ : self.insertar("V"))
            l8 = Label(mostrar,text="W)"+self.preposiciones[7],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l8.place(y=300,x=15)
            l8.bind("<Button-1>",lambda _ : self.insertar("W"))
        elif size == 9:
            l1 = Label(mostrar,text="P)"+self.preposiciones[0],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l1.place(y=20,x=15)
            l1.bind("<Button-1>",lambda _ : self.insertar("P"))
            l2 = Label(mostrar,text="Q)"+self.preposiciones[1],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l2.place(y=60,x=15)
            l2.bind("<Button-1>",lambda _ : self.insertar("Q"))
            l3 = Label(mostrar,text="R)"+self.preposiciones[2],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l3.place(y=100,x=15)
            l3.bind("<Button-1>",lambda _ : self.insertar("R"))
            l4 = Label(mostrar,text="S)"+self.preposiciones[3],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l4.place(y=140,x=15)
            l4.bind("<Button-1>",lambda _ : self.insertar("S"))
            l5 = Label(mostrar,text="T)"+self.preposiciones[4],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l5.place(y=180,x=15)
            l5.bind("<Button-1>",lambda _ : self.insertar("T"))
            l6 = Label(mostrar,text="U)"+self.preposiciones[5],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l6.place(y=220,x=15)
            l6.bind("<Button-1>",lambda _ : self.insertar("U"))
            l7 = Label(mostrar,text="V)"+self.preposiciones[6],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l7.place(y=260,x=15)
            l7.bind("<Button-1>",lambda _ : self.insertar("V"))
            l8 = Label(mostrar,text="W)"+self.preposiciones[7],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l8.place(y=300,x=15)
            l8.bind("<Button-1>",lambda _ : self.insertar("W"))
            l9 = Label(mostrar,text="X)"+self.preposiciones[8],background="#C8C8C8",fg="#060B24",font="Consolas 20",justify="left",cursor="hand2")
            l9.place(y=340,x=15)
            l9.bind("<Button-1>",lambda _ : self.insertar("X"))

    
   


            
            
            

        
    
    def mostrar_resultados(self):
        global resultado

        titleLable = Label(self.ventana, text= "Resultados: ",font="Consolas 24",fg="#060B24",bg="#ACACAC")
        titleLable.place(x=40, y= 580)

        resultado = Frame(self.ventana,width=550, height=150,background="#D9D9D9")
        resultado.place(x= 40, y =640)

           
        
    
    def calculadora(self):
        global e
        
        label = Label(self.ventana, text= "Calculadora de \nOperaciones de Conjuntos ",font="Consolas 24",fg="#060B24",bg="#ACACAC")
        label.place(x = 700, y = 235)
        base = Frame(self.ventana,width=450,height=285,bg="#D9D9D9")
        base.place(x =700, y= 360)
        e = Entry(base, width=29,font="Consolas 19",background="#BFBCBC",fg="#060B24")
        e.place(x=20,y=20)

        button_ac = Button(base,text="AC",font="Consolas 19",background="#060B24",fg="#FFFFFF",width=13,command=lambda: e.delete(0,END))
        button_ac.place(x = 20, y = 80)
        button_del = Button(base,text="DEL",font="Consolas 19",background="#060B24",fg="#FFFFFF",width=13,command=self.ac)
        button_del.place(x = 239, y = 80)

        button_y = Button(base,text="^",font="Consolas 19",background="#060B24",fg="#FFFFFF",width=6,command=lambda : e.insert(END,"^"))
        button_y.place(x = 20, y = 150)

        button_o = Button(base,text="v",font="Consolas 19",background="#060B24",fg="#FFFFFF",width=6,command=lambda:e.insert(END,"v"))
        button_o.place(x = 118, y = 150)

        button_flecha = Button(base,text="->",font="Consolas 19",background="#060B24",fg="#FFFFFF",width=6,command=lambda:e.insert(END,"->"))
        button_flecha.place(x = 337, y = 150)

        button_bi = Button(base,text="<->",font="Consolas 19",background="#060B24",fg="#FFFFFF",width=6,command=lambda:e.insert(END,"<->"))
        button_bi.place(x = 239, y = 150)

        button_no = Button(base,text="~",font="Consolas 19",background="#060B24",fg="#FFFFFF",width=11,command=lambda:e.insert(END,"~"))
        button_no.place(x = 20, y = 220)


        button_igual = Button(base,text="=",font="Consolas 19",background="#060B24",fg="#FFFFFF",width=16,command=self.realizarOperacion)
        button_igual.place(x = 198, y = 220)
        
    def ac(self):
        
        current = e.get()
        e.delete(0,END)
        e.insert(0,current[:-1])
        

    def realizarOperacion(self):
        
            global resultado
            texto = e.get()
            
            #Remplazo letras por la preposicion
            for x in texto:
                if x in self.letrasOperaciones:
                    texto = texto.replace(x, " " +self.preposiciones[self.letrasOperaciones[x]]+" ")

            texto = texto.replace("<->","|")
            texto = texto.replace("->","-")
            
            texto = texto.split(" ")
        
            #Remplazo los simbolos por los conectores
            for x in range(len(texto)):
                if texto[x] in self.operaciones:
                    texto[x] = self.operaciones[texto[x]]
            
            
            
            texto = " ".join(texto)
            
                    

            resultado.destroy()
            resultado = Frame(self.ventana,width=550, height=150,background="#D9D9D9")
            resultado.place(x= 40, y =640)
            a = Label(resultado,text=texto,font="Consolas 15",background="#D9D9D9",fg="#060B24",wraplength=530,justify="left")
            a.place(x=10,y=10)

           




            



            
            



                
            



      
 

    def volver(self):
        self.ventana.withdraw()
        self.ventanaPrincipal.deiconify()
        