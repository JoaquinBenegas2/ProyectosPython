# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

from tkinter import *
from tkinter import ttk, messagebox
from tkinter import END, re

class Calculadora:
    def __init__(self, root):

#------ VENTANA ------------------------------------------------------------------

        self.ventana = root
     
        self.colorNumeros="#121212"
        self.colorOper="#1f1f1f"
        self.colorBg="#262626"
        self.colorIg="#4a4a4a"
    
        self.ventana.configure(bg = self.colorBg)
        self.ventana.title("Cálculadora")
        self.ventana.resizable(0,0)
        
        menu=Menu(self.ventana)
        self.ventana.config(menu=menu)
        
        subMenu=Menu(menu, tearoff=0)
        menu.add_cascade(label="Ver", menu=subMenu)
        subMenu.add_command(label="Estandar", command=self.calculadoraEstandar)
        subMenu.add_command(label="Cientifica", command="")
        subMenu.add_separator()
        subMenu.add_command(label="Salir", command=self.salir)
        
        self.pantalla=Entry(self.ventana, width=40, state="disabled", borderwidth=2, disabledbackground=self.colorBg, disabledforeground="white", font=("Helvetica",15), justify="right")
        self.pantalla.grid(row=1, column=0, columnspan=4, padx=5, pady=5, ipady=23)
        
        self.i = 0


#------ BOTONES ------------------------------------------------------------------
#     
    def crearBotonNum(self, texto, background):
        return Button(self.ventana, text=texto, width=9, height=1, borderwidth = 0, font=("Helvetica", 15, "bold"), fg="white", bg=background,command=lambda:self.click(texto))
    
    def crearBoton(self, texto, background):
        return Button(self.ventana, text=texto, width=9, height=1, borderwidth = 0, font=("Helvetica", 15), fg="white", bg=background, command=lambda:self.click(texto))

    # Limpiar
    def crearBotonLimpiar(self, texto, background):
        return Button(self.ventana, text=texto, width=9, height=1, borderwidth = 0, font=("Helvetica", 15), fg="white", bg=background, command=lambda:self.limpiar())

    # Deshacer
    def crearBotonDeshacer(self, texto, background):
        return Button(self.ventana, text=texto, width=9, height=1, borderwidth = 0, font=("Helvetica", 15), fg="white", bg=background, command=lambda:self.deshacer())

    # Igual
    def crearBotonIgual(self, texto, background):
        return Button(self.ventana, text=texto, width=9, height=1, borderwidth = 0, font=("Helvetica", 15), fg="white", bg=background, command=lambda:self.realizar_operacion())
    
    def crearBotonM(self, texto, background):
        return Button(self.ventana, text=texto, width=3, height=1, borderwidth = 0, font=("Helvetica", 15), fg="white", bg=background, command=lambda:self.click(texto))


