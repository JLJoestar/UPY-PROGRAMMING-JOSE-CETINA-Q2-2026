# INPUT
rol_str = input("Enter the student ID (rol) without hyphen or verification digit: ")

# PROCESS
total_sum = 0
multiplier = 2
length_of_rol = len(rol_str)
for i in range(length_of_rol - 1, -1, -1):
    character = rol_str[i]
    digit = int(character)
    
    total_sum += digit * multiplier
    
    multiplier += 1
    if multiplier > 7:
        multiplier = 2

remainder = total_sum % 11
result = 11 - remainder

if result == 11:
    dv = "0"
elif result == 10:
    dv = "K"
else:
    dv = str(result)

# OUTPUT
print(f"The full student ID with verification digit is: {rol_str}-{dv}")