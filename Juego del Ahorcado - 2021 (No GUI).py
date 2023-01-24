import random
from os import system

ahorcado = ["""
      ┍━━━┑
      │   │
          │
          │ 
          │
          │
    ┏━━━━━┷━┓""", """
      ┍━━━┑
      │   │
      O   │
          │ 
          │
          │
    ┏━━━━━┷━┓""", """
      ┍━━━┑
      │   │
      O   │
      │   │ 
          │
          │
    ┏━━━━━┷━┓""", """
      ┍━━━┑
      │   │
      O   │
     /│   │ 
          │
          │
    ┏━━━━━┷━┓""", """
      ┍━━━┑
      │   │
      O   │
     /│\  │ 
          │
          │
    ┏━━━━━┷━┓""", """
      ┍━━━┑
      │   │
      O   │
     /│\  │ 
     /    │
          │
    ┏━━━━━┷━┓""", """
      ┍━━━┑
      │   │
      O   │
     /│\  │ 
     / \  │
          │
    ┏━━━━━┷━┓"""]


def generarRandom():
    aleatorio = random.randint(0, 5)
    return aleatorio

def elegirCategoria(aleatorio):
    tema = aleatorio
    
    # Animales
    if tema == 0: 
        palabras = ["PERRO", "GATO", "AVESTRUZ", "CAMALEON", "CEBRA", "CHIMPANCE", "COCODRILO", 
                    "ELEFANTE", "FLAMENCO", "GACELA", "GANSO", "GORILA", "GUEPARDO", "HIENA", "JIRAFA", "LEMUR", 
                    "LEON", "LEOPARDO", "MONO", "NUTRIA", "PALOMA", "PATO", "PELICANO", "PUERCOESPIN", 
                    "RANA", "RATA", "RATON", "RINOCERONTE", "SURICATA", "TORTUGA"]
    # Paises
    elif tema == 1: 
        palabras = ["ALEMANIA", "ARGENTINA", "ARGELIA", "ARMENIA", "AUSTRALIA", "AUSTRIA", "BRASIL", 
                    "BAHAMAS", "BELGICA", "BOLIVIA", "BOSNIA", "BULGARIA", "CANADA", "CHILE", 
                    "CHINA", "COLOMBIA", "COREA DEL NORTE", "COREA DEL SUR", "COSTA RICA", 
                    "CROACIA", "CUBA", "DINAMARCA", "ECUADOR", "EGIPTO", "EL SALVADOR", "ESLOVAQUIA", 
                    "ESPAÑA", "ESTADOS UNIDOS", "FRANCIA", "FINLANDIA", "GRECIA", "GUATEMALA", 
                    "GUYANA", "HAITI", "HONDURAS", "HUNGRIA", "HOLANDA", "INDIA", "INDONESIA", 
                    "IRAK", "IRAN", "IRLANDA", "ISLANDIA", "ISRAEL", "ITALIA", "JAPON", "LIBANO", 
                    "MADAGASCAR", "MALASIA", "MEXICO", "NEPAL", "NICARAGUA", "NIGERIA", "NORUEGA", 
                    "NUEVA ZELANDA", "PARAGUAY", "PERU", "POLONIA", "PORTUGAL", "PUERTO RICO", 
                    "REINO UNIDO", "REPUBLICA DOMINICANA", "RUMANIA", "RUSIA", "SERBIA", "SINGAPUR", 
                    "SIRIA", "SUDAFRICA", "SUECIA", "SUIZA", "TURQUIA", "UCRANIA", "URUGUAY", "VENEZUELA", 
                    "VIETNAM"]
    # Frutas
    elif tema == 2: 
        palabras = ["MANZANA","BANANA", "ANANA", "CIRUELA", "COCO", "DURAZNO", "FRAMBUESA", "MANGO", 
                    "MORA", "MARACUYA", "NARANJA", "POMELO", "SANDIA", "ARANDANO", "CEREZA"]
    # Nombres
    elif tema == 3:
        palabras = ["ALDANA", "ALEXIA", "ALICIA", "ALISON", "AMBAR", "AMELIA", "ANA", "VALERIA", "DANIELA", 
                    "VALENTINA", "ALMA", "LARA", "MIA", "IRENE", "FLORENCIA", "PAULA", "LUNA", "BELEN", 
                    "HUGO", "LUCAS", "MARTIN", "DANIEL", "PABLO", "MATEO", "ALEJANDRO", "LEO", "MANUEL", 
                    "ENZO", "DIEGO", "MARIO", "MARCO", "JAVIER", "MIGUEL", "CARLOS", "JUEAN", "SAMIR", 
                    "JORGE", "GABRIEL", "IVAN", "OSCAR", "MAURO", "CAMILA"]
    # Objetos
    elif tema == 4:
        palabras = ["MESA", "SILLA", "ALMOHADA", "CAMA", "BICICLETA", "MOUSE", "TECLADO", "MONITOR", 
                    "TELEVISOR", "PELOTA", "CAJA", "DADO", "DARDO", "DIARIO", "ESPADA", "ESPONGA", 
                    "FLAUTA", "GORRO", "GUITARRA", "IMPRESORA", "JARRA", "LAPIZ", "MASCARA", "PIANO", 
                    "PINCEL", "RIMEL", "TAMBOR", "VASO", "XILOFONO"]
    # Colores
    else: 
        palabras = ["ROJO", "AZUL", "AMARILLO", "BEIGE", "BLANCO", "CAFE", "CELESTE", "CIAN", "DORADO", 
                    "DURAZNO", "ESMERALDA", "FUCISA", "GRIS", "LIMA", "LAVANDA", "MAGENTA", "MARRON", 
                    "MORADO", "MOSTAZA", "NARANJA", "NEGRO", "OCRE", "PLATEADO", "PURPURA", "ROSA", 
                    "SALMON", "TURQUESA", "VERDE", "VIOLETA"]
    return palabras 

