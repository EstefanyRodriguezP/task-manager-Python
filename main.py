""" 
Objetivo
En esta actividad, desarrollarás una aplicación de línea de comandos que permitirá gestionar tareas de manera sencilla. Con este proyecto, aplicarás conocimientos fundamentales de Python, incluyendo el uso de estructuras de datos, funciones, control de flujo y módulos.

Contexto
Imagina que eres un desarrollador que necesita una herramienta ligera para organizar sus pendientes diarios desde la terminal. No quieres depender de aplicaciones externas ni de herramientas visuales avanzadas, sino algo simple y funcional que puedas ejecutar en cualquier sistema con Python instalado.
Para ello, construirás una aplicación que permita al usuario agregar tareas, verlas, marcarlas como completadas y eliminarlas. Además, las tareas deberán guardarse en un archivo para que no se pierdan cuando se cierre el programa.

Requisitos del Proyecto
1. Menú interactivo
- La aplicación debe mostrar un menú en la consola con opciones numéricas para que el usuario pueda elegir qué acción realizar.

2. Operaciones básicas:
- Agregar una nueva tarea.
- Listar todas las tareas con un indicador de estado (Pendiente o Completada).
- Marcar una tarea como completada.
- Eliminar una tarea.
- Salir del programa.

3. Estructuras de datos
- Utilizar diccionarios para representar cada tarea.
- Usar una lista para almacenar todas las tareas.

4. Funciones
- Dividir el código en funciones reutilizables para cada operación.

5. Validaciones y manejo de errores
- Evitar errores al ingresar opciones no válidas.
- Manejar archivos de manera segura para evitar pérdidas de datos.

Ejemplo de Uso
Cuando el usuario ejecute el programa, verá un menú como el siguiente:
--- Gestor de Tareas ---
1. Agregar tarea
2. Ver tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
Elige una opción: 
Al seleccionar una opción se ejecuta el código detrás de esa opción volvemos al menu hasta que el usuario seleccione Salir. """

tareas = []

def agregar_tarea():
    return
agregar_tarea()

def ver_tareas():
    return
ver_tareas()

def marcar_tarea_completa():
    return
marcar_tarea_completa()

def eliminar_tarea():
    return
eliminar_tarea()


def menu():
    print('Bienvenido al sistema!')

    while True:
        print('''--- Gestor de Tareas ---
          1. Agregar tarea
          2. Ver tareas
          3. Marcar tarea como completada
          4. Eliminar tarea
          5. Salir''')
        eleccion = input('Ingresa el número de tu opción: ')
        match eleccion:
            case '1':
                agregar_tarea()
            case '2':
                ver_tareas()
            case '3':
                marcar_tarea_completa()
            case '4':
                eliminar_tarea()
            case '5':
                print('Estás saliendo, gracias por usar el sistema!')
                break
            case _:
                print('Opción no válida, intente nuevamente')

menu()


# abrir el archivo:
# si archivo "tareas.txt" existe se abre, si no existe se crea
""" with open('tareas.txt', w) as f:
    f.write('Hola, eliminé el contenido anterior')

# abrir y leer el archivo después de sobreescribirlo
with open('tareas.txt', w) as f:
    print(f.read()) """