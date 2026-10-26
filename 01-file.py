my_file = open("test.txt")
# print(my_file.read())
# print(my_file.read())
# print(my_file.read())

# seek   resetea el archivo y vuelve a leer desde el indice indicado entre parentesis
# my_file.seek(4)
# print(my_file.read())

# readline leer por linea
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

# readlines leer todas las lineas restantes
print(my_file.readlines())


my_file.close()