#------ DISEÑO ------------------------------------------------------------------

    def calculadoraEstandar(self):
        self.Texto = Label(self.ventana, text="Estandar", font=("Helvetica", 15), fg="white", bg=self.colorBg)
        self.Texto.grid(row=0, column=0, padx=5, pady=5)

        self.Texto = Label(self.ventana, text=" ", font=("Helvetica", 15), fg="white", bg=self.colorBg)
        self.Texto.grid(row=2, column=0, padx=5, pady=5)
        
        self.botonMC = self.crearBotonM("MC", self.colorBg).place(x=9.50, y=129)
        self.botonMR = self.crearBotonM("MR", self.colorBg).place(x=95.95, y=129)
        self.botonM = self.crearBotonM("M+", self.colorBg).place(x=182.40, y=129)
        self.botonMm = self.crearBotonM("M-", self.colorBg).place(x=268.85, y=129)
        self.botonMS = self.crearBotonM("MS", self.colorBg).place(x=355.30, y=129)
        self.botonM = self.crearBotonM("M⁺", self.colorBg).place(x=441.75, y=129)
        
        self.boton16 = self.crearBoton("%", self.colorOper).grid(row=3, column=0, padx=5, pady=5)
        self.boton17 = self.crearBoton("√", self.colorOper).grid(row=3, column=1, padx=5, pady=5)
        self.boton18 = self.crearBoton("^2", self.colorOper).grid(row=3, column=2, padx=5, pady=5)
        #self.boton18 = self.crearBoton("x²", self.colorOper).grid(row=3, column=2, padx=5, pady=5)
        self.boton19 = self.crearBoton("¹/ₓ", self.colorOper).grid(row=3, column=3, padx=5, pady=5)
        self.boton20 = self.crearBotonLimpiar("CE", self.colorOper).grid(row=4, column=0, padx=5, pady=5)
        self.boton21 = self.crearBotonLimpiar("C", self.colorOper).grid(row=4, column=1, padx=5, pady=5)
        self.boton22 = self.crearBotonDeshacer("⌫", self.colorOper).grid(row=4, column=2, padx=5, pady=5)
        self.boton23 = self.crearBoton("÷", self.colorOper).grid(row=4, column=3, padx=5, pady=5)
        
        self.boton7 = self.crearBotonNum("7", self.colorNumeros).grid(row=5, column=0, padx=5, pady=5)
        self.boton8 = self.crearBotonNum("8", self.colorNumeros).grid(row=5, column=1, padx=5, pady=5)
        self.boton9 = self.crearBotonNum("9", self.colorNumeros).grid(row=5, column=2, padx=5, pady=5)
        self.boton10 = self.crearBoton("x", self.colorOper).grid(row=5, column=3, padx=5, pady=5)
        self.boton4 = self.crearBotonNum("4", self.colorNumeros).grid(row=6, column=0, padx=5, pady=5)
        self.boton5 = self.crearBotonNum("5", self.colorNumeros).grid(row=6, column=1, padx=5, pady=5)
        self.boton6 = self.crearBotonNum("6", self.colorNumeros).grid(row=6, column=2, padx=5, pady=5)
        self.boton11 = self.crearBoton("-", self.colorOper).grid(row=6, column=3, padx=5, pady=5)
        self.boton1 = self.crearBotonNum("1", self.colorNumeros).grid(row=7, column=0, padx=5, pady=5)
        self.boton2 = self.crearBotonNum("2", self.colorNumeros).grid(row=7, column=1, padx=5, pady=5)
        self.boton3 = self.crearBotonNum("3", self.colorNumeros).grid(row=7, column=2, padx=5, pady=5)
        self.boton12 = self.crearBoton("+", self.colorOper).grid(row=7, column=3, padx=5, pady=5)
        self.boton13 = self.crearBoton("±", self.colorOper).grid(row=8, column=0, padx=5, pady=5)
        self.boton0 = self.crearBotonNum("0", self.colorNumeros).grid(row=8, column=1, padx=5, pady=5)
        self.boton14 = self.crearBoton(",", self.colorOper).grid(row=8, column=2, padx=5, pady=5)
        self.boton15 = self.crearBotonIgual("=", self.colorIg).grid(row=8, column=3, padx=5, pady=5)


