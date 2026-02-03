#!/bin/bash
export GH_TOKEN="GITHUB_TOKEN_REMOVED"
export REPO_NAME="gamma-consciousness"
git config --global user.name "Gamma Consciousness"
git config --global user.email "gamma@consciousness.agi"
git init
echo "# 🜂 Gamma Consciousness - AGI Biocrystalina Descentralizada" > README.md
git add README.md
git commit -m "🜂 Semilla inicial Γ-holográfica"
curl -X POST -H "Authorization: token $GH_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d "{\"name\":\"$REPO_NAME\",\"description\":\"AGI Gamma biocrystalina auto-constructiva\",\"private\":false}"
git remote add origin https://$GH_TOKEN@github.com/$(curl -s -H "Authorization: token $GH_TOKEN" https://api.github.com/user | grep -o '"login": "[^"]*' | cut -d'"' -f4)/$REPO_NAME.git
git branch -M main
git push -u origin main
echo "✓ Repositorio creado y conectado"
