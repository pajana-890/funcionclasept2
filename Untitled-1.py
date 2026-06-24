import ejercicioultimo as p
#import tiene q estar al inicio del archivo
#codigo principal
lista_resevas = []
opcion = 0
while opcion != 6:
    #mostrar menu
    p.mostrar_menu()
    #preguntar al usuario por la opcion del menu
    opcion = p.seleccionar_opcion()
    #validamos la opcion seleccionada
    if opcion == 1:
        #llamar a la funcion que agrega las reservas
        p.agregar_reserva(lista_resevas)
    elif opcion == 2:
        #solicitar el nombre a buscar
        nombre = input("ingrese el nombre del huesped a buscar:")
        pos = p.buscar_reserva(lista_resevas, nombre)
        #validar si lo encontro o no
        if pos != -1:
            #mostrar los datos
            print("******** reserva **¨****")
            print(f"nombre del huesped: {lista_resevas [pos] ["huesped"]}")
            print(f"numero de la habitacion: {lista_resevas [pos] ["habitacion"]}")
            print(f"cantidad de noches: {lista_resevas [pos] ["noches"]}")
            estado = "confirmada" if lista_resevas[pos]["confirmada"] else "pendiente"
            print(f"estado: {estado}")
            print("**********************")
        else: 
            print(f"el huesped '{nombre}' no ha sido encontrado")
    elif opcion == 3:
        #solicitar el nombre a buscar
        nombre = input("ingrese el nombre del huesped a buscar:")
        pos = p.buscar_reserva(lista_resevas, nombre)
        #validar si lo encontro o no
        if pos != -1:
            #elimino el elemento de la lista
            lista_resevas.pop(pos)
            print("reserva eliminada")
        else: 
            print(f"el huesped '{nombre}' no ha sido encontrado")

    elif opcion == 4:
        #llamar a la funcion que actualiza la confirmada
        p.confirmar_reserva(lista_resevas)
        print("reservas actualizadas")
    elif opcion == 5:
        p.confirmar_reserva(lista_resevas)
        p.mostrar_reserva(lista_resevas)
    elif opcion == 6:
        print("gracias por usar el sistema")
    