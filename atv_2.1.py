chamado = {"equipamento": "Servidor Principal","tempo_parado_horas": 5,"setor": "Financeiro","status": "aberto"}

if chamado["equipamento"] == "Servidor Principal" or chamado["tempo_parado_horas"] > 4:
    prioridade = "P1 - Crítica"

elif chamado["setor"] == "Financeiro" and chamado["tempo_parado_horas"] > 1:
    prioridade = "P2 - Alta"

else:
    prioridade = "P3 - Normal"
print(f"Equipamento: {chamado['equipamento']} | Prioridade definida: {prioridade}")
