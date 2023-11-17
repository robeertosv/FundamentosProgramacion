DOLLAR_TO_EUR = 0.92
text = "This item with price expressed in $ and name $j$ is sold for 56$ and this other for 46$"

def to_eur(text:str)->str:
    words = text.split(' ')
    
    for e in words:
        if('$' in e):
            i = words.index(e)
            b = e.split('$')[0]
            try:
               b = float(b)
               words[i] = str(b * 0.92) + "€"
            except ValueError:
                pass
                
    t = ''
    for word in words:
        t += word+ ' '
    
    return t

print()
print(to_eur(text))
print()