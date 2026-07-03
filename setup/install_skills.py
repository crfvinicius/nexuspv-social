"""
Instala as skills do Agente Social Media no Claude Code.
Copia as skills para ~/.claude/skills/
"""
import shutil
from pathlib import Path

SKILLS_SRC = Path(__file__).parent.parent / "skills"
SKILLS_DST = Path.home() / ".claude" / "skills"
SKILLS_DST.mkdir(parents=True, exist_ok=True)

skills = [
    "agente-social-media",
    "criar-reel",
    "gerar-carrossel",
    "criar-thumbnail",
    "gerar-copy-post",
    "repurpose-conteudo",
    "gerar-imagem",
    "gerar-video-mp4",
]

print("\n=== INSTALANDO SKILLS ===\n")
for skill in skills:
    src = SKILLS_SRC / skill
    dst = SKILLS_DST / skill
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"  OK  {skill}")
    else:
        print(f"  --  {skill} (não encontrado em {src})")

print(f"\n{len(skills)} skills instaladas em: {SKILLS_DST}")
print("\nReinicie o Claude Code para carregar as skills.")
