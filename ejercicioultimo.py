opcion = 0
def mostrar_menu():
    print("********************** MENU PRINCIPAL **********************")
    print("1.- agregar reserva")
    print("2.- buscar reserva")
    print("3.- eliminar reserva")
    print("4.- confirmar reserva")
    print("5.- mostrar reserva")
    print("6.- salir")
    print("*************************************************************")
def seleccionar_opcion():
    while True:
        try:
            op = int(input("seleccione una opcion:  "))
            if op <= 0 or op > 6:
                raise ValueError
            else:
                return op 
        except ValueError:
            print("debe ser un numero entre 1 y el 6")

def agregar_reserva(lista_r):
    nombre_completo = input("ingrese el nombre completo:    ")
    num_habitacion = input("ingrese el numero de habitacion:")
    cant_noches = input("ingrese la cantidad de noches a hospedar:  ")
def validar_nombre(nombre):
    return nombre.strip().upper() != ""
def validar_habitacion(hab):
    return hab.strip().upper() != ""