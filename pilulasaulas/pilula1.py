def ValidarSenha(senha):
    if len(senha)< 8:
     return 'senha invalida, muito curta'
    temNumero= False
    temMaiuscula= False
   
    for c in senha:
        if c == "  " : 
            return " senha invalida, não pode conter espaços "
        if c >= "0" and c <= "9":
            temNumero= True
        if c >= "A" and c<= "Z":
            temMaiuscula=True
            
    if not temNumero:
            return"senha invalida, não tem numero"
            
    if not temMaiuscula:
      return "senha invalida, não tem maiuscula"
        
    return "senha valida"
        
#main
senha=input("digite sua senha:")
print(ValidarSenha(senha))