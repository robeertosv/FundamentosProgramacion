def pyramid(rows:int):
    for i in range(rows):
        espacios = rows - i -1
        asteriscos = 1 + i*2
        print(" " * espacios + "*"*asteriscos)

pyramid(10)