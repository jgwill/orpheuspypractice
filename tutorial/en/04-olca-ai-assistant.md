# 🤖 OLCA - Your AI Music Composition Assistant

## What is OLCA?

**OLCA** (Orpheus Langchain CLI Assistant) is your **personal AI composer** that can:
- 🎼 **Generate ABC notation** from musical descriptions
- 🔍 **Analyze existing compositions** 
- 💡 **Suggest improvements** and variations
- 🛠️ **Execute shell commands** to create complete musical workflows
- 📚 **Learn from your feedback** and preferences

> ⚠️ **Note:** OLCA is experimental and can execute system commands - use with caution!

---

## 🚀 Getting Started

### 1. Initialize OLCA
```bash
# Create your AI assistant configuration
olca init
```

This creates `olca.yml` with your settings:
```yaml
api_keyname: OPENAI_API_KEY_olca
model_name: gpt-4o-mini
recursion_limit: 300
temperature: 0.0
human: true
tracing: true
system_instructions: You focus on musical composition and helping with ABC notation.
```

### 2. Set Your OpenAI API Key
```bash
# Set your API key (get one from OpenAI)
export OPENAI_API_KEY_olca="your-api-key-here"
```

### 3. Start Your AI Session
```bash
# Launch the interactive assistant
olca
```

---

## 🎯 Musical Composition Examples

### Example 1: Generate a Folk Song
```
You: "Create a simple Irish folk tune in D major, 6/8 time"

OLCA: I'll create an Irish folk tune for you...
[Creates ABC file automatically]

X:1
T:Irish Folk Tune
L:1/8
M:6/8
Q:3/8=120
K:D
|: A | d2 f e2 d | A2 F D2 E | F2 A A2 B | A3 A2 :|
|: f | a2 f d2 f | e2 c A2 c | d2 f e2 c | d3 d2 :|
```

### Example 2: Analyze and Improve
```
You: "Analyze this ABC and suggest improvements: [paste your ABC]"

OLCA: Looking at your composition, I notice:
- The melody could use more variation in measures 3-4
- Consider adding chord symbols for accompaniment
- The ending could be stronger

Here's an improved version: [generates enhanced ABC]
```

### Example 3: Complete Workflow
```
You: "Create a jazz ballad and convert it to all formats"

OLCA: I'll create a jazz ballad and convert it for you...
[Generates ABC, then runs:]
oabc jazz_ballad.abc

Result: jazz_ballad.mid, jazz_ballad.mp3, jazz_ballad.svg created!
```

---

## 🔥 Advanced Features

### Learning Mode
OLCA learns from your interactions and stores knowledge in:
- `.olca/instructions.md` - Your personal style guide
- `.olca-db.json` - Learned patterns and preferences

### Trace Mode
```bash
# Enable detailed tracing for debugging
olca --tracing
```

### Mathematical Mode
```bash
# Add mathematical capabilities for music theory
olca --math
```

### Configuration Options
```yaml
# In olca.yml - customize behavior
human: true              # Interactive mode
recursion_limit: 300     # How deep AI can think
temperature: 0.0         # Creativity (0=focused, 1=creative)
tracing: true           # Debug output
```

---

## 🎼 Real-World Workflows

### Workflow 1: Song Development
```bash
# Start with idea
olca
# You: "I want to write a melancholy waltz in Am"
# AI generates basic structure

# Refine and iterate
# You: "Make the B section more hopeful"
# AI modifies and saves variations

# Convert final version
# AI automatically runs: oabc my_waltz.abc
```

### Workflow 2: Style Analysis
```bash
# Analyze Bach-style counterpoint
olca
# You: "Analyze this ABC for baroque characteristics and suggest a countermelody"
# AI provides detailed analysis and creates companion voice
```

### Workflow 3: Educational Tool
```bash
# Learn music theory interactively
olca
# You: "Explain circle of fifths and create examples in ABC"
# AI teaches concepts with practical examples
```

---

