# 🔄 Guide MIDI ↔ ABC - Conversion Bidirectionnelle

## Vue d'ensemble

OrpheusPyPractice permet la conversion dans les deux sens :
- **ABC → MIDI/MP3/Partitions** avec `oabc`
- **MIDI → ABC** avec `midi2abc`

---

## 🎵 MIDI → ABC (Analyse de fichiers existants)

### Conversion Simple
```bash
# Convertir un fichier MIDI en notation ABC
midi2abc chanson.mid

# Sauvegarder dans un fichier
midi2abc chanson.mid > chanson.abc
```

### Exemple Pratique
```bash
# Naviguer vers le dossier avec des fichiers MIDI
cd jerry-music/

# Convertir le fichier MIDI d'exemple
midi2abc 250605.mid > melodie_convertie.abc

# Voir le résultat
cat melodie_convertie.abc
```

**Résultat obtenu :**
```abc
X: 1
T: from 250605.mid
M: 4/4
L: 1/8
Q:1/4=120
K:A % 3 sharps
V:1
%%MIDI program 0
z4 zA Bc| \
c4 z2 GF| \
F4 z4| \
z8|
```

---

## 🎼 ABC → Tout (Génération complète)

### Une fois que vous avez la notation ABC
```bash
# Générer MIDI + MP3 + Partitions
oabc melodie_convertie.abc

# Vous obtenez :
# - melodie_convertie.mid  (MIDI)
# - melodie_convertie.mp3  (Audio)
# - melodie_convertie.svg  (Partition)
```

---

## 🔄 Workflow Complet

### Scénario : Analyser et améliorer un fichier MIDI

```bash
# 1. Partir d'un MIDI existant
midi2abc original.mid > analyse.abc

# 2. Éditer la notation ABC (avec votre éditeur favori)
nano analyse.abc

# 3. Regénérer tous les formats
oabc analyse.abc

# 4. Comparer original vs modifié
# original.mid vs analyse.mid
```

### Cas d'usage pratiques

**📚 Apprentissage :**
```bash
# Analyser comment une mélodie est notée
midi2abc melodie_complexe.mid > apprentissage.abc
cat apprentissage.abc  # Voir la structure ABC
```

**✏️ Édition :**
```bash
# Partir d'un MIDI, l'éditer, regénérer
midi2abc base.mid > modifiable.abc
# [Éditer modifiable.abc]
oabc modifiable.abc
```

**🎹 DAW Integration :**
```bash
# Exporter de votre DAW en MIDI
# Convertir en ABC pour analyse/partitions
midi2abc export_daw.mid > analyse_daw.abc
oabc analyse_daw.abc  # Obtenir partitions propres
```

---

## ⚙️ Options Avancées

### Options midi2abc
```bash
midi2abc -t fichier.mid        # Afficher les pistes disponibles
midi2abc -c 1 fichier.mid      # Extraire seulement le canal 1
midi2abc -Q 0 fichier.mid      # Pas d'info tempo dans l'ABC
midi2abc -x fichier.mid        # Format ABC étendu
```

### Workflow avec pistes multiples
```bash
# Voir les pistes disponibles
midi2abc -t multichannel.mid

# Extraire chaque piste séparément
midi2abc -c 1 multichannel.mid > piste1.abc
midi2abc -c 2 multichannel.mid > piste2.abc

# Convertir chaque piste
oabc piste1.abc
oabc piste2.abc
```

---

## 🎯 Cas d'usage typiques

| Objectif | Commandes | Résultat |
|----------|-----------|----------|
| Analyser un MIDI | `midi2abc song.mid` | Voir la notation ABC |
| Créer partitions depuis MIDI | `midi2abc song.mid > song.abc && oabc song.abc` | MIDI → Partitions |
| Éditer un MIDI existant | `midi2abc → éditer ABC → oabc` | Version modifiée |
| Apprendre l'ABC | `midi2abc exemples/*.mid` | Voir comment noter |

---

## 💡 Conseils Pro

1. **Toujours sauvegarder** : `midi2abc fichier.mid > fichier.abc`
2. **Vérifier avant d'éditer** : Regarder l'ABC généré avant modifications
3. **Tester immédiatement** : `oabc` après chaque modification ABC
4. **Utiliser les options** : `-c` pour pistes spécifiques, `-Q 0` pour tempo clean

---

*🎵 Avec cette approche bidirectionnelle, vous pouvez analyser n'importe quel MIDI et créer des partitions professionnelles !*
