classify = lambda a,b,c: "Equilatero" if a==b and b==c else "Isosceles" if (a==b or a==c) and (a!=c or a!=b) else "Escaleno" if a!= b and b!=c else "Error"
print(classify(2,2,2))