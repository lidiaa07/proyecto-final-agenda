import csv
#Hecho por Lidia
# Función para leer los contactos desde el archivo CSV
def leer_contactos(nombre_archivo):
    contactos = []
    try:
        with open(nombre_archivo, mode='r', newline='') as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Omitir la cabecera
            for fila in lector:
                contactos.append(fila)
    except FileNotFoundError:
        print("El archivo no existe. Se creará uno nuevo.")
    return contactos

# Función para escribir los contactos en el archivo CSV
# Hecho por Lidia
def guardar_contactos(nombre_archivo, contactos):
    with open(nombre_archivo, mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nombre", "Telefono"])  # Cabecera
        escritor.writerows(contactos)

# Función para agregar un nuevo contacto
# Hecho por Luca
def agregar_contacto(contactos, nombre, telefono):
    contactos.append([nombre, telefono])
    print(f"Contacto {nombre} agregado.")

# Función para mostrar todos los contactos
# Hecho por Alan
def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos en la agenda.")
        return
    for contacto in contactos:
        print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}")

# Función para editar un contactoÇ
# Hecho por Luca
def editar_contacto(contactos, nombre, nuevo_telefono):
    for contacto in contactos:
        if contacto[0] == nombre:
            contacto[1] = nuevo_telefono
            print(f"Teléfono de {nombre} actualizado a {nuevo_telefono}.")
            return
    print(f"No se encontró el contacto {nombre}.")

# Función para la eliminación de un contacto
# Hecho por Alan y Luca
def eliminar_contacto(contactos, nombre):
    for contacto in contactos:
        if contacto[0] == nombre:
            contactos.remove(contacto)
            print(f"Contacto {nombre} eliminado.")
            return
    print(f"No se encontró el contacto {nombre}.")

# Función principal para la gestión de la agenda 
# Hecho por Luca
def gestionar_agenda():
    nombre_archivo = "agenda.csv"
    contactos = leer_contactos(nombre_archivo)

    while True:
        print("\nAgenda de Teléfonos:")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre del contacto: ")
            telefono = input("Introduce el teléfono del contacto: ")
            agregar_contacto(contactos, nombre, telefono)

        elif opcion == "2":
            mostrar_contactos(contactos)

        elif opcion == "3":
            nombre = input("Introduce el nombre del contacto a editar: ")
            nuevo_telefono = input("Introduce el nuevo teléfono: ")
            editar_contacto(contactos, nombre, nuevo_telefono)

        elif opcion == "4":
            nombre = input("Introduce el nombre del contacto a eliminar: ")
            eliminar_contacto(contactos, nombre)

        elif opcion == "5":
            guardar_contactos(nombre_archivo, contactos)
            print("Agenda guardada. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    gestionar_agenda()