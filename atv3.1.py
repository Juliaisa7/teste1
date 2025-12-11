inventario = [
{"id": 101, "modelo": "Notebook i5", "status": "ativo"},
{"id": 102, "modelo": "Desktop i3", "status": "manutenção"},
{"id": 103, "modelo": "Notebook i7", "status": "ativo"},
{"id": 104, "modelo": "Servidor Dell", "status": "ativo"}
]

for user in inventario:
    if user.get("status") == "ativo":
        print(f"{user["modelo"]}= ativo ")