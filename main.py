tareas = {}
estados = ['Pendiente', 'Completada']

def agregar_tarea():
    while True:
                descripcion = input('A continuación, ingresa la descripción de la tarea: ').strip().upper()
                if descripcion != "":
                    break
                else:
                    print("La descripción de la tarea no puede estar vacía. Por favor, intenta otra vez...")
    estado_inicial = estados[0]
    nueva_clave = 1
    while nueva_clave in tareas:
        nueva_clave += 1
    tareas[nueva_clave] = {'descripcion': descripcion, 'estado': estado_inicial}
    return f'La tarea "{descripcion}" se agregó correctamente con estado "{estado_inicial}"!'

def ver_tareas():
    print('A continuación, se muestran todas las tareas registradas: ')
    for clave, tarea in tareas.items():
        print(f'{clave}. Descripción: {tarea["descripcion"]} - Estado: {tarea["estado"]}')

def marcar_tarea_completa():
    tarea_completada = int(input('Ingresa el número de la tarea completada: '))
    if tarea_completada in tareas:
        tareas[tarea_completada]['estado'] = estados[1]
        return f'Se modificó el estado de la tarea "{tareas[tarea_completada]['descripcion']}" a "{estados[1]}"!'
    else:
        return "La tarea no existe"

def eliminar_tarea():
    tarea_eliminada = int(input('Ingresa el número de la tarea que quieres eliminar: '))
    if tarea_eliminada in tareas:
        tareas.pop(tarea_eliminada)
        print('Se ha eliminado la tarea exitosamente!')

def menu():
    print('Bienvenido al sistema!')

    while True:
        print('''\n--- Gestor de Tareas ---
          1. Agregar tarea
          2. Ver tareas
          3. Marcar tarea como completada
          4. Eliminar tarea
          5. Salir''')
        eleccion = input('Ingresa el número de tu opción: ')
        match eleccion:
            case '1':
                print(agregar_tarea())
            case '2':
                ver_tareas()
            case '3':
                print(marcar_tarea_completa())
            case '4':
                eliminar_tarea()
            case '5':
                print('Estás saliendo, gracias por usar el sistema!')
                break
            case _:
                print('Opción no válida, intente nuevamente')

menu()
