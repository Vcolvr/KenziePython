def reverse_words(s):
    separador = s.split()
    
    separador.reverse()
    s = " ".join(separador)
        
    return s