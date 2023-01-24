
def mostrarMenu(): 
    print("")
    print("\033[1;36m"+"►"+"\033[0m", "Elija una opcion: "+"\033[0m")
    print("\033[1;32m"+"1."+"\033[0m", "Pizzas", "\033[1;32m"+"| 2."+"\033[0m", "Bebidas")

    while True:
        try:
            comida = int(input("Ingrese el numero correspondiente a la opcion que desea: "))

            while(comida < 1 or comida > 2):
                comida = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

            break
        except ValueError:
            print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")

    return comida


def menuPizzas():

    print("\033[1;36m"+"►"+"\033[0m", "Tipos de Pizza: "+"\033[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;32m"+"1."+"\033[0m", "Vegetarianas", "\033[1;33m"+"    ⋄ $330"+"\033[0m")
    print("\033[1;32m"+"2."+"\033[0m", "NO Vegetarianas", "\033[1;33m"+" ⋄ $300"+"\033[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    while True:
        try:
            tipoPizza = int(input("Introduce el numero correspondiente al tipo de pizza que quieres: "))

            while(tipoPizza < 1 or tipoPizza > 2):
                tipoPizza = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

            break
        except ValueError:
            print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")
    
    if tipoPizza == 1:
        pizzaIngredientes=[]
        totalPagar = 330

        print("")
        print("\033[1;36m"+"►"+"\033[0m", "Ingredientes a elegir para las Pizzas Vegetarianas: "+"\033[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\033[1;32m"+"1."+"\033[0m", "Pimiento", "\033[1;33m"+"        + $40"+"\033[0m")
        print("\033[1;32m"+"2."+"\033[0m", "Tofu", "\033[1;33m"+"            + $40"+"\033[0m")
        print("\033[1;32m"+"3."+"\033[0m", "Espinaca", "\033[1;33m"+"        + $40"+"\033[0m")
        print("\033[1;32m"+"4."+"\033[0m", "Calabacín", "\033[1;33m"+"       + $40"+"\033[0m")
        print("\033[1;32m"+"5."+"\033[0m", "Champiñones", "\033[1;33m"+"     + $40"+"\033[0m")
        print("\033[1;32m"+"6."+"\033[0m", "Cebolla", "\033[1;33m"+"         + $40"+"\033[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        while True:
            try:
                ingrediente = int(input("Introduce el ingrediente que deseas: "))

                while(ingrediente < 1 or ingrediente > 6):
                    ingrediente = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

                break
            except ValueError:
                print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")

        if ingrediente == 1:
            sumarIngrediente = "Pimiento"
        elif ingrediente == 2:
            sumarIngrediente = "Tofu"
        elif ingrediente == 3:
            sumarIngrediente = "Espinaca"
        elif ingrediente == 4:
            sumarIngrediente = "Calabacin"
        elif ingrediente == 5:
            sumarIngrediente = "Champiñones"
        else:
            sumarIngrediente = "Cebolla"

        pizzaIngredientes.append(sumarIngrediente)

        print("")
        print("¿Desea agregar mas ingredientes?")
        
        while True:
            try:
                print("\033[1;32m"+"1."+"\033[0m", "SI", "\033[1;32m"+"| 2."+"\033[0m", "NO: ", end="")
                masIngredientes = int(input())

                while(masIngredientes < 1 or masIngredientes > 2):
                    masIngredientes = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

                break
            except ValueError:
                print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")

        while (masIngredientes == 1):
            ingAgregado = False
            while True:
                try:
                    ingrediente = int(input("Introduce el ingrediente que deseas: "))

                    while(ingrediente < 1 or ingrediente > 6):
                        ingrediente = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

                    break
                except ValueError:
                    print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")

            if ingrediente == 1:
                sumarIngrediente = "Pimiento"
            elif ingrediente == 2:
                sumarIngrediente = "Tofu"
            elif ingrediente == 3:
                sumarIngrediente = "Espinaca"
            elif ingrediente == 4:
                sumarIngrediente = "Calabacin"
            elif ingrediente == 5:
                sumarIngrediente = "Champiñones"
            else:
                sumarIngrediente = "Cebolla"

            for i in range (len(pizzaIngredientes)):
                if pizzaIngredientes[i] == sumarIngrediente:
                    print("\033[1;33m"+"Ese ingrediente ya fue agregado"+"\033[0m")
                    ingAgregado = True
                
            if ingAgregado == False:
                pizzaIngredientes.append(sumarIngrediente)
            
            print("")
            print("¿Desea agregar mas ingredientes?")
            while True:
                try:
                    print("\033[1;32m"+"1."+"\033[0m", "SI", "\033[1;32m"+"| 2."+"\033[0m", "NO: ", end="")
                    masIngredientes = int(input())

                    while(masIngredientes < 1 or masIngredientes > 2):
                        masIngredientes = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

                    break
                except ValueError:
                    print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")

        if len(pizzaIngredientes) == 1:
            print(" ")
            print("\033[1;35m"+"Pizza vegetariana con Mozzarella, Tomate y ", end="")
        else: 
            print(" ")
            print("\033[1;35m"+"Pizza vegetariana con Mozzarella, Tomate, ", end="") 
        for i in range(len(pizzaIngredientes)):
            totalPagar = totalPagar + 40
            if i+1 != len(pizzaIngredientes):
                if i+2 == len(pizzaIngredientes):
                    print(pizzaIngredientes[i], " y ", end="", sep="")
                else:
                    print(pizzaIngredientes[i], ", ", end="", sep="")
            else:
                print(pizzaIngredientes[i], end=""+"\033[0m")

        print("\n")    
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\033[1;32m"+"✔"+"\033[0m", "Pizza Vegetariana:", "\033[1;33m"+"           + $330"+"\033[0m")
        print("\033[1;32m"+"✔"+"\033[0m", " Ingredientes Añadidos:", "\033[1;33m","        + $", totalPagar-330, sep="")     
        print("\033[0m"+"                               ━━━━━━━━━")
        print("\033[1;32m"+"✔"+"\033[0m", " Total:", "\033[1;33m","                          $", totalPagar, "\033[0m", sep="")   
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") 

        print("\033[0m", end="")

    else: 
        pizzaIngredientes=[]
        totalPagar = 300

        print("")
        print("\033[1;36m"+"►"+"\033[0m", "Ingredientes a elegir para las Pizzas Vegetarianas: "+"\033[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\033[1;32m"+"1."+"\033[0m", "Peperoni", "\033[1;33m"+"        + $45"+"\033[0m")
        print("\033[1;32m"+"2."+"\033[0m", "Jamón", "\033[1;33m"+"           + $45"+"\033[0m")
        print("\033[1;32m"+"3."+"\033[0m", "Salmón", "\033[1;33m"+"          + $45"+"\033[0m")
        print("\033[1;32m"+"4."+"\033[0m", "Anchoas", "\033[1;33m"+"         + $45"+"\033[0m")
        print("\033[1;32m"+"5."+"\033[0m", "Pollo", "\033[1;33m"+"           + $45"+"\033[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        while True:
            try:
                ingrediente = int(input("Introduce el ingrediente que deseas: "))

                while(ingrediente < 1 or ingrediente > 5):
                    ingrediente = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

                break
            except ValueError:
                print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")

        if ingrediente == 1:
            sumarIngrediente = "Peperoni"
        elif ingrediente == 2:
            sumarIngrediente = "Jamón"
        elif ingrediente == 3:
            sumarIngrediente = "Salmón"
        elif ingrediente == 4:
            sumarIngrediente = "Anchoas"
        else:
            sumarIngrediente = "Pollo"

        pizzaIngredientes.append(sumarIngrediente)

        print("")
        print("¿Desea agregar mas ingredientes?")
        
        while True:
            try:
                print("\033[1;32m"+"1."+"\033[0m", "SI", "\033[1;32m"+"| 2."+"\033[0m", "NO: ", end="")
                masIngredientes = int(input())

                while(masIngredientes < 1 or masIngredientes > 2):
                    masIngredientes = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

                break
            except ValueError:
                print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")

        while (masIngredientes == 1):
            ingAgregado = False
            while True:
                try:
                    ingrediente = int(input("Introduce el ingrediente que deseas: "))

                    while(ingrediente < 1 or ingrediente > 5):
                        ingrediente = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

                    break
                except ValueError:
                    print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")

            if ingrediente == 1:
                sumarIngrediente = "Peperoni"
            elif ingrediente == 2:
                sumarIngrediente = "Jamón"
            elif ingrediente == 3:
                sumarIngrediente = "Salmón"
            elif ingrediente == 4:
                sumarIngrediente = "Anchoas"
            else:
                sumarIngrediente = "Pollo"

            for i in range (len(pizzaIngredientes)):
                if pizzaIngredientes[i] == sumarIngrediente:
                    print("\033[1;33m"+"Ese ingrediente ya fue agregado"+"\033[0m")
                    ingAgregado = True
                
            if ingAgregado == False:
                pizzaIngredientes.append(sumarIngrediente)
            
            print("")
            print("¿Desea agregar mas ingredientes?")
            while True:
                try:
                    print("\033[1;32m"+"1."+"\033[0m", "SI", "\033[1;32m"+"| 2."+"\033[0m", "NO: ", end="")
                    masIngredientes = int(input())

                    while(masIngredientes < 1 or masIngredientes > 2):
                        masIngredientes = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

                    break
                except ValueError:
                    print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")

        if len(pizzaIngredientes) == 1:
            print(" ")
            print("\033[1;35m"+"Pizza no vegetariana con Mozzarella, Tomate y ", end="")
        else: 
            print(" ")
            print("\033[1;35m"+"Pizza no vegetariana con Mozzarella, Tomate, ", end="") 
        
        for i in range(len(pizzaIngredientes)):
            totalPagar = totalPagar + 45
            if i+1 != len(pizzaIngredientes):
                if i+2 == len(pizzaIngredientes):
                    print(pizzaIngredientes[i], " y ", end="", sep="")
                else:
                    print(pizzaIngredientes[i], ", ", end="", sep="")
            else:
                print(pizzaIngredientes[i], end=""+"\033[0m")

        print("\n")    
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\033[1;32m"+"✔"+"\033[0m", "Pizza No Vegetariana:", "\033[1;33m"+"        + $300"+"\033[0m")
        print("\033[1;32m"+"✔"+"\033[0m", " Ingredientes Añadidos:", "\033[1;33m","        + $", totalPagar-300, sep="")     
        print("\033[0m"+"                               ━━━━━━━━━")
        print("\033[1;32m"+"✔"+"\033[0m", " Total:", "\033[1;33m","                          $", totalPagar, "\033[0m", sep="")   
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") 

        print("\033[0m", end="")

    return totalPagar


def menuBebidas(): 
    print("\033[1;36m"+"►"+"\033[0m", "Bebidas a elegir: "+"\033[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;32m"+"1."+"\033[0m", "Agua")
    print("\033[1;32m"+"2."+"\033[0m", "Coca")
    print("\033[1;32m"+"3."+"\033[0m", "Sprite")
    print("\033[1;32m"+"4."+"\033[0m", "Fanta")
    print("\033[1;32m"+"5."+"\033[0m", "Pepsi")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    while True:
            try:
                opBebida = int(input("Introduce la bebida que deseas: "))

                while(opBebida < 1 or opBebida > 5):
                    bebida = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

                break
            except ValueError:
                print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")

    if opBebida == 1:
        bebida = "Agua"
    elif opBebida == 2:
        bebida = "Coca"
    elif opBebida == 2:
        bebida = "Sprite"
    elif opBebida == 2:
        bebida = "Fanta"
    else:
        bebida = "Pepsi"

    print("")
    print("\033[1;36m"+"►"+"\033[0m", "Elija el tamaño de su bebida: "+"\033[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;32m"+"1."+"\033[0m", "500ml", "\033[1;33m"+"           + $45"+"\033[0m")
    print("\033[1;32m"+"2."+"\033[0m", "1000ml", "\033[1;33m"+"          + $60"+"\033[0m")
    print("\033[1;32m"+"3."+"\033[0m", "1500ml", "\033[1;33m"+"          + $75"+"\033[0m")
    print("\033[1;32m"+"4."+"\033[0m", "2000ml", "\033[1;33m"+"          + $90"+"\033[0m")
    print("\033[1;32m"+"5."+"\033[0m", "2500ml", "\033[1;33m"+"          + $120"+"\033[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    while True:
            try:
                bebidaTamaño = int(input("Introduce el tamaño de bebida que deseas: "))

                while(bebidaTamaño < 1 or bebidaTamaño > 5):
                    bebidaTamaño = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

                break
            except ValueError:
                print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")

    totalPagarBebidas = 0

    if bebidaTamaño == 1:
        print("Bebida:", bebida, "de 500ml"+"\033[0m")
        totalPagarBebidas = 45
    elif bebidaTamaño == 2:
        print("Bebida:", bebida, "de 1000ml"+"\033[0m")
        totalPagarBebidas = 60
    elif bebidaTamaño == 3:
        print("Bebida:", bebida, "de 1500ml"+"\033[0m")
        totalPagarBebidas = 75
    elif bebidaTamaño == 4:
        print("Bebida:", bebida, "de 2000ml"+"\033[0m")
        totalPagarBebidas = 90
    else:
        print("Bebida:", bebida, "de 2500ml"+"\033[0m")
        totalPagarBebidas = 120

    return totalPagarBebidas



#Programa Principal
print("\033[1;36m"+"⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀")
print("► 𝙱𝙸𝙴𝙽𝚅𝙴𝙽𝙸𝙳𝙾 𝙰 𝙻𝙰 𝙿𝙸𝚉𝚉𝙴𝚁𝙸𝙰 𝙴𝚄𝚁𝙴𝙺𝙰 ◄"+"\033[0m")
print("¡Podemos ofrecerte varias comidas!")
print("\033[1;36m"+"⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀⇀"+"\033[0m","\n")

print("¿Deseas realizar un pedido?")

totalPedido = 0
realizarPedido = False
pedirPizza = False
pedirBebida = False
totalTodasPizzas = 0
totalTodasBebidas = 0

while True:
            try:
                print("\033[1;32m"+"1."+"\033[0m", "SI", "\033[1;32m"+"| 2."+"\033[0m", "NO: ", end="")
                op = int(input())

                while(op < 1 or op > 2):
                    op = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

                break
            except ValueError:
                print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")

while(op == 1):
    comida=mostrarMenu()
    realizarPedido = True

    if comida == 1:
        print("\n", "\033[1;36m"+"Has elegido PIZZAS: "+"\033[0m", sep="")
        pedirPizza = True
        totalPizzas = menuPizzas()
        totalTodasPizzas = totalTodasPizzas + totalPizzas
        totalPedido = totalPedido + totalPizzas
    else:
        print("\n", "\033[1;36m"+"Has elegido BEBIDAS: "+"\033[0m", sep="")
        pedirBebida = True
        totalBebidas = menuBebidas()
        totalTodasBebidas = totalTodasBebidas + totalBebidas
        totalPedido = totalPedido + totalBebidas

    print("")
    print("¿Deseas agregar otro pedido?")

    while True:
                try:
                    print("\033[1;32m"+"1."+"\033[0m", "SI", "\033[1;32m"+"| 2."+"\033[0m", "NO: ", end="")
                    op = int(input())

                    while(op < 1 or op > 2):
                        op = int(input("\033[1;31m"+"✘ ERROR ✘ Ingrese un numero entero correspondiente a las opciones: "+"\033[0m"))

                    break
                except ValueError:
                    print("\033[1;31m"+"✘ ERROR ✘ El dato ingresado debe ser un entero: "+"\033[0m")



if realizarPedido == True:
    print("")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    if pedirPizza == True and pedirBebida == True:
        print("Solo en Pizzas:       "+"\033[1;33m"+"$", totalTodasPizzas, "\033[0m", sep="")
        print("Solo en Bebidas:      "+"\033[1;33m"+"$", totalTodasBebidas, "\033[0m", sep="")
    elif pedirPizza == True:
        print("Solo en Pizzas:       "+"\033[1;33m"+"$", totalTodasPizzas, "\033[0m", sep="")
    else:
        print("Solo en Bebidas:      "+"\033[1;33m"+"$", totalTodasBebidas, "\033[0m", sep="")
    print("                    ━━━━━━━━")
    print("El total a pagar es   "+"\033[1;33m"+"$", totalPedido, "\033[0m", sep="")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
else:
    print("\033[1;35m"+"¡Genial, vuelva pronto!"+"\033[0m")
