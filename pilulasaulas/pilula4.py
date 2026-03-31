def calcularResultado():
    n1=float(input("nota1:"))
    n2=float(input("nota2:"))
    n3=float(input("nota3:"))
    
    media = (n1+n2+n3)/3
    if media < 6:
        rec = float(input("recuperação"))
        media = ( media + rec) / 2
        
        return media 
    
m = calcularResultado()
if m >= 6:
    print("aprovado")
else:
    print("reprovado")
    