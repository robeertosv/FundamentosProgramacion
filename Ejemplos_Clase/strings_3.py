def removesw(text:str, stopwords:list)->list:
    words = text.split(' ')
    final = []
    for word in words:
        if(word not in stopwords):
            final.append(word)
    
    t = ''
    
    for words in final:
        t += words + ' '
    
    return t


stopwords = ['The', 'a', 'some', 'in', 'of', 'is', 'there']
text = 'There is a good opportunity in some of the companies'

print(removesw(text, stopwords))