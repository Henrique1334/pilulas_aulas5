def menu():
    while True:
        op = int(input("menu\n 1- Soma \n2 - media \n3 - sair "))
        if op == 3:
            break
        n1 = float(input("n1:"))
        n2 = float(input("n2:"))
        if op == 1:
            print(f"Soma{n1} + {n2} = {n1+n2}")
        elif op == 2:
            print (f"media de{n1} e {n2} = {(n1 +n2)/2}")  
        else:
            print("opçao errada")
        

menu()