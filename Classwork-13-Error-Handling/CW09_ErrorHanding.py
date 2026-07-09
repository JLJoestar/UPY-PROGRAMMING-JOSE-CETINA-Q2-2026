
# INPUT

check = True
while check:
    try:
        verbo = input("Ingrese un verbo en infinitivo (ej. hablar, comer, vivir): ").strip().lower()
        
        if len(verbo) < 3:
            raise ValueError("La palabra es demasiado corta para ser un verbo válido.")
            
        if not verbo.isalpha():
            raise ValueError("El verbo solo debe contener letras (sin números ni símbolos).")
            
        ending = verbo[-2:]
        
        valid_endings = ['ar', 'er', 'ir']
        if ending not in valid_endings:
            raise KeyError(f"La terminación '-{ending}' no es un infinitivo válido en español.")
            
        check = False
        
    except ValueError as e:
        print(f" [ValueError]: {e} Intente de nuevo.\n")
    except KeyError as e:
        print(f" [KeyError]: {e} Recuerde usar verbos terminados en -ar, -er o -ir. Intente de nuevo.\n")

# PROCESS

pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

stem = verbo[:-2]
endings_list = terminaciones[ending]

# OUTPUT
print(f"\n--- Conjugación del verbo: {verbo} ---")
for index, pronombre in enumerate(pronombres):
    terminacion = endings_list[index]
    print(f"{pronombre} {stem}{terminacion}")