from tasks import TaskManager

def main():
    task_manager = TaskManager()

    while True:
        print("\n==== To-Do List ====")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")

        choice = input("Ingrese el número de la opción deseada: ")

        if choice == "1":
            task = input("Ingrese la tarea: ")
            task_manager.add_task(task)
            print("Tarea agregada exitosamente.")
        elif choice == "2":
            task_manager.show_tasks()
        elif choice == "3":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
