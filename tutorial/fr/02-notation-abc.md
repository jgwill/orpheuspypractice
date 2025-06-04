# 🎼 Guide de Maîtrise de la Notation ABC

## Qu'est-ce que la Notation ABC ?

**La Notation ABC** est un format texte simple pour écrire de la musique. Pensez-y comme du "code pour compositeurs" - vous écrivez de la musique en utilisant des lettres et des symboles, puis la convertissez en belles partitions et audio !

---

## 🎯 Structure de Base

Chaque fichier ABC a cette structure :

```abc
X:1                    # Numéro de référence
T:Titre de la Chanson # Titre
L:1/8                 # Longueur de note par défaut (croche)
M:4/4                 # Signature rythmique (mesure 4/4)
Q:1/4=120            # Tempo (120 BPM)
K:C                  # Armature (Do majeur)

# Vos notes musicales vont ici
C D E F G A B c
```

---

## 🎵 Notes et Octaves

| ABC | Note | Octave |
|-----|------|--------|
| `C, D, E,` | C D E | Octave inférieur |
| `C D E F G A B` | C D E F G A B | Octave moyen |
| `c d e f g a b` | C D E F G A B | Octave supérieur |
| `c' d' e'` | C D E | Encore plus haut |

**Exemple :**
```abc
X:1
T:Démo Octaves
L:1/4
M:4/4
K:C
C, D, E, F, | C D E F | c d e f | c' d' e' f' |
```

---

## ⏱️ Longueurs de Notes

| Symbole | Durée | Nom |
|---------|-------|-----|
| `C` | Longueur par défaut | (définie par L:) |
| `C2` | Double longueur | Blanche |
| `C4` | Quadruple | Ronde |
| `C/2` | Moitié | Double-croche |
| `C/4` | Quart | Triple-croche |

**Exemple :**
```abc
X:1
T:Démo Rythme
L:1/8
M:4/4
K:C
C4 | C2 C2 | C C C C | C/2 C/2 C/2 C/2 C C |
```

---

## 🎯 Accords et Harmonie

### Accords Simples
```abc
X:1
T:Exemple d'Accord
L:1/4
M:4/4
K:C
[CEG] [DFA] [EGB] [FAc] |
```

### Symboles d'Accords (pour grilles d'accords)
```abc
X:1
T:Style Jazz
L:1/4
M:4/4
K:C
"C" C2 E2 | "F" F2 A2 | "G7" G2 B2 | "C" c4 |
```

---

## 🎭 Fonctionnalités Avancées

### Reprises et Structure
```abc
X:1
T:Structure de Chanson
L:1/8
M:4/4
K:C
|: C D E F | G A B c :|    # Répéter cette section
|1 c B A G :|2 c2 z2 |     # 1ère/2ème fins
```

### Notes d'Agrément et Ornements
```abc
X:1
T:Ornements
L:1/8
M:4/4
K:C
{c}D2 E2 | ~F2 G2 | .A2 B2 | c4 |
```

### Liaisons et Coulés
```abc
X:1
T:Connexions
L:1/8
M:4/4
K:C
C2-C2 | (D E F G) | A2 B2 | c4 |
```

---

## 🔥 Exemples du Monde Réel

### Motif de Chanson Folk
```abc
X:1
T:Gigue Irlandaise
L:1/8
M:6/8
K:D
|: A | d2 A f2 d | e2 c A2 F | G2 E F2 D | E3 F2 A |
d2 A f2 d | e2 c A2 c | d2 f e2 c | d3 d2 :|
```

### Standard Jazz
```abc
X:1
T:Ballade Jazz
L:1/4
M:4/4
Q:1/4=80
K:C
"Cmaj7" c2 e2 | "Am7" a2 g2 | "Dm7" f2 d2 | "G7" g4 |
"Em7" e2 g2 | "Am7" a2 c'2 | "Dm7" f2 "G7" d2 | "Cmaj7" c4 |
```

### Style Classique
```abc
X:1
T:Style Menuet
L:1/8
M:3/4
Q:1/4=120
K:G
|: G2 A2 B2 | c4 B2 | A2 G2 F2 | G6 :|
|: d2 c2 B2 | A4 G2 | F2 E2 D2 | G6 :|
```

---

## 🛠️ Conseils Pro

### 1. Signatures Rythmiques
```abc
M:4/4     # Temps standard
M:3/4     # Temps de valse
M:6/8     # Temps de gigue
M:2/4     # Temps de marche
```

### 2. Armatures
```abc
K:C       # Do majeur (pas de dièses/bémols)
K:G       # Sol majeur (1 dièse)
K:F       # Fa majeur (1 bémol)
K:Am      # La mineur
K:Em      # Mi mineur
```

### 3. Indications de Tempo
```abc
Q:1/4=60     # Lent (60 BPM)
Q:1/4=120    # Modéré
Q:1/4=160    # Rapide
Q:"Allegro"  # Indication textuelle
```

### 4. Commentaires et Organisation
```abc
% Ceci est un commentaire
X:1
T:Ma Chanson
% Configurer les bases
L:1/8
M:4/4
K:C
% Mélodie principale
C D E F | G A B c |
```

---

## 🎯 Exercices Pratiques

### Exercice 1 : Gamme
Créez une gamme de Do majeur :
```abc
X:1
T:Gamme de Do Majeur
L:1/4
M:4/4
K:C
C D E F | G A B c | c B A G | F E D C |
```

### Exercice 2 : Chanson Simple
```abc
X:1
T:Brille Brille Petite Étoile
L:1/4
M:4/4
K:C
C C G G | A A G2 | F F E E | D D C2 |
G G F F | E E D2 | G G F F | E E D2 |
```

### Exercice 3 : Avec Accords
```abc
X:1
T:Progression Simple
L:1/4
M:4/4
K:C
"C" C2 E2 | "Am" A2 c2 | "F" F2 A2 | "G" G2 B2 |
"C" c2 G2 | "Am" A2 E2 | "F" F2 "G" D2 | "C" C4 |
```

---

## 🚀 Convertir Votre ABC

Une fois que vous avez écrit votre notation ABC :

```bash
# Sauvegarder comme chanson.abc, puis convertir :
oabc chanson.abc

# Vous obtenez :
# - chanson.mid (MIDI)
# - chanson.mp3 (Audio)  
# - chanson.svg (Partition)
```

---

## 📚 Prochaines Étapes

1. **🎵 Essayer la commande oabc** → `03-commande-oabc.md`
2. **🤖 Obtenir l'aide IA** → `04-assistant-ia-olca.md`
3. **🔧 Workflows avancés** → `06-workflows-avances.md`

---

*🎼 La notation ABC est comme apprendre un langage de programmation musical - une fois que vous la connaissez, vous pouvez écrire n'importe quelle musique imaginable !*
