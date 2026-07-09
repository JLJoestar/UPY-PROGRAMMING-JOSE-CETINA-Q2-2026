import math


# INPUT

a = input("Write the left endpoint of the interval: ")
b = input("Write the right endpoint of the interval: ")
f_x = input("Write the function to integrate: ")
method = input("Write the integration method (LRM/RRM/MRM/TRAP): ")


# PROCESS

try:
    if "pi" in a:
        a = math.pi
    else:
        a = float(a)
        
    if "pi" in b:
        b = math.pi
    else:
        b = float(b)
        
    n = 1000
    h = (b - a) / n
    area = 0.0
    shift = 0
    constant = 0

    if method == "TRAP":
        f_0 = f_x.replace("x", f"({str(a)})")
        area += (h / 2) * eval(f_0)
        
        for i in range(1, n):
            xi = a + i * h
            f_xi = f_x.replace("x", f"({str(xi)})")
            area += (h / 2) * 2 * eval(f_xi)
            
        f_xn = f_x.replace("x", f"({str(b)})")
        area += (h / 2) * eval(f_xn)
        
    else:
        if method == "RRM":
            shift = 1
            
        if method == "MRM":
            constant = h / 2
            
        for i in range(shift, n + shift):
            xi = a + i * h
            height = f_x.replace("x", f"({str(xi + constant)})")
            area += h * eval(height)

except ZeroDivisionError:
    print("\n[Math Error]: Math domain error. Division by zero detected during integration loops.")
    area = None

except ValueError as e:
    print(f"\n[Math Error]: Invalid mathematical domain encounter: {e}")
    area = None

except (SyntaxError, NameError):
    print("\n[Syntax Error]: The mathematical function syntax is invalid or contains unrecognised variables.")
    area = None


# OUTPUT

if area is not None:
    print(f"The integration of {f_x} is {area}")
else:
    print("Execution aborted due to mathematical errors.")