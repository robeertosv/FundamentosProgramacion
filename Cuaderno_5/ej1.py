datos = [
    {
        "nombre": "Roberto",
        "edad": 17,
        "sexo": "H"
    },
    {
        "nombre": "Pepe",
        "edad": 18,
        "sexo": "H"
    },
    {
        "nombre": "Luis",
        "edad": 19,
        "sexo": "H"
    }
]

def getData():
    persona = input("De qué persona quieres buscar datos?\n")
    dato = input(f"Qué quieres saber de {persona}\n")
    
    for i in range(len(datos)):
        if(datos[i]["nombre"] == persona):
            print(f"{dato} de {persona} es {datos[i][dato]}")    
            
def UI():
    for i in datos:
        print(f"Nombre: {i['nombre']}, edad: {i['edad']}")


UI()
getData()