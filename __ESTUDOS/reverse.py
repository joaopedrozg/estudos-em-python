def reverse1(numero):
    novo = list(str(numero))
    novo.reverse()
    novo = ''.join(novo)
    novo = int(novo)
    
    return novo

print(reverse1(123456789))