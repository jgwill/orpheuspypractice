# 🎵 Commande OABC - Votre Couteau Suisse Musical

## Qu'est-ce qu'OABC ?

**OABC** est la commande magique qui transforme votre notation ABC en **tout** ce dont vous avez besoin :
- 🎼 **Belles partitions** (SVG/JPG)
- 🎵 **Fichiers MIDI** pour la lecture
- 🔊 **Fichiers audio MP3**
- ⚡ **Tout en une commande !**

---

## 🚀 Utilisation de Base

### Conversion Simple
```bash
# Convertir fichier ABC en tout
oabc ma_chanson.abc
```

**Ce que vous obtenez :**
- `ma_chanson.mid` - Fichier MIDI
- `ma_chanson.mp3` - Fichier audio
- `ma_chanson.svg` - Partition (vectoriel)

### Vérifier Toutes les Dépendances
```bash
# S'assurer que tout est installé
odep install_musescore
odep install_abc2midi  
odep install_imagemagick
```

---

## 🎯 Exemple Étape par Étape

### 1. Créer Votre Fichier ABC
Créez `valse.abc` :
```abc
X:1
T:Valse Simple
L:1/8
M:3/4
Q:1/4=120
K:C
|: C2 E2 G2 | c4 G2 | F2 A2 c2 | G6 :|
|: e2 d2 c2 | B2 A2 G2 | F2 E2 D2 | C6 :|
```

### 2. La Convertir
```bash
oabc valse.abc
```

### 3. Vérifier Vos Résultats
```bash
ls -la valse.*
# valse.abc  - Votre notation ABC originale
# valse.mid  - Fichier MIDI pour instruments/DAW
# valse.mp3  - Audio pour partager/écouter
# valse.svg  - Belle partition
```

---

## 🔥 Fonctionnalités Avancées

### Différents Formats de Sortie
```bash
# Obtenir JPG au lieu de SVG pour la partition
oabc ma_chanson.abc --format jpg

# Spécifier répertoire de sortie personnalisé
oabc ma_chanson.abc --output /chemin/vers/sortie/
```

### Traitement par Lots
```bash
# Convertir tous les fichiers ABC du répertoire courant
for file in *.abc; do
    oabc "$file"
done
```

### Paramètres de Qualité
```bash
# Export audio haute qualité
oabc ma_chanson.abc --audio-quality high

# Vélocité MIDI personnalisée
oabc ma_chanson.abc --velocity 80
```

---

## 🎼 Ce Qui Se Passe Sous le Capot

Quand vous exécutez `oabc ma_chanson.abc`, voici la magie :

1. **🔍 Analyser ABC** - Lit votre notation ABC
2. **🎵 Générer MIDI** - Utilise `abc2midi` pour créer MIDI
3. **🎼 Créer Partition** - Utilise `musescore3` pour de belles partitions
4. **🔊 Générer Audio** - Convertit MIDI en MP3
5. **✨ Polir Sortie** - Optimise tous les formats

```
ma_chanson.abc
     ↓
  [Magie OABC]
     ↓
┌─────────────────┐
│ ma_chanson.mid  │ ← MIDI pour DAW
│ ma_chanson.mp3  │ ← Audio pour partager  
│ ma_chanson.svg  │ ← Partition
└─────────────────┘
```

---

## 🛠️ Dépannage

### "abc2midi : commande introuvable"
```bash
# Installer la dépendance manquante
odep install_abc2midi

# Installation manuelle (Ubuntu/Debian)
sudo apt-get install abcmidi
```

### "musescore3 : commande introuvable"
```bash
# Auto-installer MuseScore
odep install_musescore

# Installation manuelle
sudo apt-get install musescore3
```

### Pas de sortie audio
```bash
# Vérifier que le fichier MIDI a été créé
ls -la *.mid

# Installer outils audio
sudo apt-get install timidity fluid-soundfont-gm
```

### Erreurs de syntaxe ABC
```bash
# Vérifier la syntaxe avec abc2midi
abc2midi chanson.abc -o test.mid

# Erreurs communes :
# - En-têtes manquants (X:, T:, K:)
# - Notes invalides (utiliser octaves appropriées)
# - Barres de mesure manquantes
```

---

## 🎯 Exemples du Monde Réel

