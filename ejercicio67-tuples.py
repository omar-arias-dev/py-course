# list
list_values = ["Ford", "Mazda"]

# tuple
tuple_values = ("Ford", "Mazda")
print(tuple_values)

tuple_to_list = list(tuple_values)
tuple_to_list.append("BMW")
tuple_to_list.append("Ferrari")
print("tuple_to_list", tuple_to_list)

list_to_tuple = tuple(tuple_to_list)
print("list_to_tuple", list_to_tuple)


(v1, v2, *v3) = tuple_to_list # El signo * es un tope, y a partir de ahi se hara un arreglo. Si la tupla tiene mas valor de los que se desestrucuran, provocará un error (tuple_to_list tiene 3 valores).
print("values", v1, v2, v3)


numbers = (1, 2, 3)
new_tuple = numbers * 3 # Multiplica por 3 la cantidad de valores, no el valor en si. Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(new_tuple)