from object import Dron

modelo = input("Ingrese el modelo del dron: ")
alturaMax = float(input("Ingrese la altura máxima que puede volar el dron: "))
bateria = int(input("Carga de la batería (0-100): "))
camara = input("¿Tiene cámara? (si/no): ").lower() #.lower para que sin importar como se escriba si o no se ejecute el programa sin problemas.
if camara == "si":
    tipo = "con cámara"
else:
    tipo = "sin cámara"

dron = Dron(modelo, alturaMax, bateria, tipo) #Objeto creado a partir de la clase


while True:
    print("MENÚ DEL DRON")
    print("1. Ver datos del dron")
    print("2. Volar")
    print("3. Sector para Cargar batería")
    print("4. Activar la cámara")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print(dron)
    elif opcion == "2":
        distancia = int(input("¿Cuántos metros querés volar? "))
        print(dron.volar(distancia))
    elif opcion == "3":
        cargar = int(input("¿Cuánta batería querés cargar? "))
        print(dron.cargarBateria(cargar))
    elif opcion == "4":
        print(dron.activarCamara())
    elif opcion == "5":
        print("¡Chau!")
        break
    else:
        print("Opción inválida. Intentá otra vez.")