### Exemple 1 : Chanson Folk
```abc
X:1
T:Air Folk Irlandais
L:1/8
M:6/8
Q:3/8=120
K:D
|: A | d2 f e2 d | A2 F D2 E | F2 A A2 B | A3 A2 :|
|: f | a2 f d2 f | e2 c A2 c | d2 f e2 c | d3 d2 :|
```

```bash
oabc folk_irlandais.abc
# Parfait pour : Musique traditionnelle, sessions celtiques
```

### Exemple 2 : Standard Jazz
```abc
X:1
T:Ballade Jazz
L:1/4
M:4/4
Q:1/4=80
K:Bb
"Bbmaj7" B2 d2 | "Gm7" g2 f2 | "Cm7" e2 c2 | "F7" f4 |
"Dm7" d2 f2 | "Gm7" g2 b2 | "Cm7" c2 "F7" A2 | "Bbmaj7" B4 |
```

```bash
oabc ballade_jazz.abc
# Parfait pour : Grilles d'accords, ensembles jazz
```

### Exemple 3 : Pièce Classique
```abc
X:1
T:Menuet en Sol
L:1/8
M:3/4
Q:1/4=120
K:G
|: G2 A2 B2 | c4 B2 | A2 G2 F#2 | G6 :|
|: B2 c2 d2 | e4 d2 | c2 B2 A2 | B6 :|
```

```bash
oabc menuet.abc
# Parfait pour : Étude classique, pratique piano
```

---

## 🔥 Conseils Pro

### 1. Aperçu Rapide
```bash
# Juste générer MIDI pour écoute rapide
abc2midi ma_chanson.abc -o apercu.mid
```

### 2. Conversion par Lots d'Échantillons
```bash
# Essayer les échantillons inclus
cd samples/
for abc_file in *.abc; do
    oabc "$abc_file"
done
```

### 3. Workflows Personnalisés
```bash
# Créer un script de conversion
echo '#!/bin/bash
for file in "$@"; do
    echo "Conversion $file..."
    oabc "$file"
    echo "✓ Terminé : $file"
done' > convertir_tout.sh
chmod +x convertir_tout.sh

# L'utiliser
./convertir_tout.sh *.abc
```

### 4. Intégration avec DAW
```bash
# Convertir ABC en MIDI pour votre DAW
oabc ma_composition.abc
# Importer ma_composition.mid dans Logic/Pro Tools/Ableton
```

---

## 🎼 Guide de Qualité de Sortie

### Fichiers MIDI (.mid)
- **Utiliser pour :** Import DAW, lecture instrumentale
- **Qualité :** Précision parfaite des notes
- **Taille :** Très petite (1-10KB typiquement)

### Fichiers Audio (.mp3)
- **Utiliser pour :** Partage, démos, référence
- **Qualité :** Bonne pour démos
- **Taille :** Modérée (100KB-1MB)

### Partitions (.svg)
- **Utiliser pour :** Impression, partage de partitions
- **Qualité :** Vectoriel - redimensionne parfaitement
- **Taille :** Petite, nette à tout zoom

---

## 🚀 Exemples d'Intégration

### Avec Docker
```bash
# Exécuter dans environnement conteneurisé
(cd bin/testapp && dkrun)
# Dans le conteneur :
oabc /samples/Bov_i3.abc
```

### Avec Assistant IA
```bash
# Laisser l'IA aider à créer ABC, puis convertir
olca init
olca  # Demander à l'IA d'écrire notation ABC
# Sauvegarder sortie IA comme chanson.abc
oabc chanson.abc
```

### Avec Contrôle de Version
```bash
# Suivre vos compositions
git add *.abc
git commit -m "Ajouter nouvelle composition valse"
# Générer sorties
oabc *.abc
# Sorties vont dans .gitignore (fichiers binaires)
```

---

## 📚 Prochaines Étapes

1. **🤖 Essayer composition IA** → `04-assistant-ia-olca.md`
2. **🐳 Configuration professionnelle** → `05-configuration-docker.md`
3. **🔧 Workflows avancés** → `06-workflows-avances.md`

---

*🎵 OABC est votre passerelle du texte à la belle musique - maîtrisez cette commande et vous composerez comme un pro !*
