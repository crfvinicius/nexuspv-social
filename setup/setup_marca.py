"""
Setup da identidade de marca para o Agente Social Media.
Cria o arquivo ~/.operacao-ia/config/marca.json interativamente.
"""
import json
import os
from pathlib import Path

CONFIG_DIR = Path.home() / ".operacao-ia" / "config"
CONFIG_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT = CONFIG_DIR / "marca.json"

print("\n=== SETUP DA MARCA ===\n")
print("Responda as perguntas abaixo para configurar sua identidade de marca.\n")

nome = input("1. Nome da sua marca/empresa: ").strip()
nicho = input("2. Nicho/segmento (ex: Agência de IA para clínicas): ").strip()
instagram = input("3. Handle do Instagram (com @): ").strip()
tom = input("4. Tom de voz (ex: didático e aspiracional): ").strip()
publico = input("5. Público-alvo (ex: donos de clínicas veterinárias): ").strip()
proposta = input("6. Proposta de valor (o que você entrega): ").strip()
produtos_raw = input("7. Produtos/serviços principais (separados por vírgula): ").strip()
produtos = [p.strip() for p in produtos_raw.split(",")]

data = {
    "nome": nome,
    "nicho": nicho,
    "handles": {"instagram": instagram},
    "tom_de_voz": tom,
    "publico_alvo": publico,
    "proposta_de_valor": proposta,
    "produtos": produtos
}

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nMarca configurada com sucesso em: {OUTPUT}")
