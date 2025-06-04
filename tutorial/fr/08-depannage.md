# 🔧 Guide de Dépannage Complet

*Solutions rapides pour tous vos problèmes techniques*

---

## 🎯 Vue d'Ensemble

Ce guide résout tous les problèmes courants que vous pourriez rencontrer avec OrpheusPyPractice, de l'installation aux workflows avancés.

---

## 🚨 Problèmes d'Installation

### ❌ Erreur: "oabc command not found"
```bash
# Vérifier l'installation
which oabc
echo $PATH

# Solution 1: Réinstaller OrpheusPyPractice
cd /path/to/OrpheusPyPractice
pip install -e .

# Solution 2: Ajouter au PATH
export PATH=$PATH:/path/to/OrpheusPyPractice/bin
echo 'export PATH=$PATH:/path/to/OrpheusPyPractice/bin' >> ~/.bashrc
source ~/.bashrc
```

### ❌ Erreur: "Permission denied"
```bash
# Problème de permissions
chmod +x /path/to/OrpheusPyPractice/bin/oabc
chmod +x /path/to/OrpheusPyPractice/bin/olca

# Si nécessaire, changer le propriétaire
sudo chown -R $USER:$USER /path/to/OrpheusPyPractice
```

### ❌ Dépendances Python manquantes
```bash
# Installer toutes les dépendances
pip install -r requirements.txt

# Vérifier les dépendances manquantes
python -c "import sys; print(sys.path)"
pip list | grep -E "(music|midi|abc)"

# Installation manuelle si nécessaire
pip install music21 mido python-rtmidi
```

---

## 🎵 Problèmes avec les Fichiers ABC

### ❌ Erreur: "Invalid ABC syntax"
```bash
# Vérifier la syntaxe ABC
oabc my_song.abc --validate-only --verbose

# Problèmes courants et solutions :
```

**En-tête manquant :**
```abc
X:1          ← Numéro de référence obligatoire
T:Ma Chanson ← Titre obligatoire
M:4/4        ← Métrique obligatoire
L:1/4        ← Longueur de note par défaut
K:C          ← Tonalité obligatoire

C D E F | G A B c |
```

**Barres de mesure incorrectes :**
```abc
# ❌ Incorrect
C D E F G A B c

# ✅ Correct
C D E F | G A B c |
```

**Caractères non supportés :**
```bash
# Nettoyer les caractères problématiques
sed 's/[""]/"/g' my_song.abc > my_song_clean.abc
sed 's/['']/'"'"'/g' my_song_clean.abc > my_song_final.abc
```

### ❌ Problème de métrique/tempo
```abc
# Différentes métriques courantes
M:4/4    % 4 temps par mesure, noire = 1 temps
M:3/4    % 3 temps par mesure (valse)
M:2/4    % 2 temps par mesure (marche)
M:6/8    % 6 croches par mesure
M:C      % Équivalent à 4/4

# Longueurs de notes
L:1/4    % Noire par défaut
L:1/8    % Croche par défaut
```

---

## 🎼 Problèmes de Conversion MIDI/MP3

### ❌ Fichier MIDI vide ou corrompu
```bash
# Diagnostiquer le problème
oabc my_song.abc --output-midi --debug --verbose

# Solutions alternatives
# 1. Forcer la régénération
oabc my_song.abc --output-midi --force-regenerate

# 2. Changer le programme MIDI
oabc my_song.abc --output-midi --program acoustic_grand_piano

# 3. Ajuster la vélocité
oabc my_song.abc --output-midi --velocity 80
```

### ❌ Pas de son dans le MP3
```bash
# Vérifier les codecs audio
ffmpeg -codecs | grep mp3

# Alternative avec différents paramètres
oabc my_song.abc --output-mp3 --bitrate 192 --sample-rate 44100

# Utiliser un autre synthétiseur si disponible
oabc my_song.abc --output-mp3 --synthesizer fluidsynth
```

### ❌ Qualité audio médiocre
```bash
# Paramètres haute qualité
oabc my_song.abc --output-mp3 \
     --bitrate 320 \
     --sample-rate 48000 \
     --quality high \
     --soundfont /path/to/good_soundfont.sf2
```

---

## 🤖 Problèmes avec l'IA OLCA

### ❌ "OLCA API key not found"
```bash
# Configurer la clé API
export OLCA_API_KEY="your_api_key_here"
echo 'export OLCA_API_KEY="your_api_key_here"' >> ~/.bashrc

# Ou utiliser le fichier de configuration
mkdir -p ~/.olca
echo "api_key=your_api_key_here" > ~/.olca/config
```

### ❌ Réponses de l'IA incohérentes
```bash
# Réinitialiser le contexte
olca --reset-context

# Ajuster les paramètres
olca --set-temperature 0.7    # Moins aléatoire
olca --set-max-tokens 2000    # Réponses plus longues
olca --set-model gpt-4        # Modèle plus performant
```

