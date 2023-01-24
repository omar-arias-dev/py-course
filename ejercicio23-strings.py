a = """TITULO
parrafo"""

print(a)


phrase = "Hola, mundo"
print("Hola, mundo")

print( "[0:2]", phrase[0:2] ) # Start at position 0 and take two values

print( "[:4]", phrase[:4] ) # Start in null and take four values

print( "[2:]", phrase[2:] ) # Start at position 2 and take all values


# set phrase in uppercase
print(phrase.upper())


# set phrase in lowercase
upper = phrase.upper()
print(upper.lower())


# remove blank spaces
phrase_with_spaces = " " + phrase + " "
print(phrase_with_spaces)
print(phrase_with_spaces.strip()) # Remove at start and end


# replace letters and words
print(phrase.replace("Hola", "Hey"))


# Split string
print(phrase.split(",")[1])


# Insert code in string (format)
cantidad = 3
id = 10
precio = 59.90
total_venta = "El producto vale {}. Son {} productos. El numero de control del producto es {}"

print(total_venta.format(precio, cantidad, id))


# string length
print("Digite una frase")
phrase = input()
print(len(phrase))