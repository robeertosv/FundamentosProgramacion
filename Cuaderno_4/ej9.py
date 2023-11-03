"""
Implemente una función que indique si una palabra contiene las cinco vocales:
por ejemplo “murciélago”. Modifique posteriormente la función para que detecte
sólo aquellas palabras que contienen una única vez cada vocal.
"""
word = "murciélago"
def allVowels(word:str)->bool:
    a = False
    e = False
    i = False
    o = False
    u = False
    for i in range(len(word)):
        if(word[i] == 'a' or word[i] == 'á'):
            a = True
        elif(word[i] == 'e' or word[i] == 'é'):
            e = True
        elif(word[i] == 'i' or word[i] == 'í'):
            i = True
        elif(word[i] == 'o' or word[i] == 'ó'):
            o = True
        elif(word[i] == 'u' or word[i] == 'ú'):
            u = True
    return True if(a and e and i and o and u) else False
def allVowelsOneTime(word:str)->bool:
    a = False
    e = False
    i = False
    o = False
    u = False
    repeated = False
    for i in range(len(word)):
        if(word[i] == 'a' or word[i] == 'á'):
            if(a == True):
                repeated = True
            else:
                a = True
        elif(word[i] == 'e' or word[i] == 'é'):
            if(e == True):
                repeated = True
            else:
                e = True
        elif(word[i] == 'i' or word[i] == 'í'):
            if(i == True):
                repeated = True
            else:
                i = True
        elif(word[i] == 'o' or word[i] == 'ó'):
            if(o == True):
                repeated = True
            else:
                o = True
        elif(word[i] == 'u' or word[i] == 'ú'):
            if(u == True):
                repeated = True
            else:
                u = True
        
    return True if(a and e and i and o and u and not repeated) else False

print(allVowelsOneTime(word))