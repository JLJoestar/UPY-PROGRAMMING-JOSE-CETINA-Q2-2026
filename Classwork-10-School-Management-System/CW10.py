# INPUT & DATA STRUCTURES
# Complete database setup with 6 students, 1 teacher, and 1 coordinator
usuarios = {
    'Chilispin': {'password': '1234', 'rol': 'alumno', 'nombre': 'Chilispin'},
    'IkerSteps': {'password': '1234', 'rol': 'alumno', 'nombre': 'IkerSteps'},
    'Leo': {'password': '1234', 'rol': 'alumno', 'nombre': 'Leo'},
    'PapiArca': {'password': '1234', 'rol': 'alumno', 'nombre': 'PapiArca'},
    'Arma': {'password': '1234', 'rol': 'alumno', 'nombre': 'Arma'},
    'Luka': {'password': '1234', 'rol': 'alumno', 'nombre': 'Luka'},
    'JLJoestar': {'password': '1234', 'rol': 'maestro', 'nombre': 'JLJoestar'},
    'Strazxy': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Strazxy'}
}

materias = ('Matemáticas', 'Programación', 'Inglés')

calificaciones = {
    'Chilispin': {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'IkerSteps': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'Leo': {'Matemáticas': 7.0, 'Programación': 6.5, 'Inglés': 8.0},
    'PapiArca': {'Matemáticas': 8.0, 'Programación': 8.5, 'Inglés': 9.0},
    'Arma': {'Matemáticas': 6.0, 'Programación': 7.5, 'Inglés': 8.0},
    'Luka': {'Matemáticas': 9.5, 'Programación': 10.0, 'Inglés': 9.0}
}

# Login Loop Verification
logged_in = False
usuario_actual = ""

while not logged_in:
    username = input("Usuario: ")
    password = input("Contraseña: ")
    
    if username in usuarios and usuarios[username]['password'] == password:
        logged_in = True
        usuario_actual = username
        print(f"Bienvenido, {usuarios[username]['nombre']} ({usuarios[username]['rol']})\n")
    else:
        print("Credenciales incorrectas. Intente de nuevo.\n")

# PROCESS & OUTPUT BRANCHING BY ROLE
rol = usuarios[usuario_actual]['rol']

if rol == 'alumno':
    # --- STUDENT MENU ---
    print(f"--- Boleta de {usuarios[usuario_actual]['nombre']} ---")
    
    aprobadas = set()
    
    # Print grades looping over the fixed materias tuple
    for materia in materias:
        nota = calificaciones[usuario_actual][materia]
        print(f"{materia}: {nota}")
        if nota >= 8.0:
            aprobadas.add(materia)
            
    # Calculate pendientes using set difference
    todos_las_materias = set(materias)
    pendientes = todos_las_materias.difference(aprobadas)
    
    print(f"Materias aprobadas: {aprobadas}")
    print(f"Materias pendientes: {pendientes}")

elif rol == 'maestro':
    # --- TEACHER MENU ---
    print("--- Lista de Alumnos ---")
    for usr, datos in usuarios.items():
        if datos['rol'] == 'alumno':
            print(f"- {usr}: {datos['nombre']}")
            
    print("")
    alumno_target = input("Alumno (username): ")
    
    if alumno_target in usuarios and usuarios[alumno_target]['rol'] == 'alumno':
        materia_target = input("Materia: ")
        
        if materia_target in materias:
            nueva_nota = float(input("Nueva calificación: "))
            # Overwrite grade in memory
            calificaciones[alumno_target][materia_target] = nueva_nota
            print("Calificación actualizada con éxito.")
        else:
            print("Error: La materia especificada no existe.")
    else:
        print("Error: El usuario no existe o no es un alumno.")

elif rol == 'coordinador':
    # --- COORDINATOR MENU ---
    print("=== REPORTE GENERAL DE COORDINACIÓN (SOLO LECTURA) ===")
    
    print("\n1. Lista de Profesores:")
    for usr, datos in usuarios.items():
        if datos['rol'] == 'maestro':
            print(f"- {datos['nombre']}")
            
    print("\n2. Lista de Asignaturas:")
    for materia in materias:
        print(f"- {materia}")
        
    print("\n3. Reporte de Calificaciones por Estudiante:")
    for usr, materias_notas in calificaciones.items():
        nombre_completo = usuarios[usr]['nombre']
        print(f"\nEstudiante: {nombre_completo} ({usr})")
        for materia in materias:
            print(f"  * {materia}: {materias_notas[materia]}")