# relative path
with open("fileFolder/relative.txt", mode="r") as my_file:
    print(my_file.readlines())

# absolute path
with open(
    "D:/Programacion/Cursos-DevTalles/Python/Archivos/archivo.txt", mode="r"
) as my_file:
    print(my_file.readlines())
