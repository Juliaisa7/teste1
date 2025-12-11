softwares_criticos = ["ERP", "Banco de Dados SQL", "Firewall"]

software_novo = input("Digite o nome do software a ser instalado: ")

if software_novo in softwares_criticos:
    print("Atenção: Este software é crítico e já está instalado. Nenhuma alteração é necessária.")

else:
    print(f"Software '{software_novo}' não encontrado no inventário. Iniciando instalação...")
    softwares_criticos.append(software_novo)

print("Inventário atualizado de softwares críticos:")
print(softwares_criticos)
