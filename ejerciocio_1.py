# 1. crear funciones
# 2. crear menú
# 3. cargar alumnos
# 4. mostrar alumnos
# 5. calcular promedio
# 6. informar aprobados y desaprobados

alumnos = []
def cargar_alumno(alumnos):
    """Añade un nuevo alumno a la lista"""
    nombre = input("Ingrese nombre del alumno: ")

    
    alumnos.append({
        "nombre": nombre,
        "notas": []
    })
    print(f"Alumno {nombre} cargado exitosamente.\n")

def cargar_nota(alumnos):
    """Carga una nota para un alumno existente"""
    if not alumnos:
        print("No hay alumnos cargados.\n")
        return
    
    nombre = input("Ingrese nombre del alumno: ")
    
    nota = float(input("Ingrese la nota (0-10): "))
    if 0 <= nota <= 10:
        for alumno in alumnos:
            if alumno["nombre"] == nombre:
                alumno["notas"].append(nota)
                print(f"Nota {nota} cargada.\n")
                break
        else:
            print(f"Alumno {nombre} no encontrado.\n")
    else:
        print("La nota debe estar entre 0 y 10.\n")
    return
    

def mostrar_alumnos(alumnos):
    print(alumnos)
    return

def mostrar_promedios(alumnos):
    """Muestra el promedio de cada alumno"""
    if not alumnos:
        print("No hay alumnos cargados.\n")
        return
    
    print("===PROMEDIOS===")
    for alumno in alumnos:
        if alumno["notas"]:
            promedio = sum(alumno["notas"]) / len(alumno["notas"])
            print(f"{alumno['nombre']}: {promedio:.2f}")
        else:
            print(f"{alumno['nombre']}: Sin notas")
    return

def aprobados_desaprobados(alumnos):
    if not alumnos:
        print("No hay alumnos cargados.\n")
        return
    desaprobados=[]
    aprobados=[]
    for alumno in alumnos:
        if alumno["notas"]:
            promedio = sum(alumno["notas"]) / len(alumno["notas"])
            if promedio >= 6:
                aprobados.append(alumno["nombre"])
            else:
                desaprobados.append(alumno["nombre"])
        else:
            print(f"{alumno['nombre']}: Sin notas")
    print()


while True:
    print('''
    ===MENU===
    1-cargar alumno
    2-mostrar alumnos cargados y su nota
    3-cargar nota
    4-mostrar promedios 
    5-informar aprobados y desaprobados
    6-salir
    ''')
    opcion=input("ingrese una opcion: ")
    
    if opcion=="1":
        cargar_alumno(alumnos)
    elif opcion=="2":
        mostrar_alumnos(alumnos)
    elif opcion=="3":
        cargar_nota(alumnos)
    elif opcion=="4":
        mostrar_promedios(alumnos)
    elif opcion=="5":
        aprobados_desaprobados(alumnos)
    elif opcion=="6":
        break
