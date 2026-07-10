class DigitoVerificadorError(Exception):
    pass


# INPUT

check = True
while check:
    try:
        rol = input("Ingrese el rol: ")
        if "-" not in rol:
            raise ValueError("No tiene el formato XXXXXXXXX-X")
        if rol.count("-") != 1:
            raise ValueError("No tiene el formato XXXXXXXXX-X")
            
        rol_sin_digito, digito = rol.split("-")
        
        if not rol_sin_digito.isnumeric() or not digito.isnumeric():
            raise ValueError("El rol o el dígito verificador contienen caracteres no numéricos")
            
        check = False
    except ValueError as e:
        print(f"Rol inválido: {e}")
    except ValueError as e:
        print(f"Rol inválido: {e}")


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

try:
    if verificador != int(digito):
        raise DigitoVerificadorError(f"El digito verificado no coincide, calculado: {verificador}")
except DigitoVerificadorError as e:
    print(e)


# OUTPUT
else:
    print(f"{rol_sin_digito}-{verificador}")