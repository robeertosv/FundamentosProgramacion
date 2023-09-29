"""
Los profesores solemos utilizar dos decimales cuando trabajamos con las
notas parciales de un alumno, pero en las actas se desea calificar con puntos
enteros o medios (es decir: 0 / 0.5 / 1 / 1.5 /… / 9.5 /10). 

Combinando operaciones y funciones enteras y en coma flotante:

Encuentra una fórmula general que convierta una nota con dos decimales a la calificación correspondiente en el acta, 
e implementa una función que la utilice para convertir cualquier nota.

Pista (aunque te parezca obvio, esta es la pista): 0.5 (que es lo que quiero conseguir) es la mitad de 1.

Tu propuesta debe funcionar para todos los casos de prueba que adjuntamos.
Nota original   En acta
8,89            9,0
8,50            8,5
8,45            8,5
8,24            8,0

Error frecuente: considerar que necesitas una instrucción if. No es necesario
utilizarlo y te pedimos de hecho que no lo utilices.

"""

def notaARedondear(nota: float) -> float:
    
    nota *= 2
    
    parteInt = int(nota)
    
    decimales = nota - parteInt

    suma = int(decimales + 0.5)
    
    return (parteInt + suma)/2

print(notaARedondear(8.89))
print(notaARedondear(8.50))
print(notaARedondear(8.45))
print(notaARedondear(8.24))
