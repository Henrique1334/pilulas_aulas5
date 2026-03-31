def simularCrescimento(populacao,taxa,limite):
     Anos= 0
     while populacao <= limite:
        populacao= populacao * (1 + taxa)
        Anos += 1
     return Anos

#main
p= float(input("populacao inicial:"))
t= float(input("taxa(%):"))
l= float(input("limite:"))

print(f"Anos={simularCrescimento(p,t,l)}")
