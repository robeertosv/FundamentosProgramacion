"""
El enunciado propuesto es básicamente una especie de JSON

El esquema de este "JSON" es que cada usuario es un diccionario tal que:
        - posts es un array de tuplas, (id, contenido_del_post)
        - likes es un array de tuplas, (username, id_del_post)
"""
red_social = {
    'user0': {
        'posts': [(0, 'Este es un post sobre: coches naturaleza motos cocina'), (1, 'Este es un post sobre: motos videojuegos coches'), (2, 'Este es un post sobre: motos coches cocina'), (3, 'Este es un post sobre: naturaleza cocina videojuegos motos coches'), (4, 'Este es un post sobre: naturaleza videojuegos')],
        'likes': [('user1', 0), ('user1', 1)]
    },
    'user1': {
        'posts': [(0, 'Este es un post sobre: coches naturaleza videojuegos motos cocina'), (1, 'Este es un post sobre: videojuegos cocina coches motos'), (2, 'Este es un post sobre: motos videojuegos coches cocina'), (3, 'Este es un post sobre: cocina coches naturaleza videojuegos motos'), (4, 'Este es un post sobre: coches motos')],
        'likes': []
    },
    'user2': {
        'posts': [(0, 'Este es un post sobre: motos videojuegos naturaleza'), (1, 'Este es un post sobre: videojuegos naturaleza motos'), (2, 'Este es un post sobre: videojuegos motos coches'), (3, 'Este es un post sobre: motos videojuegos coches cocina'), (4, 'Este es un post sobre: videojuegos coches')],
        'likes': [('user1', 0), ('user2', 0), ('user0', 1), ('user0', 0)]
    }
}

# Incluir un like
def incluir_like(red_social, usuario1: str, usuario2:str, post: int) -> bool:
    """usuario1 es el emisor del like y el usuario2 es el receptor del like"""
    
    """Incluye un like al post de un usuario, comprobando que existe.
    Devuelve false si (a) no existía el post indicado,
    o (b) no existía el usuario, o (c) ya había un like de ese usuario a ese post.
    NOTA: Asumimos que los posts nunca se borran, y que el número de
    post para un usuario es consecutivo, empezando en cero.
    """
    
    likesDados = red_social[usuario1]['likes'] #Array
    posts = None
    
    existeElPerfil = False
    existeElPost = False
    tieneLike = None
    status = None
    
    i = 0
    j = 0
    
    #Comprobar si existe el usuario
    if usuario2 in red_social:
        existeElPerfil = True
        posts = red_social[usuario2]['posts'] #Array        
        
        #Comprobar si existe el post
        while not existeElPost and i < len(posts):
            if posts[i][0] == post:
                existeElPost = True
            i+=1
    
        #Comprobar si ya se le dió like
    
        while tieneLike and j < len(likesDados):
            if likesDados[j][0] == usuario2 and likesDados[j][1] == post:
                tieneLike = True
            else:
                tieneLike = False
    
    if existeElPerfil and existeElPost and not tieneLike:
        status = True
        likesDados.append((usuario2, post))
    else:
        status = False
    
    return status

#print(incluir_like(red_social, "user0", "user1", 3))
#print(incluir_like(red_social, "user0", "user20", 0))

def obtener_post_mas_popular(red_social)->(str, int, int):
    """Devuelve una tupla: (usuario_con_el_post_mas_popular, id_de_ese_post, numero_de_likes)"""
    
    #Lista con todos los likes que se han dado
    posts = [] # ('user_id', post_id, cantidad_likes)
    likes = [] # ('user_id', liked_post_id)
    
    postLikes = {} #En el que las claves son los posts, y los valores son los likes
    
    for user in red_social:
        for post in red_social[user]['posts']:
            posts.append((user, post[0]))
        
        for like in red_social[user]['likes']:
            likes.append(like)
    
    for post in posts:
        postLikes.setdefault(post, 0)
    
    for like in likes:
        #Sumar un like a cada post con likes
        postLikes[like] += 1
    
    max_likes = 0
    index = None
    
    #Ver que post tiene más likes
    for post in postLikes:
        if postLikes[post] > max_likes:
            max_likes = postLikes[post]
            index = post
            
    return (index[0], index[1], max_likes)

#print(obtener_post_mas_popular(red_social))

def buscar(red_social, palabras: list[str])->list[str]:
    posts = []
    numeroPalabras = len(palabras)
    #Hacer un array que contenga a todos los posts
    for user in red_social:
        for post in red_social[user]['posts']:
            posts.append(post[1])
    
    searchResult = []
    
    for post in posts:
        repetido = False
        for palabra in palabras:
            if palabra in post and not repetido:
                repetido = True # para evitar que se incluya 2 veces el mismo post si se repite la palabra
                searchResult.append(post)
    return searchResult

#print(buscar(red_social, ["motos", "coches"]))

def obtener_ranking(red_social, m: int)->list:
    """Obtiene el ranking de los `m` usuarios que hacen más
    likes a otros, excluyendo autolikes.
    """
    usuariosLikes = {}
    likesUsuarios = {}
    
    for user in red_social:
        usuariosLikes.setdefault(user, 0)
        
        
    #Contar cuantos likes ha dado cada usuario sin contar autolikes
    for user in usuariosLikes:
        for like in red_social[user]['likes']:
            if like[0] != user:
                usuariosLikes[user] +=1
    
    for user in usuariosLikes:
        likesUsuarios.setdefault(usuariosLikes[user], user)
    
    #Sacar el TOP m de usuarios
    cantidadLikes = []
    
    for user in usuariosLikes:
        cantidadLikes.append(usuariosLikes[user])
    
    #Ordenar para ver los mayores (hay que darle la vuelta porque ordena de menor a mayor)
    cantidadLikes.sort()
    cantidadLikes = cantidadLikes[::-1]
    
    #Los usuarios en el TOP m son los que han dado:
    cantidadLikes = cantidadLikes[0:m]
    
    #Que son los:
    topUsers = []
    for like in range(m):
        topUsers.append(likesUsuarios[cantidadLikes[like]])
    
    result = []
    
    for i in range(m):
        result.append((topUsers[i], cantidadLikes[i]))
    
    return result
    
#print(obtener_ranking(red_social, 2))

def tiene_autolikes(red_social, jugador:str)->bool:
    """Ni idea de como hacer esto recursivo, pero así se haría normal"""
    
    autolike = False
    if jugador not in red_social:
        return "Ese usuario no existe"
    
    likes = red_social[jugador]['likes']
    
    for i in range(len(likes)):
        if likes[i][0] == jugador:
            autolike = True
    
    return autolike

print(tiene_autolikes(red_social, "user2" ))
print(tiene_autolikes(red_social, "user0" ))