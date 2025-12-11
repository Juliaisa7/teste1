cargo = "Usuário"

status_ativo= True

if cargo == "Administrador"  and status_ativo == True:
    print("Acesso Total ao Sistema")
elif cargo == "Usuário" and status_ativo == True:
    print("Acesso Limitado: Módulo de Manutenção")
elif cargo == "Visitante" and status_ativo == True:
    print("Acesso Somente a Leitura")
else:
    print("Acesso Negado: Usuário Inativo")