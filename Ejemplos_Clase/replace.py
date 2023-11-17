def replace_hashtag(text:str, rep:str)->str:
    words = []
    for i in range(len(text)):
        if(text[i] == '#'):
            words.append(rep)
        else:
            words.append(text[i])
    
    final = ''
    for letter in words:
        final += letter
    return final

print(replace_hashtag('Roberto#Seco#Volkava', '*'))