### ❌ L'IA ne comprend pas les termes musicaux
```bash
# Mettre à jour la base de connaissances musicales
olca --update-music-knowledge

# Charger un vocabulaire musical personnalisé
olca --load-vocabulary musical_terms.json

# Exemple de vocabulaire :
cat > musical_terms.json << EOF
{
  "modes": ["dorien", "phrygien", "lydien", "mixolydien"],
  "instruments": ["violon", "piano", "guitare", "flûte"],
  "tempos": ["andante", "allegro", "adagio", "presto"]
}
EOF
```

---

## 🐋 Problèmes Docker

### ❌ "Docker image not found"
```bash
# Construire l'image Docker
cd /path/to/OrpheusPyPractice
docker build -t orpheuspypractice .

# Vérifier les images disponibles
docker images | grep orpheus

# Télécharger depuis DockerHub (si disponible)
docker pull orpheuspypractice:latest
```

### ❌ Problèmes de permissions dans le conteneur
```bash
# Exécuter avec l'utilisateur correct
docker run --rm -it \
  --user $(id -u):$(id -g) \
  -v $PWD:/workspace \
  orpheuspypractice oabc input.abc

# Ou ajuster les permissions
docker run --rm -it \
  -v $PWD:/workspace \
  orpheuspypractice bash -c "
    chown -R \$(id -u):\$(id -g) /workspace
    oabc input.abc
  "
```

### ❌ Volumes Docker non montés
```bash
# Vérification des chemins
pwd                    # Chemin actuel
ls -la                 # Fichiers présents

# Montage correct
docker run --rm -it \
  -v "$(pwd)":/workspace \
  -w /workspace \
  orpheuspypractice oabc input.abc --all-formats
```

---

## 📁 Problèmes de Fichiers et Chemins

### ❌ "File not found" avec chemins relatifs
```bash
# Utiliser des chemins absolus
oabc /full/path/to/input.abc --output-dir /full/path/to/output

# Ou naviguer vers le bon répertoire
cd /path/to/music/files
oabc input.abc --all-formats
```

### ❌ Caractères spéciaux dans les noms de fichiers
```bash
# Nettoyer les noms de fichiers
for file in *.abc; do
    new_name=$(echo "$file" | tr ' ' '_' | tr -cd '[:alnum:]._-')
    if [ "$file" != "$new_name" ]; then
        mv "$file" "$new_name"
    fi
done
```

### ❌ Problèmes d'encodage de fichiers
```bash
# Vérifier l'encodage
file -bi my_song.abc

# Convertir vers UTF-8
iconv -f ISO-8859-1 -t UTF-8 my_song.abc > my_song_utf8.abc

# Ou nettoyer les caractères problématiques
dos2unix my_song.abc
```

---

## 🔊 Problèmes Audio et Système

### ❌ Pas de sortie audio
```bash
# Vérifier le système audio
pulseaudio --check -v
alsamixer

# Tester la sortie audio
speaker-test -t wav -c 2

# Forcer un périphérique audio spécifique
export ALSA_DEVICE="hw:0,0"
oabc input.abc --output-mp3
```

### ❌ Latence audio élevée
```bash
# Ajuster la taille du buffer audio
export PULSE_LATENCY_MSEC=50

# Ou utiliser JACK pour un audio professionnel
jackd -d alsa -r 44100 -p 256
```

---

## 🚀 Problèmes de Performance

### ❌ Traitement très lent
```bash
# Traitement parallèle
find . -name "*.abc" | xargs -n1 -P4 -I{} oabc {} --all-formats

# Utiliser le cache
export OABC_CACHE_DIR="/tmp/oabc_cache"
mkdir -p "$OABC_CACHE_DIR"

# Optimiser les paramètres
oabc input.abc --fast-mode --low-quality-preview
```

### ❌ Mémoire insuffisante
```bash
# Traitement par lots plus petits
split -l 50 large_songbook.abc song_
for chunk in song_*; do
    oabc "$chunk" --all-formats
done

# Limiter l'utilisation mémoire
ulimit -m 1000000  # Limite à ~1GB
oabc input.abc --memory-limit 512M
```

---

## 🌐 Problèmes Réseau et API

### ❌ Timeout des requêtes API
```bash
# Augmenter le timeout
export OLCA_TIMEOUT=60
olca --timeout 60s "Compose une mélodie douce"

# Utiliser un proxy si nécessaire
export https_proxy=http://proxy:8080
export http_proxy=http://proxy:8080
```

### ❌ Limites de taux API dépassées
```bash
# Attendre et réessayer
olca --retry-attempts 3 --retry-delay 30 "Generate melody"

# Utiliser un mode batch avec délais
for prompt in $(cat prompts.txt); do
    olca "$prompt"
    sleep 5  # Attendre 5 secondes entre les requêtes
done
```