def obtenerCategoria(aleatorio):
    tema = aleatorio
    
    # Animales
    if tema == 0: 
        categoriaNombre = "Animales"
    # Paises
    elif tema == 1: 
        categoriaNombre = "Paises"
    # Frutas
    elif tema == 2: 
        categoriaNombre = "Frutas"
    # Nombres
    elif tema == 3:
        categoriaNombre = "Nombres"
    # Objetos
    elif tema == 4:
        categoriaNombre = "Objetos"
    # Colores
    else: 
        categoriaNombre = "Colores"

    return categoriaNombre

def buscarPalabraAleatoria(listaPalabras):
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]

#Programa Principal
system("cls")
print("\033[1;36m"+"――――――――――――――――――――"+"\033[0m")
print(" JUEGO DEL AHORCADO")
print("\033[1;36m"+"――――――――――――――――――――"+"\033[0m")

letrasIncorrectas = []
oportunidades = 6
etapaAhorcado = 0
tusLetras = ""
aleatorio = generarRandom()
categoria = elegirCategoria(aleatorio)
palabra = buscarPalabraAleatoria(categoria)
categoriaNombre = obtenerCategoria(aleatorio)
longitudPalabra = len(palabra)

print("\033[1;33m"+"Categoria:"+"\033[0m", categoriaNombre)
print("\033[1;33m"+"Letras incorrectas:"+"\033[0m", letrasIncorrectas)


print(ahorcado[0])
print("    ▔▔▔▔▔▔▔▔▔")


while oportunidades > 0:
    incorrectas = 0
    print("    ", end="")
    for letrasPalabra in palabra:
        if letrasPalabra in tusLetras:
            print(letrasPalabra,"", end = "")
        else:
            if letrasPalabra == " ":
                print("  ", end = "")
            else:
                print("▁ ", end = "")
                incorrectas = incorrectas + 1

    if incorrectas == 0:
        print(" ")
        system("cls")

        print("\033[1;36m"+"――――――――――――――――――――"+"\033[0m")
        print(" JUEGO DEL AHORCADO")
        print("\033[1;36m"+"――――――――――――――――――――"+"\033[0m")

        print("\033[1;33m"+"Categoria:"+"\033[0m", categoriaNombre)
        print("\033[1;33m"+"Letras incorrectas:"+"\033[0m", letrasIncorrectas)
        print(ahorcado[etapaAhorcado])
        print("    ▔▔▔▔▔▔▔▔▔")

        print("\033[1;33m"+"La palabra era:"+"\033[0m", palabra)
        print("\033[1;32m"+"¡GANASTE!"+"\033[0m")
        break
    
    print("\n")
    letra = input("Ingrese una letra: ").upper()
    
    tusLetras = tusLetras + letra

    if letra not in palabra:
        oportunidades = oportunidades - 1
        etapaAhorcado = etapaAhorcado + 1
        letrasIncorrectas.append(letra)

    system("cls")

    print("\033[1;36m"+"――――――――――――――――――――"+"\033[0m")
    print(" JUEGO DEL AHORCADO")
    print("\033[1;36m"+"――――――――――――――――――――"+"\033[0m")

    print("\033[1;33m"+"Categoria:"+"\033[0m", categoriaNombre)
    print("\033[1;33m"+"Letras incorrectas:"+"\033[0m", letrasIncorrectas)
    print(ahorcado[etapaAhorcado])
    print("    ▔▔▔▔▔▔▔▔▔")

    if oportunidades == 0:
        print("\033[1;33m"+"La palabra era:"+"\033[0m", palabra)
        print("\033[1;31m"+"¡PERDISTE!"+"\033[0m")
        break