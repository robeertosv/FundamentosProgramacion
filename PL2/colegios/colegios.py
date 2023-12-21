#Sedes es un diccionario que tiene como claves las ciudades y como valores una lista con los nombres de los colegios de esa ciudad.
sedes = {
    'Madrid': ['Santo Domingo', 'Buen Amor', 'Virgen de Covadonga'],
    'Burgos': ['El Cid Campeador', 'Infanta Doña Sol', 'Merindades', 'Río Duero']
}

#Colegios es una lista de diccionarios, cada diccionario representa un colegio y tiene como claves 'nombre', 'ciudad' y 'puntuaciones'.
colegios = [
    {
        'nombre': 'Santo Domingo',
        'ciudad': 'Madrid',
        'puntuaciones': [60, 65, 30]
    },
    {
        'nombre': 'Infanta Doña Sol',
        'ciudad': 'Soria',
        'puntuaciones': [27, 40, 20]
    },
    {
        'nombre': 'El Cid Campeador',
        'ciudad': 'Burgos',
        'puntuaciones': [40, 35, 35]
    },
    {
        'nombre': 'Buen Amor',
        'ciudad': 'Toledo',
        'puntuaciones': [49, 50, 25] 
    },
    {
        'nombre': 'Virgen de Covadonga',
        'ciudad': 'Madrid',
        'puntuaciones': [55, 30, 25]
    },
    {
        'nombre': 'Merindades',
        'ciudad': 'Burgos',
        'puntuaciones': [48, 33, 30]
    },
    {
        'nombre': 'Río Duero',
        'ciudad': 'Burgos',
        'puntuaciones': [40, 30, 15]
    }
]

"""
1. Devolver la sede donde menos colegios hayan participado y cuántos colegios participaron en dicha sede.
Basándonos en el ejemplo de inicialización que se proporciona al comienzo de este enunciado, se muestra
a continuación una posible llamada a esta función, indicando el valor que devolvería en cursiva:
print(sede_menos_colegios(sedes))
('Madrid', 3)
"""

def sede_menos_colegios(sedes:dict)->tuple:
    m = 999999999999999
    r = ['', 0]
    for sede in sedes:
        if len(sedes[sede]) < m:
            m = len(sedes[sede])
            r[0] = sede
            r[1] = len(sedes[sede])
    return r[0], r[1]
            
            

#print(sede_menos_colegios(sedes))

"""
Ordenar alfabéticamente la lista de colegios por la ciudad en la que están.
Basándonos en el ejemplo de inicialización que se proporciona al comienzo de este enunciado, se muestra
a continuación una posible llamada a esta función, indicando el valor que devolvería en cursiva:
"""

def ordenar_por_ciudad(colegios):
    n = len(colegios)-1
    
    for i in range(n):
        for j in range(n-1):
            if colegios[j+1]['ciudad'] < colegios[j]['ciudad']:
                colegios[j+1], colegios[j] = colegios[j], colegios[j+1]
    return colegios

#print(ordenar_por_ciudad(colegios))