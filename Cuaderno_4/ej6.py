"""
Implementar una función que compruebe si una palabra es un palíndromo.
Atención, no hagas más trabajo del necesario. 
"""

def is_palindrome(palabra:str)->bool:
    palindrome = None
    inversa = palabra[::-1]
    
    if(palabra == inversa):
        palindrome = True
    else:
        palindrome = False
    
    return palindrome

print(is_palindrome('Roberto'))
print(is_palindrome('ana'))