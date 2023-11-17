personas = [
    {
        "sexo": 'M',
        "edad": 15
    },{
        "sexo": 'M',
        "edad": 14
    },
    {
        "sexo": 'M',
        "edad": 11
    },
    {
        "sexo": 'M',
        "edad": 18
    },
    {
        "sexo": 'H',
        "edad": 15
    },
    {
        "sexo": 'H',
        "edad": 24
    },
    {
        "sexo": 'H',
        "edad": 11
    },
    {
        "sexo": 'H',
        "edad": 18
    },
    {
        "sexo": 'H',
        "edad": 17
    },
    {
        "sexo": 'H',
        "edad": 5
    }
]

def getMediaEdad(personas:list)->float:
    sumatorio = 0
    for persona in personas:
        sumatorio += persona['edad']
    
    return sumatorio / len(personas)

def mujeresEntreEdad(personas):
    mujeres = []
    
    for persona in personas:
        mujeres.append(persona) if persona['sexo'] == 'M' and persona['edad'] > 13 and persona['edad'] < 16 else None
        
    return len(mujeres)

def hombresMenores(personas):
    hombres = []
    
    for persona in personas:
        hombres.append(persona) if persona['sexo'] == 'H' and persona['edad'] < 20 else None
        return len(hombres)
    
def mediaPorSexo(personas):
    hombres = []
    mujeres = []
    
    for persona in personas:
        hombres.append(persona) if persona['sexo'] == 'H' else mujeres.append(persona)
    
    sumatorioHombres = 0
    sumatorioMujeres = 0
    
    for hombre in hombres:
        sumatorioHombres += hombre['edad']
    for mujer in mujeres:
        sumatorioMujeres += mujer['edad']     
    
    print(f'la media de edad de los hombres es: {sumatorioHombres/len(hombres)}')
    print(f'la media de edad de las mujeres es: {sumatorioMujeres/len(mujeres)}')
