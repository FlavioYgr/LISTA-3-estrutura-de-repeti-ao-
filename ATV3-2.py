print("cadastro")
usuario=str(input("usuário: "))
senha=str(input("SENHA :"))
while usuario==senha:	
        print("ERRO: o usuário não pode ser igual a senha, tente novamente")
        usuario=str(input("usuário : "))	
        senha=str(input("SENHA:"))
else:	
    print("cadastrado efetuado com sucesso")