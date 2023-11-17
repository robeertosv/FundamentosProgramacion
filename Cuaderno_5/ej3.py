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

def masJoven(personas):
    hombres = []
    mujeres = []
    
    for persona in personas:
        hombres.append(persona) if persona['sexo'] == 'H' else mujeres.append(persona)
    
    minEdadH = 10000
    minEdadM = 10000
    for hombre in hombres:
        if(hombre['edad'] < minEdadH):
            minEdadH = hombre['edad']
    
    for mujer in mujeres:
        if(mujer['edad'] < minEdadM):
            minEdadM = mujer['edad']
    
    print(f"El hombre más pequeño tiene {minEdadH} años, la mujer más pequeña tiene {minEdadM} años")

masJoven(personas)