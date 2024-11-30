# main.py

# Sistema básico de gestión de tareas

def mostrar_menu():
    print("\n--- Gestión de Tareas ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Salir")

def ver_tareas(tareas):
    if not tareas:
        print("\nNo hay tareas registradas.")
    else:
        print("\nTareas:")
        for i, tarea in enumerate(tareas):
            estado = "✅" if tarea["completada"] else "❌"
            print(f"{i + 1}. {tarea['nombre']} - {estado}")

def agregar_tarea(tareas):
    nombre = input("\nIngresa el nombre de la nueva tarea: ")
    tareas.append({"nombre": nombre, "completada": False})
    print(f"Tarea '{nombre}' agregada correctamente.")

def completar_tarea(tareas):
    if not tareas:
        print("\nNo hay tareas para completar.")
        return
    try:
        ver_tareas(tareas)
        num = int(input("\nNúmero de la tarea a completar: "))
        if 1 <= num <= len(tareas):
            tareas[num - 1]["completada"] = True
            print(f"Tarea '{tareas[num - 1]['nombre']}' marcada como completada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")
        if opcion == "1":
            ver_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
