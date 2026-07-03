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

Antes de instalar, verifique se tem tudo instalado:

| Ferramenta | Versão | Como instalar |
|---|---|---|
| [Claude Code](https://claude.ai/code) | Qualquer | Baixar no site oficial |
| [Google Chrome](https://google.com/chrome) | Qualquer | Baixar no site oficial |
| [Python](https://python.org) | 3.8+ | Baixar no site oficial |
| [Git](https://git-scm.com) | Qualquer | Baixar no site oficial |
| [Bun](https://bun.sh) | 1.x | Ver instruções abaixo |
| [FFmpeg](https://ffmpeg.org) | 6+ | Ver instruções abaixo |

### Instalar Bun e FFmpeg (Windows)

Abra o **PowerShell como Administrador** e rode:

```powershell
winget install Oven-sh.Bun
winget install Gyan.FFmpeg
```

Feche e reabra o PowerShell após instalar para o PATH atualizar.

**Verificar instalação:**
```powershell
bun --version
ffmpeg -version
```

---

## Instalação

### 1. Clone o repositório

Abra o **PowerShell** e rode:

```powershell
git clone https://github.com/crfvinicius/nexuspv-social.git
cd nexuspv-social
```

### 2. Instale as skills no Claude Code

```powershell
python setup/install_skills.py
```

Você verá `OK` para cada uma das 8 skills instaladas.

### 3. Configure o design system

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.operacao-ia\data\social-media"
Copy-Item "templates\design_systems\dark-mono\DESIGN.md" "$env:USERPROFILE\.operacao-ia\data\social-media\DESIGN.md"
```

### 4. Configure sua marca

```powershell
python setup/setup_marca.py
```

O script vai perguntar:
1. Nome da sua marca
2. Nicho/segmento
3. Handle do Instagram (ex: `@suamarca`)
4. Tom de voz
5. Público-alvo
6. Proposta de valor
7. Produtos/serviços

### 5. Reinicie o Claude Code

Feche e reabra o Claude Code. As skills carregam automaticamente.

---

## Como usar

Abra o Claude Code, navegue até qualquer pasta e peça em texto:

```
pode gerar um reel sobre [tema]
```

```
gerar carrossel sobre [tema] com 5 slides
```

```
criar copy para post sobre [tema]
```

O agente lê sua marca, cria o roteiro, pede sua aprovação e gera o arquivo final.

**Onde ficam os arquivos gerados:**
```
~/.operacao-ia/data/social-media/output/
├── reels/          → MP4 prontos para publicar
└── carrosseis/     → HTML dos slides
```

---

## Pipeline de render (Reel MP4)

```
Claude escreve roteiro
    → Gera scene.html (animado com window.SET_TIME)
    → bun render.mjs (Chrome headless → 750 frames PNG)
    → ffmpeg -crf 18 → MP4 1080×1920 H.264
```

Tempo médio: **2-3 minutos** por Reel de 30s.

---

## Checklist de validação (para testadores)

Após instalar, confirme cada item:

- [ ] `python setup/install_skills.py` rodou sem erro e mostrou `OK` para as 8 skills
- [ ] `DESIGN.md` foi copiado para `~/.operacao-ia/data/social-media/`
- [ ] `python setup/setup_marca.py` criou o arquivo `~/.operacao-ia/config/marca.json`
- [ ] Claude Code reiniciado reconhece as skills (tente digitar `/criar-reel`)
- [ ] Conseguiu gerar um Reel de teste com o comando `pode gerar um reel sobre [tema]`
- [ ] O MP4 foi gerado em `~/.operacao-ia/data/social-media/output/reels/`

Qualquer passo que falhar, reporte com a mensagem de erro exata.

---

## Estrutura do projeto

```
nexuspv-social/
├── skills/                    # Skills do Claude Code
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
└── config/
    ├── marca.example.json
    └── transcricao.example.json
```

---

## Créditos

Desenvolvido por **Nexus PV** — Agência de serviços de IA para clínicas.

Instagram: [@viniciusfrota.ia](https://instagram.com/viniciusfrota.ia)
