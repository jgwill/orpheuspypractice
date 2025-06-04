# 🎼 ABC Notation Mastery Guide

## What is ABC Notation?

**ABC Notation** is a simple text format for writing music. Think of it as "code for composers" - you write music using letters and symbols, then convert it to beautiful sheet music and audio!

---

## 🎯 Basic Structure

Every ABC file has this structure:

```abc
X:1                    # Reference number
T:Song Title          # Title
L:1/8                 # Default note length (eighth note)
M:4/4                 # Time signature (4/4 time)
Q:1/4=120            # Tempo (120 BPM)
K:C                  # Key signature (C major)

# Your music notes go here
C D E F G A B c
```

---

## 🎵 Notes and Octaves

| ABC | Note | Octave |
|-----|------|--------|
| `C, D, E,` | C D E | Lower octave |
| `C D E F G A B` | C D E F G A B | Middle octave |
| `c d e f g a b` | C D E F G A B | Higher octave |
| `c' d' e'` | C D E | Even higher |

**Example:**
```abc
X:1
T:Octave Demo
L:1/4
M:4/4
K:C
C, D, E, F, | C D E F | c d e f | c' d' e' f' |
```

---

## ⏱️ Note Lengths

| Symbol | Duration | Name |
|--------|----------|------|
| `C` | Default length | (set by L:) |
| `C2` | Double length | Half note |
| `C4` | Quadruple | Whole note |
| `C/2` | Half length | Sixteenth |
| `C/4` | Quarter length | Thirty-second |

**Example:**
```abc
X:1
T:Rhythm Demo
L:1/8
M:4/4
K:C
C4 | C2 C2 | C C C C | C/2 C/2 C/2 C/2 C C |
```

---

## 🎯 Chords and Harmony

### Simple Chords
```abc
X:1
T:Chord Example
L:1/4
M:4/4
K:C
[CEG] [DFA] [EGB] [FAc] |
```

### Chord Symbols (for lead sheets)
```abc
X:1
T:Jazz Style
L:1/4
M:4/4
K:C
"C" C2 E2 | "F" F2 A2 | "G7" G2 B2 | "C" c4 |
```

---

## 🎭 Advanced Features

### Repeats and Structure
```abc
X:1
T:Song Structure
L:1/8
M:4/4
K:C
|: C D E F | G A B c :|    # Repeat this section
|1 c B A G :|2 c2 z2 |     # 1st/2nd endings
```

### Grace Notes and Ornaments
```abc
X:1
T:Ornaments
L:1/8
M:4/4
K:C
{c}D2 E2 | ~F2 G2 | .A2 B2 | c4 |
```

### Ties and Slurs
```abc
X:1
T:Connections
L:1/8
M:4/4
K:C
C2-C2 | (D E F G) | A2 B2 | c4 |
```

---

## 🔥 Real-World Examples

### Folk Song Pattern
```abc
X:1
T:Irish Jig
L:1/8
M:6/8
K:D
|: A | d2 A f2 d | e2 c A2 F | G2 E F2 D | E3 F2 A |
d2 A f2 d | e2 c A2 c | d2 f e2 c | d3 d2 :|
```

### Jazz Standard
```abc
X:1
T:Jazz Ballad
L:1/4
M:4/4
Q:1/4=80
K:C
"Cmaj7" c2 e2 | "Am7" a2 g2 | "Dm7" f2 d2 | "G7" g4 |
"Em7" e2 g2 | "Am7" a2 c'2 | "Dm7" f2 "G7" d2 | "Cmaj7" c4 |
```

### Classical Style
```abc
X:1
T:Minuet Style
L:1/8
M:3/4
Q:1/4=120
K:G
|: G2 A2 B2 | c4 B2 | A2 G2 F2 | G6 :|
|: d2 c2 B2 | A4 G2 | F2 E2 D2 | G6 :|
```

---

## 🛠️ Pro Tips

### 1. Time Signatures
```abc
M:4/4     # Standard time
M:3/4     # Waltz time
M:6/8     # Jig time
M:2/4     # March time
```

### 2. Key Signatures
```abc
K:C       # C major (no sharps/flats)
K:G       # G major (1 sharp)
K:F       # F major (1 flat)
K:Am      # A minor
K:Em      # E minor
```

### 3. Tempo Markings
```abc
Q:1/4=60     # Slow (60 BPM)
Q:1/4=120    # Moderate
Q:1/4=160    # Fast
Q:"Allegro"  # Text marking
```

### 4. Comments and Organization
```abc
% This is a comment
X:1
T:My Song
% Set up the basics
L:1/8
M:4/4
K:C
% Main melody
C D E F | G A B c |
```

---

## 🎯 Practice Exercises

### Exercise 1: Scale
Create a C major scale:
```abc
X:1
T:C Major Scale
L:1/4
M:4/4
K:C
C D E F | G A B c | c B A G | F E D C |
```

### Exercise 2: Simple Song
```abc
X:1
T:Twinkle Twinkle
L:1/4
M:4/4
K:C
C C G G | A A G2 | F F E E | D D C2 |
G G F F | E E D2 | G G F F | E E D2 |
```

### Exercise 3: With Chords
```abc
X:1
T:Simple Progression
L:1/4
M:4/4
K:C
"C" C2 E2 | "Am" A2 c2 | "F" F2 A2 | "G" G4 |
"C" c2 G2 | "Am" A2 E2 | "F" F2 "G" G2 | "C" C4 |
```

---

## 🚀 Convert Your ABC

Once you've written your ABC notation:

```bash
# Save as song.abc, then convert:
oabc song.abc

# You get:
# - song.mid (MIDI)
# - song.mp3 (Audio)  
# - song.svg (Sheet music)
```

---

## 📚 Next Steps

1. **🎵 Try the oabc command** → `03-oabc-command.md`
2. **🤖 Get AI help** → `04-olca-ai-assistant.md`
3. **🔧 Advanced workflows** → `06-advanced-workflows.md`

---

*🎼 ABC notation is like learning a musical programming language - once you know it, you can write any music imaginable!*
