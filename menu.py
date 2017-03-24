import Menu2 as m
### Menu de Renfe
miestacion = "Donostia"
mizona = 1
opc = 0

def menu():
    print("Bienvenido a Renfe")
    print("1.- Ida\t")
    print("2.- Ida-vuelta\t")
    print("3.- mensual")
    opc = input("Elija su opcion:")

    if opc == 1:
        ida()
    elif opc == 2:
        idavuelta()
    elif opc == 3:
        mensual()
    else:
        print("Introduzca un dato correcto")


def ida():
    destino = input("Elija su destino:")
    destino.title()    
    zona = input("Elija su zona:")
    for z, p in m.zonas.items():
        for d in p:
            if d == destino:
                 zona = z
            break
    m.precios[opc][abs(zona-mizona)]

def idavuelta():
    destino = input("Elija su destino:")
    destino.title()    
    zona = input("Elija su zona:")
    for z, p in m.zonas.items():
        for d in p:
            if d == destino:
                 zona = z
            break
    m.precios[opc][abs(zona-mizona)]

def mensual():
    print("Bono mensual")
      
       


   
    



