from PIL import Image

config = {}

archivo = open("config.txt", 'r')

for linea in archivo:
    clave, valor = linea.strip().split('=')
    config[clave] = float(valor) if "." in valor else int(valor)
archivo.close()

#print(config)
with open("clase.csv", 'r') as data:
    #data.readline() #quitar encabezados
    #for linea in data:
    datos = data.readlines()
    
ancho, alto, max_iter = config["alto"], config["ancho"], config["max_iter"]
    
img = Image.new( 'HSV', (alto, ancho))

#quitar encabezados
encabezados = datos.pop(0)

#print(encabezados)

for dato in datos:
    #fila, columna, interaciones = dato.strip().split(",")
    fila, columna, iteraciones = map(int, dato.strip().split(","))
    brillo = 40 if ( iteraciones == max_iter) else int ((iteraciones / max_iter) * 255)
    #putpixel necesita tuplas, la orimera indica la posicion y la segunda el color
    img.putpixel((columna,fila), (brillo, 255, 255))
    
img_rgb = img.convert('RGB')
img_rgb.save("mandelbrot.clase.png")

print("DONE")
    
        