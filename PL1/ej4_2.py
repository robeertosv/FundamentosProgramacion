for i in range(10):
    print('- '*i)

espacios = 0
cantidad = 10
print()
print()
print()
for i in range(10):
    print(' ' * espacios, end="")
    print("& "* cantidad, end="")
    print(' ' * espacios, end="")
    print()
    espacios += 1
    cantidad = cantidad -1