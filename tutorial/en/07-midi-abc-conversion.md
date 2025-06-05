# 🔄 MIDI ↔ ABC Guide - Bidirectional Conversion

## Overview

OrpheusPyPractice enables conversion in both directions:
- **ABC → MIDI/MP3/Sheet Music** with `oabc`
- **MIDI → ABC** with `midi2abc`

---

## 🎵 MIDI → ABC (Analyzing existing files)

### Simple Conversion
```bash
# Convert a MIDI file to ABC notation
midi2abc song.mid

# Save to a file
midi2abc song.mid > song.abc
```

### Practical Example
```bash
# Navigate to folder with MIDI files
cd jerry-music/

# Convert the example MIDI file
midi2abc 250605.mid > converted_melody.abc

# View the result
cat converted_melody.abc
```

**Result obtained:**
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

## 🎼 ABC → Everything (Complete generation)

### Once you have ABC notation
```bash
# Generate MIDI + MP3 + Sheet Music
oabc converted_melody.abc

# You get:
# - converted_melody.mid  (MIDI)
# - converted_melody.mp3  (Audio)
# - converted_melody.svg  (Sheet Music)
```

---

## 🔄 Complete Workflow

### Scenario: Analyze and improve a MIDI file

```bash
# 1. Start from existing MIDI
midi2abc original.mid > analysis.abc

# 2. Edit the ABC notation (with your favorite editor)
nano analysis.abc

# 3. Regenerate all formats
oabc analysis.abc

# 4. Compare original vs modified
# original.mid vs analysis.mid
```

### Practical use cases

**📚 Learning:**
```bash
# Analyze how a melody is notated
midi2abc complex_melody.mid > learning.abc
cat learning.abc  # See ABC structure
```

**✏️ Editing:**
```bash
# Start from MIDI, edit it, regenerate
midi2abc base.mid > editable.abc
# [Edit editable.abc]
oabc editable.abc
```

**🎹 DAW Integration:**
```bash
# Export from your DAW as MIDI
# Convert to ABC for analysis/sheet music
midi2abc daw_export.mid > daw_analysis.abc
oabc daw_analysis.abc  # Get clean sheet music
```

---

## ⚙️ Advanced Options

### midi2abc Options
```bash
midi2abc -t file.mid        # Show available tracks
midi2abc -c 1 file.mid      # Extract channel 1 only
midi2abc -Q 0 file.mid      # No tempo info in ABC
midi2abc -x file.mid        # Extended ABC format
```

### Multi-track Workflow
```bash
# See available tracks
midi2abc -t multichannel.mid

# Extract each track separately
midi2abc -c 1 multichannel.mid > track1.abc
midi2abc -c 2 multichannel.mid > track2.abc

# Convert each track
oabc track1.abc
oabc track2.abc
```

---

## 🎯 Typical Use Cases

| Goal | Commands | Result |
|------|----------|--------|
| Analyze a MIDI | `midi2abc song.mid` | See ABC notation |
| Create sheet music from MIDI | `midi2abc song.mid > song.abc && oabc song.abc` | MIDI → Sheet Music |
| Edit existing MIDI | `midi2abc → edit ABC → oabc` | Modified version |
| Learn ABC notation | `midi2abc examples/*.mid` | See how to notate |

---

## 💡 Pro Tips

1. **Always save**: `midi2abc file.mid > file.abc`
2. **Check before editing**: Look at generated ABC before modifications
3. **Test immediately**: Run `oabc` after each ABC modification
4. **Use options**: `-c` for specific tracks, `-Q 0` for clean tempo

---

*🎵 With this bidirectional approach, you can analyze any MIDI file and create professional sheet music!*
