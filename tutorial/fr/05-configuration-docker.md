# 🐳 Configuration Docker - Environnement Musical Professionnel

## Qu'est-ce que l'Intégration Docker ?

**OrpheusPyPractice** est livré avec un **environnement Docker complet** qui fournit :
- 🎼 **MuseScore3 pré-configuré** pour génération de partitions
- 🎵 **Outils ABC2MIDI** prêts à utiliser
- 🖼️ **ImageMagick** pour traitement graphique
- 🗂️ **Support X11** pour applications GUI
- 🔧 **Toutes les dépendances** parfaitement configurées

**Parfait pour :** Environnements de production, CI/CD, collaboration d'équipe, ou développement isolé.

---

## 🚀 Démarrage Docker Rapide

### Option 1 : Environnement de Test (Recommandé pour débutants)
```bash
# Naviguer vers environnement de test
cd bin/testapp

# Exécuter le conteneur (inclut échantillons et tests)
dkrun

# Vous êtes maintenant dans le conteneur avec tout prêt !
# Essayer convertir un échantillon :
oabc /samples/Bov_i3.abc
```

### Option 2 : Environnement de Production
```bash
# Naviguer vers environnement de production  
cd bin/app

# Exécuter le conteneur de production
dkrun

# Environnement musical complet prêt
```

### Option 3 : Environnement de Base
```bash
# Juste les outils principaux
cd bin/base
dkrun
```

---

## 🎯 Ce Qui Est Dans le Conteneur

### Outils Musicaux Pré-installés
- **MuseScore3** - Génération de partitions professionnelles
- **ABC2MIDI** - Conversion notation ABC vers MIDI  
- **ImageMagick** - Traitement graphique pour partitions
- **Xvfb** - Affichage virtuel pour applications GUI
- **OrpheusPyPractice** - Boîte à outils complète installée

### Fichiers d'Échantillons Disponibles
```bash
# Dans le conteneur, vérifier échantillons
ls /samples/
# Bov_i3.abc
# loup-01c_tst_240620172717.abc
# ... et plus !

# Fichiers de test pour vérification
ls /tests/
# test_oabc.sh
# test_musescore3_mid_2_score.sh
```

### Environnement de Travail
```bash
# Votre espace de travail
/work/     # Monter vos fichiers locaux ici
/app/      # Fichiers d'application
/scripts/  # Scripts d'aide
/samples/  # Fichiers ABC d'exemple
```

---

## 🔧 Architecture du Conteneur

### Conteneur de Base (`jgwill/orpheus:base`)
```dockerfile
# Ubuntu avec Python 3.10
# Dépendances musicales : abcmidi, musescore3
# Support X11 pour applications GUI
# Configuration d'affichage virtuel
```

### Conteneur App (`jgwill/orpheus:app`)
```dockerfile
# Étend base avec OrpheusPyPractice installé
# Permissions utilisateur configurées
# Environnement prêt pour production
```

### Conteneur Test (`jgwill/orpheus:testapp`)
```dockerfile
# Étend app avec fichiers de test
# Fichiers ABC d'échantillons inclus
# Capacités de test automatisé
```

---

## 🎼 Exemples d'Utilisation du Conteneur

### Exemple 1 : Convertir Fichiers d'Échantillons
```bash
# Démarrer conteneur de test
cd bin/testapp && dkrun

# Dans le conteneur :
cd /samples
oabc Bov_i3.abc
ls -la Bov_i3.*
# Bov_i3.abc  Bov_i3.mid  Bov_i3.mp3  Bov_i3.svg
```

### Exemple 2 : Travailler avec Vos Fichiers
```bash
# Vos fichiers sont montés à /app
cd bin/testapp && dkrun

# Dans le conteneur :
cd /app
# Vos fichiers locaux sont ici !
ls *.abc
oabc ma_chanson.abc
```

### Exemple 3 : Traitement par Lots
```bash
# Traiter plusieurs fichiers
cd bin/testapp && dkrun

# Dans le conteneur :
cd /app
for abc_file in *.abc; do
    echo "Conversion $abc_file..."
    oabc "$abc_file"
done
```

### Exemple 4 : Assistant IA dans Conteneur
```bash
# Utiliser OLCA dans conteneur
cd bin/testapp && dkrun

# Dans le conteneur :
export OPENAI_API_KEY_olca="votre-clé"
olca init
olca
# Assistance IA complète dans environnement isolé
```

---

## 🔥 Fonctionnalités Docker Avancées

### Montage de Volume
Vos fichiers locaux sont automatiquement montés :
```bash
# Répertoire local → Chemin conteneur
./                → /app/
```

### Variables d'Environnement
```bash
# Support d'affichage pour applications GUI
DISPLAY=:99

# Débogage Qt
QT_DEBUG_PLUGINS=1

# Transfert X11
/tmp/.X11-unix:/tmp/.X11-unix
```

### Gestion Utilisateur
```bash
# Utilisateur conteneur : jgi
# Accès sudo : Disponible
# Permissions : Configurées pour outils musicaux
```

---

## 🛠️ Construire Votre Propre Conteneur