#------ METODOS ------------------------------------------------------------------

    def click(self, texto): 
        self.pantalla.configure(state="normal")
        self.texto_lenght = len(texto)
        self.pantalla.insert(self.i, texto)
        self.i += self.texto_lenght
        self.pantalla.configure(state="disabled")

    def limpiar(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete(0, END)
        self.pantalla.configure(state="disabled")

    def deshacer(self):
        self.pantalla.configure(state="normal")
        self.estadoPantalla = self.pantalla.get()
        if len(self.estadoPantalla):
            self.nuevoEstadoPantalla = self.estadoPantalla[:-1]
            self.pantalla.delete(0, END)
            self.pantalla.insert(0, self.nuevoEstadoPantalla)
        self.pantalla.configure(state="disabled")

    def realizar_operacion(self):
        self.pantalla.configure(state="normal")
        try: 
            self.operacion = self.pantalla.get()
            self.operacion=re.sub("÷", "/", self.operacion)
            self.operacion=re.sub("x", "*", self.operacion)
            self.operacion=re.sub(",", ".", self.operacion)
            self.operacion=re.sub("√", "**(0.5)", self.operacion)
            #self.operacion=re.sub("x²", "**2", self.operacion) 
            self.operacion=re.sub("^2", "**2", self.operacion)
            #self.operacion.replace("^2", "**2")

            self.resultado = eval(self.operacion)
            
            self.pantalla.delete(0, END)
            self.pantalla.insert(0, self.resultado)
            self.pantalla.configure(state="disabled")
        except:
            self.pantalla.delete(0, END)
            self.pantalla.insert(0, "ERROR")
            self.i = 0
            self.pantalla.configure(state="disabled")
        
    def salir(self):
        self.salir=messagebox.askquestion("Salir", "¿Desea salir de la Calculadora?")
        if self.salir == "yes":
            self.ventana.quit()
            self.ventana.destroy()
        
    
        
    """def calculadoraCientifica(self):
        
        self.boton3 = self.crearBoton("x²", self.colorOper).grid(row=2, column=0, padx=5, pady=5)
        self.boton3 = self.crearBoton("xʸ", self.colorOper).grid(row=2, column=1, padx=5, pady=5)
        self.boton3 = self.crearBoton("sin", self.colorOper).grid(row=2, column=2, padx=5, pady=5)
        self.boton3 = self.crearBoton("cos", self.colorOper).grid(row=2, column=3, padx=5, pady=5)
        self.boton1 = self.crearBoton("tan", self.colorOper).grid(row=2, column=4, padx=5, pady=5)
        self.boton2 = self.crearBoton("√", self.colorOper).grid(row=3, column=0, padx=5, pady=5)
        self.boton3 = self.crearBoton("10²", self.colorOper).grid(row=3, column=1, padx=5, pady=5)
        self.boton3 = self.crearBoton("log", self.colorOper).grid(row=3, column=2, padx=5, pady=5)
        self.boton3 = self.crearBoton("Exp", self.colorOper).grid(row=3, column=3, padx=5, pady=5)
        self.boton1 = self.crearBoton("Mod", self.colorOper).grid(row=3, column=4, padx=5, pady=5)
        self.boton3 = self.crearBoton("⬆", self.colorOper).grid(row=4, column=0, padx=5, pady=5)
        self.boton3 = self.crearBoton("CE", self.colorOper).grid(row=4, column=1, padx=5, pady=5)
        self.boton3 = self.crearBoton("C", self.colorOper).grid(row=4, column=2, padx=5, pady=5)
        self.boton3 = self.crearBoton("⌫", self.colorOper).grid(row=4, column=3, padx=5, pady=5)
        self.boton3 = self.crearBoton("÷", self.colorOper).grid(row=4, column=4, padx=5, pady=5)
        
        self.boton1 = self.crearBoton("π", self.colorOper).grid(row=5, column=0, padx=5, pady=5)
        self.boton1 = self.crearBotonNum(7, self.colorNumeros).grid(row=5, column=1, padx=5, pady=5)
        self.boton2 = self.crearBotonNum(8, self.colorNumeros).grid(row=5, column=2, padx=5, pady=5)
        self.boton3 = self.crearBotonNum(9, self.colorNumeros).grid(row=5, column=3, padx=5, pady=5)
        self.boton3 = self.crearBoton("x", self.colorOper).grid(row=5, column=4, padx=5, pady=5)
       
        self.boton1 = self.crearBoton("n!", self.colorOper).grid(row=6, column=0, padx=5, pady=5)
        self.boton1 = self.crearBotonNum(4, self.colorNumeros).grid(row=6, column=1, padx=5, pady=5)
        self.boton2 = self.crearBotonNum(5, self.colorNumeros).grid(row=6, column=2, padx=5, pady=5)
        self.boton3 = self.crearBotonNum(6, self.colorNumeros).grid(row=6, column=3, padx=5, pady=5)
        self.boton3 = self.crearBoton("-", self.colorOper).grid(row=6, column=4, padx=5, pady=5)
        
        self.boton1 = self.crearBoton("±", self.colorOper).grid(row=7, column=0, padx=5, pady=5)
        self.boton1 = self.crearBotonNum(3, self.colorNumeros).grid(row=7, column=1, padx=5, pady=5)
        self.boton2 = self.crearBotonNum(2, self.colorNumeros).grid(row=7, column=2, padx=5, pady=5)
        self.boton3 = self.crearBotonNum(1, self.colorNumeros).grid(row=7, column=3, padx=5, pady=5)
        self.boton3 = self.crearBoton("+", self.colorOper).grid(row=7, column=4, padx=5, pady=5)
        
        self.boton1 = self.crearBoton("(", self.colorOper).grid(row=8, column=0, padx=5, pady=5)
        self.boton1 = self.crearBoton(")", self.colorOper).grid(row=8, column=1, padx=5, pady=5)
        self.boton2 = self.crearBotonNum(0, self.colorNumeros).grid(row=8, column=2, padx=5, pady=5)
        self.boton3 = self.crearBoton(",", self.colorOper).grid(row=8, column=3, padx=5, pady=5)
        self.boton3 = self.crearBoton("=", self.colorOper).grid(row=8, column=4, padx=5, pady=5)"""


#-----------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL 

root = Tk() 
aplicacion = Calculadora(root)   
aplicacion.calculadoraEstandar()     
root.mainloop()        