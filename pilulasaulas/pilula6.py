def ehPrimo(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i ==0:
            return False
        
    return True
    
Valor = int(input("N="))
if ehPrimo(Valor):
    print(" e primo")
else:
    print("nao e primo ")