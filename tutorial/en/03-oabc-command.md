# 🎵 OABC Command - Your Musical Swiss Army Knife

## What is OABC?

**OABC** is the magic command that transforms your ABC notation into **everything** you need:
- 🎼 **Beautiful sheet music** (SVG/JPG)
- 🎵 **MIDI files** for playback
- 🔊 **MP3 audio** files
- ⚡ **All in one command!**

---

## 🚀 Basic Usage

### Simple Conversion
```bash
# Convert ABC file to everything
oabc my_song.abc
```

**What you get:**
- `my_song.mid` - MIDI file
- `my_song.mp3` - Audio file
- `my_song.svg` - Sheet music (vector)

### Check All Dependencies
```bash
# Make sure everything is installed
odep install_musescore
odep install_abc2midi  
odep install_imagemagick
```

---

## 🎯 Step-by-Step Example

### 1. Create Your ABC File
Create `waltz.abc`:
```abc
X:1
T:Simple Waltz
L:1/8
M:3/4
Q:1/4=120
K:C
|: C2 E2 G2 | c4 G2 | F2 A2 c2 | G6 :|
|: e2 d2 c2 | B2 A2 G2 | F2 E2 D2 | C6 :|
```

### 2. Convert It
```bash
oabc waltz.abc
```

### 3. Check Your Results
```bash
ls -la waltz.*
# waltz.abc  - Your original ABC notation
# waltz.mid  - MIDI file for instruments/DAWs
# waltz.mp3  - Audio for sharing/listening
# waltz.svg  - Beautiful sheet music
```

---

## 🔥 Advanced Features

### Different Output Formats
```bash
# Get JPG instead of SVG for sheet music
oabc my_song.abc --format jpg

# Specify custom output directory
oabc my_song.abc --output /path/to/output/
```

### Batch Processing
```bash
# Convert all ABC files in current directory
for file in *.abc; do
    oabc "$file"
done
```

### Quality Settings
```bash
# High-quality audio export
oabc my_song.abc --audio-quality high

# Custom MIDI velocity
oabc my_song.abc --velocity 80
```

---

## 🎼 What Happens Under the Hood

When you run `oabc my_song.abc`, here's the magic:

1. **🔍 Parse ABC** - Reads your ABC notation
2. **🎵 Generate MIDI** - Uses `abc2midi` to create MIDI
3. **🎼 Create Sheet Music** - Uses `musescore3` for beautiful scores
4. **🔊 Generate Audio** - Converts MIDI to MP3
5. **✨ Polish Output** - Optimizes all formats

```
my_song.abc
     ↓
  [OABC Magic]
     ↓
┌─────────────────┐
│ my_song.mid     │ ← MIDI for DAWs
│ my_song.mp3     │ ← Audio for sharing  
│ my_song.svg     │ ← Sheet music
└─────────────────┘
```

---

## 🛠️ Troubleshooting

### Common Issues

#### "Command not found: oabc"
```bash
# Solution: Install the package
pip install orpheuspypractice
```

#### "musescore3: command not found"
```bash
# Solution: Install dependencies
odep install_musescore
```

#### "No audio output"
```bash
# Check dependencies
odep is_musescore_installed
odep is_abc2midi_installed
odep is_imagemagick_installed
```

#### "Permission denied"
```bash
# Fix file permissions
chmod +x *.abc
```

---

## 🎯 Real-World Examples

### Example 1: Folk Song
```abc
X:1
T:Irish Folk Tune
L:1/8
M:6/8
Q:3/8=120
K:D
|: A | d2 f e2 d | A2 F D2 E | F2 A A2 B | A3 A2 :|
|: f | a2 f d2 f | e2 c A2 c | d2 f e2 c | d3 d2 :|
```

```bash
oabc irish_folk.abc
# Perfect for: Traditional music, Celtic sessions
```

### Example 2: Jazz Standard
```abc
X:1
T:Jazz Ballad
L:1/4
M:4/4
Q:1/4=80
K:Bb
"Bbmaj7" B2 d2 | "Gm7" g2 f2 | "Cm7" e2 c2 | "F7" f4 |
"Dm7" d2 f2 | "Gm7" g2 b2 | "Cm7" c2 "F7" A2 | "Bbmaj7" B4 |
```

