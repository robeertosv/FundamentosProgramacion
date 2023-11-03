def read_next_frequency():
    valor = 0
    try:
        v = int(input("Dime un valor: "))
    except ValueError:
        valor = 0
    else:
        if v < 200:
            valor = v
            
    return valor

def process_series():
    i = 0
    SPIKE_SIZE = 10
    AVG_THRESHOLD = 20
    prev = 0
    cantidad = 0 
    sumatorio = 0
    while i >= 0:
        val = read_next_frequency()
        
        if(abs(cantidad- prev) > SPIKE_SIZE):
            print("Pico detectado!!")
            
        cantidad +=1
        sumatorio += val
        prev = val
        if(sumatorio / cantidad > AVG_THRESHOLD):
            print("PELIGRO: Por encima de la media")
            
        i = val
        
process_series()