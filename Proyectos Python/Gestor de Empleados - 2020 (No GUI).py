# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:13:52 2020

@author: Joaquin
"""

class Empleado ():
    def __init__(self, nombre, apellido, DNI, horasTrabajo, añosTrabajo, cantHijos, valorHora): # Metodo constructor que recibe parametros
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.horasTrabajo = horasTrabajo
        self.añosTrabajo = añosTrabajo
        self.cantHijos = cantHijos
        self.valorHora = valorHora
        self.aporteJubilatorio = 0.11
        self.aporteObraSocial = 0.03
        self.aporteSeguridadSocial = 0.03
        self.antiguedad = 0.02
        self.sueldoFinal = 0.0
        self.sueldoBruto = 0.0
        self.aportesTotales = 0.0
        self.asignacion = 0.0
        
    def mostrarMenu(self): # Este metodo se encarga de mostrar el menu
        print("-"*24)
        print("MENU".center(24, " "))
        print("-"*24)
        print("1. Cargar datos.")
        print("2. Calcular el sueldo de un empleado.")
        print("3. Imprimir lista de datos completa de los empleados.")
        print("4. Consultar los datos de un empleado por DNI.")
        print("5. Consultar los datos de un empleado por Apellido.")
        print("6. Mostrar la lista de los empleados con mas de 2 hijos.")
        print("7. Mostrar la lista de empleados con sueldos superiores al promedio.")
        print("8. Modificar empleado.")
        print("9. Salir.")
        # Se le pide al usuario que ingrese la opcion deseada
        opcion = int(input("Seleccione una opcion: "))
        return opcion # El metodo retorna el valor de la opcion ingresada
        
    def cargarDatos(self, empleados): # Metodo cargarDatos que recibe la lista empleados como parametro
        # Se pide al usuario que ingrese los datos
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.apellido = input("Ingrese el apellido del empleado: ")
        self.DNI = input("Ingrese el DNI del empleado: ")
        # El siguiente for controla que el DNI no se haya ingresado previamente
        for i in range(len(empleados)):
            while self.DNI == empleados[i].DNI:
                print("✘ El DNI no se puede repetir ✘")
                self.DNI = input("Ingrese el DNI del empleado: ") 
        self.horasTrabajo = int(input("Ingrese la cantidad de horas trabajadas: "))
        self.añosTrabajo = int(input("Ingrese la cantidad de años trabajados: "))
        self.cantHijos = int(input("Ingrese la cantidad de hijos: "))
        self.valorHora = int(input("Ingrese el valor que gana por hora: "))
        # Se crea un objeto empleado y se le pasa los datos por parametro
        empleado = Empleado(self.nombre, self.apellido, self.DNI, self.horasTrabajo, self.añosTrabajo, self.cantHijos, self.valorHora)
        # A continuacion se asignan a las variables los datos retornados por los metodos
        empleado.sueldoBruto = self.calcularSueldoBruto()
        empleado.asignacion = self.calcularSalarioFamiliar()
        empleado.aportesTotales = self.calcularAporteObraSocial() + self.calcularAporteSeguridadSocial() + self.calcularAporteJubilatorio()
        empleado.sueldoFinal = self.calcularSueldo()
        # Finalmente se agrega el empleado a la lista "empleados"
        empleados.append(empleado)
        
    def calcularSueldoBruto(self): # Metodo que calcula el sueldo bruto a partir de las horas trabajadas y el valor correspondiente
        suelBruto = self.valorHora * self.horasTrabajo
        return suelBruto # Retorna el sueldoBruto
 
    def calcularAntiguedad(self): # Metodo que calcula el aumento de acuerdo a la antiguedad (2%)
        antig = self.calcularSueldoBruto() * self.antiguedad
        return antig # Retorna el valor de la antiguedad
    
    def calcularAporteJubilatorio(self): # Metodo que calcula el aporte jubilatorio (11%)
        apJubilatorio = self.calcularSueldoBruto() * self.aporteJubilatorio
        return apJubilatorio # Retorna el valor del aporte jubilatorio
    
    def calcularAporteSeguridadSocial(self): # Metodo que calcula el aporte de seguridad social (3%)
        apSeguridadSocial = self.calcularSueldoBruto() * self.aporteSeguridadSocial
        return apSeguridadSocial # Retorna el valor del aporte
    
    def calcularAporteObraSocial(self): # Metodo que calcula el aporte de la obra social (3%)
        apObraSocial = self.calcularSueldoBruto() * self.aporteObraSocial
        return apObraSocial # Retorna el valor del aporte de la obra social
    
    def calcularSalarioFamiliar(self): # Metodo que calcula el salario familiar de acuerdo a la cantidad de hijos
        salFamiliar = self.cantHijos * 3500
        return salFamiliar # Retorna el salario familiar
        
    def calcularSueldo(self): # El metodo calcularSueldo, suma los aumentos del salario familiar y la antiguedad, y resta el valor de los aportes
        sueldoFin = self.calcularSueldoBruto() + self.calcularSalarioFamiliar() + self.calcularAntiguedad() - self.calcularAporteObraSocial() - self.calcularAporteSeguridadSocial() - self.calcularAporteJubilatorio()
        return sueldoFin
    
    # El siguiente metodo muestra los datos de un empleado, recibe como parametro la lista empleados y el valor de i
    def mostrarDatos(self, empleados, i):
        print("Nombre:", empleados[i].nombre)
        print("Apellido:", empleados[i].apellido)
        print("DNI:", empleados[i].DNI)
        print("Horas trabajadas:", empleados[i].horasTrabajo)
        print("Cantidad de años:", empleados[i].añosTrabajo)
        print("Sueldo Bruto:", empleados[i].sueldoBruto)
        print("Cantidad de Hijos:", empleados[i].cantHijos)
        print("Asignacion:", empleados[i].asignacion)
        print("Aportes Totales:", empleados[i].aportesTotales)
        print("Sueldo Final:", empleados[i].sueldoFinal)
        print("-"*36)
        
    def mostrarDatosEmpleados(self, empleados): # Metodo que se encarga de mostrar los datos de todos los empleados
        print("\n")
        print("-"*24)
        print("LISTA DE EMPLEADOS".center(24, " "))
        print("-"*24)
        # For que recorre la lista empleados
        for i in range (len(empleados)):
            self.mostrarDatos(empleados, i) # Se llama al metodo "mostrarDatos" para mostrar la informacion
        # Si la cantidad de empleados es igual a 0 se muestra un mensaje
        if len(empleados) == 0:
            print("Aun no hay empleados cargados")
            
    def mostrarSueldoEmpleado(self, empleados): # El metodo mostrarSueldoEmpleado recibe la lista empleados como parametro
        encontrar = False # Variable que nos permite saber si el dato deseado fue encontrado
        DNI = input("Ingrese el DNI del empleado a calcular: ")
        for i in range(len(empleados)): # Luego de pedir el DNI de un empleado, se recorre  la lista
            if DNI == empleados[i].DNI:
                # Si el DNI se encuentra se muestra el sueldo del empleado y la variable encontrar ahora es True
                encontrar = True 
                print("El sueldo del empleado", empleados[i].nombre, "es:", empleados[i].sueldoFinal)
        if encontrar == False: # Si el DNI ingresado no coincide se muestra el siguiente mensaje
            print("No se ha encontrado el DNI ingresado.")
                
    def consultarPorDNI(self, empleados): # El metodo consultarPorDNI recibe como parametro la lista empleados
        encontrar = False # Variable que nos permite saber si el dato deseado fue encontrado
        DNI = input("Ingrese el DNI del empleado a consultar: ")
        for i in range(len(empleados)): # Al igual que el metodo anterior, recorre la lista buscando coincidencias con el DNI
            if DNI == empleados[i].DNI:
                # Si el DNI se encuentra, se llama al metodo "mostrarDatos" que recibe la lista empleados y el valor de i
                encontrar = True
                print("-"*24)
                self.mostrarDatos(empleados, i) 
        if encontrar == False: # Si el DNI ingresado no coincide se muestra el siguiente mensaje
            print("No se ha encontrado el DNI ingresado.")
              
    # El metodo consultarPorApellido funciona igual que el metodo consultarPorDNI, recibe como parametro la lista empleados
    def consultarPorApellido(self, empleados): 
        encontrar = False
        apell = input("Ingrese el apellido del empleado a consultar: ")
        # En este caso, se pide al usuario un apellido y se recorre la lista
        for i in range(len(empleados)):
            if apell == empleados[i].apellido:
                # Si el apellido coincide, se muestran los datos del empleado a partir del metodo "mostrarDatos"
                encontrar = True
                print("-"*24)
                self.mostrarDatos(empleados, i)
        if encontrar == False: # Si el apellido no se encuentra, se muestra el siguiente mensaje
            print("No se ha encontrado el apellido ingresado.")
    
    def listaMasDosHijos(self, empleados): # Este metodo recibe la lista empleados como parametro
        encontrar = False
        print("\n")
        print("-"*24)
        print("LISTA DE EMPLEADOS CON MAS DE 2 HIJOS".center(24, " "))
        # Se recorre la lista y busca empleados cuya cantidad de  hijos sea mayor a 2
        for i in range(len(empleados)):
            if empleados[i].cantHijos > 2:
                # Si encuentra, muestra un mensaje con los datos y la cantidad de hijos
                encontrar = True
                print("-"*24)
                print(empleados[i].nombre, empleados[i].apellido, "con", empleados[i].cantHijos, "hijos")
        if encontrar == False: # Si no se encuentran empleados con mas de 2 hijos se muestra un mensaje
            print("No se han encontrado empleados con mas de 2 hijos")
                
    # Metodo que muestra los empleados con sueldo mayor al promedio, recibe la lista empleados como parametro
    def listaSuperiorPromedio(self, empleados): 
        print("\n")
        print("-"*24)
        print("LISTA DE EMPLEADOS CON SUELDO MAYOR AL PROMEDIO".center(24, " "))
        suma = 0 # Acumulador
        # Para evitar errores, el promedio se calcula siempre y cuando se haya cargado al menos un empleado
        if len(empleados) > 0:
            # Se recorre la lista y se suman los sueldos
            for i in range(len(empleados)):
                suma += empleados[i].sueldoFinal
            promedio = suma / len(empleados) # Calculo del promedio
            # Una vez con el promedio, se recorre la lista en busca de los empleados con un sueldo mayor
            for i in range(len(empleados)): 
                if empleados[i].sueldoFinal > promedio:
                    # Se muestran aquellos empleados y dicho sueldo
                    print("-"*24)
                    print(empleados[i].nombre, empleados[i].apellido, "con un sueldo de $", empleados[i].sueldoFinal)
        # Si no hay empleados cargados se muestra un mensaje
        if len(empleados) == 0:
            print("Aun no hay empleados cargados")
       
    # Metodo que permite modificar el dato de un empleado         
    def modificarEmpleado(self, empleados):
        encontrar = False
        print("\n")
        print("-"*24)
        print("MODIFICAR EMPLEADO".center(24, " "))
        print("-"*24)
        # Primero se le pide al usuario el DNI del empleado a modificar
        empleadoDNI = input("Ingrese el DNI del empleado que desea modificar: ")
        # Se recorre la lista y en caso de encontrarlo se ejecuta el siguiente codigo
        for i in range(len(empleados)):
            if empleadoDNI == empleados[i].DNI:
                # Se muestra un pequeño menu con los posibles datos a modificar
                encontrar = True
                print("1. Nombre.")
                print("2. Apellido.")
                print("3. DNI.")
                print("4. Horas Trabajadas.")
                print("5. Cantidad de años.")
                print("6. Cantidad de hijos.")
                print("7. Valor por hora.")
                
                # El usuario ingresa la opcion deseada
                op = int(input("Ingrese el dato que desea modificar: "))
                
                # El siguiente while permite asegurar un valor que no sea mayor a 7
                while(op > 7):
                    print("✘ Dato NO valido ✘")
                    op = int(input("Seleccione una opcion: "))  
                    
                # De acuerdo a la opcion ingresada, se procede a la modificacion
                # Se muestra el dato actual y se le pide al usuario el nuevo dato
                # Finalmente se reemplaza valor antiguo por el dato ingresado nuevamente
                if op==1:
                    print("Nombre actual:", empleados[i].nombre)
                    nom = input("Ingrese el nuevo nombre: ")
                    empleados[i].nombre = nom 
                if op==2:
                    print("Apellido actual:", empleados[i].apellido)
                    apel = input("Ingrese el nuevo apellido: ")
                    empleados[i].apellido = apel
                if op==3:
                    print("DNI actual:", empleados[i].DNI)
                    dni = input("Ingrese el nuevo DNI: ")
                    empleados[i].DNI = dni   
                if op==4:
                    print("Horas actuales:", empleados[i].horasTrabajo)
                    hor = input("Ingrese la nueva cantidad de horas: ")
                    empleados[i].horasTrabajo = hor   
                if op==5:
                    print("Años actuales:", empleados[i].añosTrabajo)
                    ani = input("Ingrese la nueva cantidad de años: ")
                    empleados[i].añosTrabajo = ani
                if op==6:
                    print("Cantidad de hijos actuales:", empleados[i].cantHijos)
                    hij = input("Ingrese la nueva cantidad de hijos: ")
                    empleados[i].cantHijos = hij  
                if op==7:
                    print("Valor por hora actual:", empleados[i].valorHora)
                    hor = input("Ingrese el nuevo valor por hora: ")
                    empleados[i].valorHora = hor
                
                # Se corrigen los datos de acuerdo al nuevo dato ingresado
                empleados[i].sueldoBruto = self.calcularSueldoBruto()
                empleados[i].asignacion = self.calcularSalarioFamiliar()
                empleados[i].aportesTotales = self.calcularAporteObraSocial() + self.calcularAporteSeguridadSocial() + self.calcularAporteJubilatorio()
                empleados[i].sueldoFinal = self.calcularSueldo()
        # Si el DNI ingresado en un inicio no se encuentra, se muestra un mensaje
        if encontrar == False:
            print("No se ha encontrado el DNI ingresado")                
                
#----------------------   
# Programa Principal
#---------------------- 

listaDeEmpleados = [] # Se crea la lista que posteriormente almacenará los empleados
 # Se crea un objeto Empleado y se ingresan los datos correspondientes como parametros
empleado = Empleado("", "", "", 0.0, 0.0, 0.0, 0.0)

opcion = empleado.mostrarMenu() # Definimos la variable opcion y le asignamos el valor que nos retorna el metodo mostrarMenu()

# Mientras la opcion ingresada sea mayor a 9, se mostrará un mensaje de error y se pedirá el ingreso de la opcion nuevamente 
while(opcion > 9):
    print("✘ Dato NO valido ✘")
    opcion = int(input("Seleccione una opcion: "))
    
# Mientras la opcion sea distinta de 9 pueden ejecutarse las opciones del 1 al 8
while(opcion != 9):
    if(opcion == 1): # Si la opcion es igual a 1
        empleado.cargarDatos(listaDeEmpleados) # Se llama al metodo mediante el objeto y se ingresa como parametro la lista de empleados
    
    if(opcion == 2): # Si la opcion es igual a 2
        empleado.mostrarSueldoEmpleado(listaDeEmpleados) # Se llama al metodo mediante el objeto y se ingresa como parametro la lista de empleados
    
    if(opcion == 3): # Si la opcion es igual a 3
        empleado.mostrarDatosEmpleados(listaDeEmpleados) # Se llama al metodo mediante el objeto y se ingresa como parametro la lista de empleados
        
    if(opcion == 4): # Si la opcion es igual a 4
        empleado.consultarPorDNI(listaDeEmpleados) # Se llama al metodo mediante el objeto y se ingresa como parametro la lista de empleados
        
    if(opcion == 5): # Si la opcion es igual a 5
        empleado.consultarPorApellido(listaDeEmpleados) # Se llama al metodo mediante el objeto y se ingresa como parametro la lista de empleados
        
    if(opcion == 6): # Si la opcion es igual a 6
        empleado.listaMasDosHijos(listaDeEmpleados) # Se llama al metodo mediante el objeto y se ingresa como parametro la lista de empleados
    
    if(opcion == 7): # Si la opcion es igual a 7
        empleado.listaSuperiorPromedio(listaDeEmpleados) # Se llama al metodo mediante el objeto y se ingresa como parametro la lista de empleados
    
    if(opcion == 8): # Si la opcion es igual a 8
        empleado.modificarEmpleado(listaDeEmpleados) # Se llama al metodo mediante el objeto y se ingresa como parametro la lista de empleados
    
    print("\n") # Este print simula un enter en pantalla
    opcion = empleado.mostrarMenu() # Nuevamente definimos la variable opcion y le asignamos el valor que nos retorna el metodo mostrarMenu()

# En el caso de que se ingrese la opcion 9, el programa finaliza  y se muestra el siguiente mensaje
print("\n")
print("-"*24)
print("PROGRAMA FINALIZADO".center(24, " ")) 
print("-"*24)
    