---

## 🛠️ Scripts de Diagnostic

### Script de Vérification Complète
```bash
#!/bin/bash
# diagnostic_complet.sh

echo "🔍 Diagnostic OrpheusPyPractice"
echo "================================"

# Vérifications de base
echo "📋 Vérifications de base:"
which oabc && echo "✅ oabc trouvé" || echo "❌ oabc manquant"
which olca && echo "✅ olca trouvé" || echo "❌ olca manquant"
which docker && echo "✅ docker trouvé" || echo "❌ docker manquant"

# Vérifications Python
echo -e "\n🐍 Environnement Python:"
python --version
pip list | grep -E "(music|midi|abc)" | head -5

# Test de fichier ABC simple
echo -e "\n🎵 Test ABC simple:"
cat > test.abc << EOF
X:1
T:Test
M:4/4
L:1/4
K:C
C D E F | G A B c |
EOF

if oabc test.abc --validate-only; then
    echo "✅ Syntaxe ABC valide"
else
    echo "❌ Problème de syntaxe ABC"
fi

# Test de conversion
echo -e "\n🔄 Test de conversion:"
if oabc test.abc --output-midi --quiet; then
    echo "✅ Conversion MIDI réussie"
else
    echo "❌ Échec conversion MIDI"
fi

# Nettoyage
rm -f test.abc test.mid

echo -e "\n🏁 Diagnostic terminé"
```

### Script de Réparation Automatique
```bash
#!/bin/bash
# reparation_auto.sh

echo "🔧 Réparation automatique OrpheusPyPractice"

# Réinstaller les dépendances
echo "📦 Réinstallation des dépendances..."
pip install --upgrade --force-reinstall music21 mido

# Nettoyer les caches
echo "🧹 Nettoyage des caches..."
find ~/.cache -name "*oabc*" -delete 2>/dev/null
find /tmp -name "*oabc*" -delete 2>/dev/null

# Recréer les répertoires de configuration
echo "📁 Recréation des configurations..."
mkdir -p ~/.olca ~/.oabc
chmod 755 ~/.olca ~/.oabc

# Réinitialiser les permissions
echo "🔐 Réinitialisation des permissions..."
find /path/to/OrpheusPyPractice -name "*.py" -exec chmod +x {} \;

echo "✅ Réparation terminée"
```

---

## 📞 Obtenir de l'Aide

### 🆘 Support Communautaire
```bash
# Générer un rapport de bug
olca --generate-bug-report > bug_report.txt

# Inclure les informations système
oabc --version >> bug_report.txt
python --version >> bug_report.txt
uname -a >> bug_report.txt
```

### 🔍 Logging Avancé
```bash
# Activer les logs détaillés
export DEBUG=1
export VERBOSE=1
export LOG_LEVEL=DEBUG

# Rediriger vers un fichier de log
oabc input.abc --all-formats 2>&1 | tee debug.log
```

### 📊 Collecter les Métriques
```bash
# Profiler les performances
python -m cProfile -o profile.stats /path/to/oabc input.abc
python -c "import pstats; p=pstats.Stats('profile.stats'); p.sort_stats('cumulative').print_stats(20)"
```

---

## 💡 Conseils de Prévention

### 🛡️ **Bonnes Pratiques**
- Toujours valider vos fichiers ABC avant traitement
- Utilisez des chemins absolus dans les scripts
- Sauvegardez vos configurations personnalisées

### 🔄 **Maintenance Régulière**
- Mettez à jour OrpheusPyPractice régulièrement
- Nettoyez les caches et logs anciens
- Testez vos workflows après chaque mise à jour

### 📋 **Documentation**
- Documentez vos configurations personnalisées
- Gardez une trace des modifications apportées
- Créez des scripts de sauvegarde pour vos projets

---

## 🎯 Solutions Rapides

| Problème | Solution Rapide |
|----------|----------------|
| 🚫 Commande non trouvée | `export PATH=$PATH:/path/to/bin` |
| 🎵 ABC invalide | `oabc file.abc --validate-only` |
| 🔇 Pas de son | `pulseaudio --check -v` |
| 🐋 Docker ne marche pas | `docker build -t orpheuspypractice .` |
| 🤖 IA non configurée | `export OLCA_API_KEY="your_key"` |
| 📁 Fichier non trouvé | Utiliser chemin absolu |
| 🐌 Traitement lent | `oabc --fast-mode input.abc` |
| 💾 Mémoire insuffisante | `ulimit -m 1000000` |

---

*🎉 **Félicitations !** Vous avez maintenant tous les outils pour résoudre les problèmes techniques. Votre aventure musicale avec OrpheusPyPractice peut continuer sans encombre !*
