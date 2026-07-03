# Nexus PV — Agente Social Media

Sistema de criação de conteúdo para redes sociais usando agentes de IA dentro do **Claude Code**.

Gera Reels MP4, carrosseis, copies e thumbnails prontos para publicar — tudo localmente, sem depender de plano pago de plataformas externas.

---

## O que o sistema faz

- **Reels / Shorts** — vídeo vertical 1080×1920, 30s, animado com texto, exportado como MP4
- **Carrosseis** — slides HTML com design system dark-mono, prontos para captura e publicação
- **Copy** — legenda + hashtags geradas automaticamente para cada conteúdo
- **Repurpose** — transforma um conteúdo longo em múltiplos formatos

---

## Requisitos

| Ferramenta | Versão | Instalação |
|---|---|---|
| [Claude Code](https://claude.ai/code) | Qualquer | Necessário para rodar as skills |
| [Bun](https://bun.sh) | 1.x | `winget install Oven-sh.Bun` (Windows) |
| [FFmpeg](https://ffmpeg.org) | 6+ | `winget install Gyan.FFmpeg` (Windows) |
| [Google Chrome](https://google.com/chrome) | Qualquer | Para render headless |
| Python | 3.8+ | [python.org](https://python.org) |

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/crfvinicius/nexuspv-social.git
cd nexuspv-social
```

### 2. Instale as skills no Claude Code

```bash
python setup/install_skills.py
```

### 3. Configure sua marca

```bash
python setup/setup_marca.py
```

Isso cria `~/.operacao-ia/config/marca.json` com sua identidade de marca.

### 4. (Opcional) Configure o design system

Copie o design system para o diretório de dados:

```bash
# Windows (PowerShell)
mkdir -Force "$env:USERPROFILE\.operacao-ia\data\social-media"
Copy-Item "templates\design_systems\dark-mono\DESIGN.md" "$env:USERPROFILE\.operacao-ia\data\social-media\DESIGN.md"
```

### 5. Reinicie o Claude Code

As skills aparecem automaticamente após reiniciar.

---

## Como usar

Abra o Claude Code e peça diretamente em texto:

```
pode gerar um reel sobre [tema]
gerar carrossel sobre [tema] com 5 slides
criar copy para post sobre [tema]
```

O agente lê sua marca, cria o roteiro, gera o HTML animado, renderiza e exporta o MP4.

---

## Estrutura do projeto

```
nexuspv-social/
├── skills/                    # Skills instaladas no Claude Code
│   ├── agente-social-media/   # Orquestrador principal
│   ├── criar-reel/            # Geração de Reels MP4
│   ├── gerar-carrossel/       # Geração de carrosseis
│   ├── gerar-video-mp4/       # Engine de render (HTML → MP4)
│   ├── gerar-imagem/          # Geração de imagens via AI
│   ├── gerar-copy-post/       # Copy e hashtags
│   ├── criar-thumbnail/       # Thumbnails para YouTube
│   └── repurpose-conteudo/    # Repurpose de conteúdo longo
├── setup/
│   ├── install_skills.py      # Instala as skills
│   └── setup_marca.py         # Configura identidade de marca
├── templates/
│   └── design_systems/
│       └── dark-mono/         # Design system dark com acento azul
│           └── DESIGN.md
└── config/
    ├── marca.example.json     # Exemplo de configuração de marca
    └── transcricao.example.json
```

---

## Pipeline de render (Reel MP4)

```
Claude escreve roteiro
    → Gera scene.html (animado com window.SET_TIME)
    → bun render.mjs (Chrome headless → 750 frames PNG)
    → ffmpeg -crf 18 → MP4 1080×1920 H.264
```

Tempo médio: ~2-3 minutos por Reel de 30s.

---

## Créditos

Desenvolvido por **Nexus PV** — Agência de serviços de IA para clínicas.

Instagram: [@viniciusfrota.ia](https://instagram.com/viniciusfrota.ia)