```bash
oabc jazz_ballad.abc
# Perfect for: Lead sheets, jazz ensembles
```

### Example 3: Classical Piece
```abc
X:1
T:Minuet in G
L:1/8
M:3/4
Q:1/4=120
K:G
|: G2 A2 B2 | c4 B2 | A2 G2 F#2 | G6 :|
|: B2 c2 d2 | e4 d2 | c2 B2 A2 | B6 :|
```

```bash
oabc minuet.abc
# Perfect for: Classical study, piano practice
```

---

## 🔄 MIDI → ABC Conversion

**New Feature!** You can also convert existing MIDI files to ABC notation!

### Simple MIDI → ABC Conversion
```bash
# Convert a MIDI file to ABC notation
midi2abc song.mid

# Save to a file
midi2abc song.mid > song.abc
```

### Practical Example
```bash
# Example with an existing MIDI file
cd jerry-music/
midi2abc 250605.mid > my_conversion.abc

# Check the result
cat my_conversion.abc
# You get complete ABC notation!
```

### Bidirectional Workflow
```bash
# Complete workflow: MIDI ↔ ABC
midi2abc original.mid > from_midi.abc    # MIDI → ABC
oabc from_midi.abc                       # ABC → MIDI + MP3 + Sheet Music

# Perfect for:
# ✅ Analyzing existing MIDI files
# ✅ Editing music in text format  
# ✅ Creating sheet music from MIDI
# ✅ Learning ABC notation
```

### Advanced midi2abc Options
```bash
# Useful options
midi2abc -t song.mid        # Show tracks only
midi2abc -c 1 song.mid      # Channel 1 only
midi2abc -Q 0 song.mid      # No tempo in output
midi2abc -x song.mid        # Extended ABC format
```

---

## 🔥 Pro Tips

### 1. Quick Preview
```bash
# Just generate MIDI for quick listening
abc2midi my_song.abc -o preview.mid
```

### 2. Batch Convert Samples
```bash
# Try the included samples
cd samples/
for abc_file in *.abc; do
    oabc "$abc_file"
done
```

### 3. Custom Workflows
```bash
# Create a conversion script
echo '#!/bin/bash
for file in "$@"; do
    echo "Converting $file..."
    oabc "$file"
    echo "✓ Done: $file"
done' > convert_all.sh
chmod +x convert_all.sh

# Use it
./convert_all.sh *.abc
```

### 4. Integration with DAWs
```bash
# Convert ABC to MIDI for your DAW
oabc my_composition.abc
# Import my_composition.mid into Logic/Pro Tools/Ableton
```

---

## 🎼 Output Quality Guide

### MIDI Files (.mid)
- **Use for:** DAW import, instrument playback
- **Quality:** Perfect note accuracy
- **Size:** Very small (1-10KB typically)

### Audio Files (.mp3)
- **Use for:** Sharing, demos, reference
- **Quality:** Good for demos
- **Size:** Moderate (100KB-1MB)

### Sheet Music (.svg)
- **Use for:** Printing, sharing scores
- **Quality:** Vector - scales perfectly
- **Size:** Small, crisp at any zoom

---

## 🚀 Integration Examples

### With Docker
```bash
# Run in containerized environment
(cd bin/testapp && dkrun)
# Inside container:
oabc /samples/Bov_i3.abc
```

### With AI Assistant
```bash
# Let AI help create ABC, then convert
olca init
olca  # Ask AI to write ABC notation
# Save AI output as song.abc
oabc song.abc
```

### With Version Control
```bash
# Track your compositions
git add *.abc
git commit -m "Add new waltz composition"
# Generate outputs
oabc *.abc
# Outputs go in .gitignore (binary files)
```

---

## 📚 Next Steps

1. **🤖 Try AI composition** → `04-olca-ai-assistant.md`
2. **🐳 Professional setup** → `05-docker-setup.md`
3. **🔧 Advanced workflows** → `06-advanced-workflows.md`

---

*🎵 OABC is your gateway from text to beautiful music - master this command and you'll be composing like a pro!*
