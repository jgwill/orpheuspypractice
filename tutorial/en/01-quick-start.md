# 🚀 Quick Start Guide - OrpheusPyPractice

## What is OrpheusPyPractice?

**OrpheusPyPractice** is a complete musical toolkit that lets you:
- ✍️ Write music in simple ABC notation
- 🎵 Convert to MIDI, MP3, and beautiful sheet music
- 🤖 Generate compositions with AI assistance
- 🐳 Run everything in professional Docker containers

---

## ⚡ 5-Minute Setup

### 1. Install the Package
```bash
pip install orpheuspypractice
```

### 2. Test the Installation
```bash
# Check if everything is working
oabc --help
```

### 3. Create Your First Song
Create a file called `my_song.abc`:
```abc
X:1
T:My First Song
L:1/8
M:4/4
Q:1/4=120
K:C
|: C2 D2 E2 F2 | G2 A2 B2 c2 | c2 B2 A2 G2 | F2 E2 D2 C2 :|
```

### 4. Convert to Everything!
```bash
# This creates MIDI + MP3 + Sheet Music automatically!
oabc my_song.abc
```

**🎉 Congratulations!** You now have:
- `my_song.mid` - MIDI file
- `my_song.mp3` - Audio file  
- `my_song.svg` - Beautiful sheet music

---

## 🎯 What You Get

| Command | What it does | Output |
|---------|-------------|---------|
| `oabc` | Convert ABC → Everything | MIDI + MP3 + Sheet Music |
| `olca` | AI Music Assistant | Interactive composition help |
| `ohfi` | AI Music Generation | Generate new melodies |
| `odep` | Install Dependencies | Setup musical tools |

---

## 🔥 Pro Tips

### Want AI Help?
```bash
# Initialize the AI assistant
olca init

# Start composing with AI
olca
```

### Docker Power User?
```bash
# Run in professional container
(cd bin/testapp && dkrun)
```

### Need Dependencies?
```bash
# Auto-install everything needed
odep install_musescore
odep install_abc2midi
odep install_imagemagick
```

---

## 🎼 Sample ABC Files

Try these examples from the `samples/` folder:

**Simple Folk Tune:**
```abc
X:1
T:Tempo Change
L:1/8
M:2/4
Q:1/4=85
K:Amin
|:"Am" A2 EA | EA EA | c2 Ac | Ac Ac | e2 ce |"Dm" d2 Bd |1"Am" c2 Ac |"E7" B2 e2 :|
```

**More Complex:**
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

## 🆘 Need Help?

| Problem | Solution |
|---------|----------|
| Command not found | `pip install orpheuspypractice` |
| No sound output | `odep install_musescore` |
| Missing dependencies | Run `odep install_abc2midi` |
| Docker issues | Check Docker is running |

---

## 🚀 Next Steps

1. **📖 Learn ABC Notation** → `02-abc-notation.md`
2. **🤖 Try AI Assistant** → `04-olca-ai-assistant.md`
3. **🐳 Docker Setup** → `05-docker-setup.md`

**Ready to become a musical coding wizard?** 🧙‍♂️🎵

---

*💡 This is just the beginning! OrpheusPyPractice can do much more - explore the other tutorials to unlock its full potential!*
