# 🚀 Guide de Démarrage Rapide - OrpheusPyPractice

## Qu'est-ce qu'OrpheusPyPractice ?

**OrpheusPyPractice** est une boîte à outils musicale complète qui vous permet de :
- ✍️ Écrire de la musique en notation ABC simple
- 🎵 Convertir en MIDI, MP3 et belles partitions
- 🤖 Générer des compositions avec l'assistance IA
- 🐳 Exécuter tout dans des conteneurs Docker professionnels

---

## ⚡ Configuration en 5 Minutes

### 1. Installer le Package
```bash
pip install orpheuspypractice
```

### 2. Tester l'Installation
```bash
# Vérifier que tout fonctionne
oabc --help
```

### 3. Créer Votre Première Chanson
Créez un fichier appelé `ma_chanson.abc` :
```abc
X:1
T:Ma Première Chanson
L:1/8
M:4/4
Q:1/4=120
K:C
|: C2 D2 E2 F2 | G2 A2 B2 c2 | c2 B2 A2 G2 | F2 E2 D2 C2 :|
```

### 4. Convertir en Tout !
```bash
# Une commande magique qui crée MIDI + MP3 + Partition
oabc ma_chanson.abc

# Vous obtenez :
# ma_chanson.mid  ← Fichier MIDI pour instruments
# ma_chanson.mp3  ← Audio pour partager
# ma_chanson.svg  ← Belle partition musicale
```

---

## 🎯 Ce Que Vous Obtenez

| Commande | Ce qu'elle fait | Sortie |
|----------|----------------|---------|
| `oabc` | Convertir ABC → Tout | MIDI + MP3 + Partition |
| `olca` | Assistant Musical IA | Aide composition interactive |
| `ohfi` | Génération Musicale IA | Générer nouvelles mélodies |
| `odep` | Installer Dépendances | Configurer outils musicaux |

---

## 🔥 Conseils Pro

### Vous Voulez l'Aide IA ?
```bash
# Initialiser l'assistant IA
olca init

# Commencer à composer avec l'IA
olca
```

### Utilisateur Docker Avancé ?
```bash
# Exécuter dans un conteneur professionnel
(cd bin/testapp && dkrun)
```

### Besoin de Dépendances ?
```bash
# Auto-installer tout ce qui est nécessaire
odep install_musescore
odep install_abc2midi
odep install_imagemagick
```

---

## 🎼 Exemples de Fichiers ABC

Essayez ces exemples du dossier `samples/` :

**Air Folk Simple :**
```abc
X:1
T:Changement de Tempo
L:1/8
M:2/4
Q:1/4=85
K:Amin
|:"Am" A2 EA | EA EA | c2 Ac | Ac Ac | e2 ce |"Dm" d2 Bd |1"Am" c2 Ac |"E7" B2 e2 :|
```

**Plus Complexe :**
```abc
X:1
T:i 3
L:1/8
Q:1/4=115
M:4/4
K:A
|: E2 |"A" A2 cA eAfA |"A" eAfA ecBc |"A" A2 cA eAfA |"Bm" ecBc"D" AFEF |"A" A2 cA eAfA | "A" eAfA ecBc :|
```

---

## 🆘 Besoin d'Aide ?

| Problème | Solution |
|----------|----------|
| Commande introuvable | `pip install orpheuspypractice` |
| Pas de sortie audio | `odep install_musescore` |
| Dépendances manquantes | Exécuter `odep install_abc2midi` |
| Problèmes Docker | Vérifier que Docker fonctionne |

---

## 🚀 Prochaines Étapes

1. **📖 Apprendre la Notation ABC** → `02-notation-abc.md`
2. **🤖 Essayer l'Assistant IA** → `04-assistant-ia-olca.md`
3. **🐳 Configuration Docker** → `05-configuration-docker.md`

**Prêt à devenir un magicien du codage musical ?** 🧙‍♂️🎵

---

*💡 Ce n'est que le début ! OrpheusPyPractice peut faire beaucoup plus - explorez les autres tutoriels pour débloquer tout son potentiel !*
