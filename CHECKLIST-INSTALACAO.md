# Checklist de Instalação — Nexus PV Social Media Agent

Marque cada item conforme for completando. Se travar em algum passo, anote a mensagem de erro exata e envie para [@viniciusfrota.ia](https://instagram.com/viniciusfrota.ia).

---

## Pré-requisitos

- [ ] **Claude Code** instalado e funcionando → [claude.ai/code](https://claude.ai/code)
- [ ] **Google Chrome** instalado → [google.com/chrome](https://google.com/chrome)
- [ ] **Python 3.8+** instalado → [python.org](https://python.org)
- [ ] **Git** instalado → [git-scm.com](https://git-scm.com)
- [ ] **Bun** instalado → `winget install Oven-sh.Bun`
- [ ] **FFmpeg** instalado → `winget install Gyan.FFmpeg`

**Verificar no PowerShell:**
```powershell
python --version
bun --version
ffmpeg -version
git --version
```

---

## Instalação

- [ ] **1. Clonar o repositório**
  ```powershell
  git clone https://github.com/crfvinicius/nexuspv-social.git
  cd nexuspv-social
  ```

- [ ] **2. Instalar as skills**
  ```powershell
  python setup/install_skills.py
  ```
  Resultado esperado: `OK` para cada uma das 8 skills

- [ ] **3. Copiar o design system**
  ```powershell
  New-Item -ItemType Directory -Force "$env:USERPROFILE\.operacao-ia\data\social-media"
  Copy-Item "templates\design_systems\dark-mono\DESIGN.md" "$env:USERPROFILE\.operacao-ia\data\social-media\DESIGN.md"
  ```

- [ ] **4. Configurar a marca**
  ```powershell
  python setup/setup_marca.py
  ```
  Resultado esperado: arquivo criado em `~/.operacao-ia/config/marca.json`

- [ ] **5. Reiniciar o Claude Code**
  Feche e reabra o Claude Code completamente.

---

## Validação

Após instalar, teste cada funcionalidade:

- [ ] **Skills carregaram** → No Claude Code, digite `/criar-reel` e veja se reconhece o comando
- [ ] **Reel gerado** → Peça: `pode gerar um reel sobre inteligência artificial`
  - [ ] Claude pediu aprovação do roteiro
  - [ ] Render rodou (apareceu progresso de frames)
  - [ ] MP4 gerado em `~/.operacao-ia/data/social-media/output/reels/`
- [ ] **Carrossel gerado** → Peça: `gerar carrossel sobre [tema] com 5 slides`
  - [ ] HTML gerado em `~/.operacao-ia/data/social-media/output/carrosseis/`
  - [ ] Abriu no browser com navegação por slide funcionando

---

## Reporte de Erros

Se algo não funcionar, envie:

1. **Em qual passo travou** (número do passo acima)
2. **Mensagem de erro exata** (copie e cole o texto)
3. **Sistema operacional** (Windows 10, Windows 11, Mac, etc.)
4. **Versões** (`python --version`, `bun --version`, `ffmpeg -version`)

Envie o reporte para: **[@viniciusfrota.ia](https://instagram.com/viniciusfrota.ia)** no Instagram

---

## Observações

- O render de um Reel de 30s leva em média **2-3 minutos**
- Os arquivos gerados ficam em `~/.operacao-ia/data/social-media/output/`
- Para gerar um novo Reel basta abrir o Claude Code e pedir em texto — não precisa rodar nada no terminal
- Em caso de dúvida, consulte o [README.md](README.md)
