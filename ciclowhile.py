controlador = 0

print("****EMPANADAS EL MACHETICO****")
print("1. Agregar un sabor de empanada")
print("2. Ver el sabor de empanada registrado")
print("3. SALIR")

saborEmpanada = ""

while controlador != 3:
    controlador = int(input("Digita una opcion: "))
    if controlador == 1:
        saborEmpanada = str(input("Digite el sabor de empanada: "))
    elif controlador == 2:
        print(f"El sabor de empanada guardado es: {saborEmpanada}")
    elif controlador == 3:
        print("Adios")
    else:
        print("Elige una opcion valida")