## 🛠️ Shell Integration

OLCA can execute commands to create complete workflows:

### Automatic Conversion
```
You: "Create a blues progression and convert to audio"

OLCA executes:
1. Generates blues ABC notation
2. Saves as blues.abc
3. Runs: oabc blues.abc
4. Reports: "Created blues.mid, blues.mp3, blues.svg"
```

### Batch Processing
```
You: "Convert all ABC files in samples/ folder"

OLCA executes:
for file in samples/*.abc; do
    oabc "$file"
done
```

### Git Integration
```
You: "Save my composition to git with proper commit message"

OLCA executes:
git add my_song.abc
git commit -m "Add new Celtic ballad composition"
```

---

## 🔥 Pro Tips

### 1. Give Context
```
Instead of: "Write a song"
Try: "Write a 16-bar blues in E major with a walking bass line feeling"
```

### 2. Iterative Development
```
"Start with a simple melody"
"Add harmony"
"Make the bridge more interesting"
"Add ornamentation to the final repeat"
```

### 3. Use Musical Terms
```
"Create a Dorian mode melody"
"Add a ii-V-I progression"
"Use call-and-response phrasing"
```

### 4. Reference Existing Work
```
"Create something in the style of Celtic music"
"Use the chord progression from 'Autumn Leaves'"
"Write counterpoint like Bach would"
```

---

## 🎯 Common Use Cases

### For Composers
- **Sketch ideas quickly** - Turn hummed melodies into ABC
- **Explore variations** - Generate multiple versions of themes  
- **Overcome writer's block** - Get AI suggestions for stuck passages

### For Students
- **Learn by example** - Generate pieces in specific styles
- **Understand theory** - Ask for explanations with musical examples
- **Practice analysis** - Have AI break down complex pieces

### For Teachers
- **Create exercises** - Generate sight-reading materials
- **Demonstrate concepts** - Show theory with immediate audio examples
- **Curriculum support** - Create examples for specific lessons

---

## 🛡️ Safety and Best Practices

### Security Notes
- ⚠️ OLCA can execute shell commands - review before running
- 🔒 Keep API keys secure and private
- 💾 Backup important compositions before experimenting

### Best Practices
```bash
# Always review generated commands
# Start with simple requests
# Use version control for compositions
# Keep olca.yml configuration backed up
```

### Error Recovery
```bash
# If OLCA gets stuck
Ctrl+C  # Stop current operation

# Reset if needed
rm -rf .olca/  # Clears learned patterns
olca init      # Restart fresh
```

---

## 🎼 Integration with Other Tools

### With Docker
```bash
# Use OLCA in containerized environment
(cd bin/testapp && dkrun)
# Inside container:
olca
```

### With Version Control
```bash
# OLCA can help with git workflows
# You: "Create a new composition and commit it properly"
# AI handles the entire process
```

### With OABC Pipeline
```bash
# Seamless integration
# OLCA creates ABC → automatically converts with OABC
# Full pipeline from idea to audio/sheet music
```

---

## 🆘 Troubleshooting

### Common Issues

#### "No module named openai"
```bash
# Install dependencies
pip install langchain openai
```

#### "API key not found"
```bash
# Set your API key
export OPENAI_API_KEY_olca="sk-your-key-here"
# Or add to your shell profile
echo 'export OPENAI_API_KEY_olca="sk-your-key-here"' >> ~/.bashrc
```

#### "Recursion limit reached"
```bash
# Increase limit in olca.yml
recursion_limit: 500
```

#### "Permission denied on shell commands"
```bash
# Review and approve shell operations
# OLCA will ask for confirmation in human mode
```

---

## 📚 Next Steps

1. **🐳 Professional setup** → `05-docker-setup.md`
2. **🔧 Advanced workflows** → `06-advanced-workflows.md`
3. **📖 Storytelling** → `07-ai-storytelling.md`

---

*🤖 OLCA transforms the way you create music - from idea to finished composition with AI assistance every step of the way!*
