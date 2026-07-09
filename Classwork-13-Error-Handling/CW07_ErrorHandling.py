class DigitoVerificadorError(Exception):
    pass


# INPUT

check = True
while check:
    try:
        rol = input("Ingrese el rol: ")
        
        # Validación de que exista el guion antes de separar
        if "-" not in rol:
            raise ValueError("El rol debe contener un guion '-'")
            
        rol_sin_digito, digito = rol.split("-")
        
        # Validación de caracteres numéricos
        if not rol_sin_digito.isnumeric() or not digito.isnumeric():
            raise ValueError("El rol o el dígito verificador contienen caracteres no numéricos")
            
        check = False
    except ValueError as e:
        print(f"Rol incorrecto: {e}")


# PROCESS

invertido = rol_sin_digito[::-1]

secuencia = [2, 3, 4, 5, 6, 7]
suma = 0

for index in range(len(invertido)):
    multiplicando = secuencia[index % 6]
    numero = int(invertido[index:index+1])
    suma += numero * multiplicando
    
total = suma % 11

verificador = 11 - total

# Validación del dígito verificador usando la excepción personalizada
try:
    if verificador != int(digito):
        raise DigitoVerificadorError(f"El digito verificado no coincide, calculado: {verificador}")
except DigitoVerificadorError as e:
    print(e)


# OUTPUT
else:
    print(f"{rol_sin_digito}-{verificador}")