### Dockerfile Personnalisé
```dockerfile
FROM jgwill/orpheus:base

# Ajouter vos outils personnalisés
RUN apt-get update && apt-get install -y \
    votre-outil-musical \
    votre-éditeur-préféré

# Copier vos configurations
COPY mes_configs/ /home/jgi/.config/

# Définir votre environnement de travail
WORKDIR /mon_projet
```

### Construire et Tester
```bash
# Construire votre image
docker build -t mon-orpheus .

# Tester
docker run -it --rm \
    -v $(pwd):/app \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY=:99 \
    mon-orpheus
```

---

## 🎯 Intégration CI/CD

### Exemple GitHub Actions
```yaml
# .github/workflows/pipeline-musical.yml
name: Pipeline Musical
on: [push]
jobs:
  test-musique:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Tester Conversion ABC
      run: |
        cd bin/testapp
        dkrun bash /tests/test_oabc.sh
```

### Docker Compose (Futur)
```yaml
# docker-compose.yml
version: '3'
services:
  orpheus:
    image: jgwill/orpheus:testapp
    volumes:
      - .:/app
    environment:
      - DISPLAY=:99
```

---

## 🔧 Workflow de Développement de Conteneur

### 1. Cycle de Développement
```bash
# Éditer code source localement
vim src/orpheuspypractice/...

# Construire et tester dans conteneur
cd bin/testapp
dkbuild          # Construire nouvelle image
dkrun            # Tester changements
```

### 2. Workflow de Test
```bash
# Exécuter tests automatisés
cd bin/testapp
dkrun bash /tests/test_oabc.sh

# Vérifier tous composants
dkrun bash /tests/test_musescore3_mid_2_score.sh
```

### 3. Déploiement Production
```bash
# Construire image production
cd bin/app
dkbuild

# Déployer en production
docker push jgwill/orpheus:app
```

---

## 🎼 Scripts de Conteneur

### Commandes Utiles de Conteneur
```bash
# Dans n'importe quel conteneur :

# Vérifier outils musicaux
odep is_musescore_installed
odep is_abc2midi_installed
odep is_imagemagick_installed

# Exécuter tests
bash /tests/test_oabc.sh

# Convertir échantillons
cd /samples && oabc *.abc

# Démarrer affichage virtuel (si nécessaire)
sudo Xvfb :99 -screen 0 1024x768x16 &
```

### Scripts d'Automatisation
```bash
# /scripts/run.sh - Point d'entrée principal du conteneur
# /scripts/convert_all.sh - Conversion par lots de fichiers ABC  
# /tests/test_*.sh - Test automatisé
```

---

## 🆘 Dépannage Docker

### Problèmes Courants

#### "Impossible de se connecter au daemon Docker"
```bash
# Démarrer service Docker
sudo systemctl start docker

# Ajouter utilisateur au groupe docker
sudo usermod -aG docker $USER
# (se déconnecter et reconnecter)
```

#### "Transfert X11 ne fonctionne pas"
```bash
# Vérifier configuration X11
echo $DISPLAY

# Autoriser connexions X11 (si nécessaire)
xhost +local:docker
```

#### "Permission refusée dans conteneur"
```bash
# Vérifier permissions utilisateur
whoami  # Devrait être 'jgi'

# Fichiers devraient être accessibles en écriture
ls -la /app/
```

#### "MuseScore ne fonctionne pas"
```bash
# Vérifier affichage virtuel
ps aux | grep Xvfb

# Redémarrer affichage virtuel
sudo pkill Xvfb
sudo Xvfb :99 -screen 0 1024x768x16 &
```

---

## 🔥 Conseils Pro

### 1. Stockage Persistant
```bash
# Créer volume nommé pour données persistantes
docker volume create orpheus-data

# Utiliser dans conteneur
dkextra=" -v orpheus-data:/persistent "
```

### 2. Raccourcis de Développement
```bash
# Alias test rapide
alias otest='cd bin/testapp && dkrun bash /tests/test_oabc.sh'

# Accès rapide conteneur
alias odev='cd bin/testapp && dkrun'
```

### 3. Support Multi-Architecture
```bash
# Construire pour différentes plateformes
docker buildx build --platform linux/amd64,linux/arm64 .
```

### 4. Optimisation de Conteneur
```bash
# Vérifier taille image
docker images | grep orpheus

# Constructions multi-étapes pour images plus petites
# (voir exemples Dockerfile)
```

---

## 🎯 Considérations de Production

### Sécurité
```bash
# Exécuter avec utilisateur non-root (déjà configuré)
# Limiter capacités conteneur
# Utiliser secrets pour clés API
# Mises à jour sécurité régulières
```

### Surveillance
```bash
# Gestion logs
docker logs conteneur-orpheus

# Vérifications santé
# Surveillance ressources conteneur
# Surveillance statut outils musicaux
```

### Mise à l'Échelle
```bash
# Mise à l'échelle horizontale avec Docker Swarm/Kubernetes
# Équilibrage charge pour conteneurs multiples
# Stockage partagé pour fichiers ABC
```

---

## 📚 Prochaines Étapes

1. **🔧 Workflows avancés** → `06-workflows-avances.md`
2. **📖 Narration IA** → `07-narration-ia.md`
3. **🆘 Dépannage** → `08-depannage.md`

---

*🐳 Docker vous donne un environnement musical parfait et reproductible - développez n'importe où, déployez partout !*
