# 🛠️ Troubleshooting Guide - Common Issues & Solutions

## 🎯 Quick Problem Solver

**Having issues?** This guide covers the most common problems and their solutions. Most issues can be resolved in under 5 minutes!

---

## 🚨 Installation Issues

### "Command not found: oabc"

**Problem:** Package not installed or not in PATH
```bash
# Check if installed
pip list | grep orpheuspypractice

# If not found, install
pip install orpheuspypractice

# If still not found, try
pip install --user orpheuspypractice
export PATH="$HOME/.local/bin:$PATH"
```

### "Permission denied" errors

**Problem:** Insufficient permissions
```bash
# Don't use sudo with pip, use --user instead
pip install --user orpheuspypractice

# If using system Python, create virtual environment
python -m venv orpheus_env
source orpheus_env/bin/activate
pip install orpheuspypractice
```

### Package conflicts

**Problem:** Conflicting dependencies
```bash
# Create fresh environment
python -m venv fresh_orpheus
source fresh_orpheus/bin/activate
pip install --upgrade pip
pip install orpheuspypractice
```

---

## 🎵 ABC to Audio/Sheet Music Issues

### "abc2midi: command not found"

**Problem:** Missing abc2midi dependency
```bash
# Install missing dependency
odep install_abc2midi

# Check if installed
odep is_abc2midi_installed

# Manual install (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install abcmidi
```

### "musescore3: command not found"

**Problem:** MuseScore not installed
```bash
# Auto-install MuseScore
odep install_musescore

# Check installation
odep is_musescore_installed

# Manual install
sudo apt-get install musescore3
# or
flatpak install flathub org.musescore.MuseScore
```

### No audio output (silent MP3)

**Problem:** MIDI to audio conversion failing
```bash
# Check MIDI file was created
ls -la *.mid

# If MIDI exists but no MP3, check audio tools
which timidity
which fluidsynth

# Install audio synthesis
sudo apt-get install timidity fluid-soundfont-gm

# Try manual conversion
timidity song.mid -Ow -o song.wav
# Then convert WAV to MP3
```

### Sheet music generation fails

**Problem:** MuseScore GUI issues
```bash
# Check X11 forwarding (if using SSH)
echo $DISPLAY

# Use virtual display
export DISPLAY=:99
sudo Xvfb :99 -screen 0 1024x768x24 &

# Test MuseScore
musescore3 --help
```

---

## 🤖 OLCA AI Assistant Issues

### "OLCA configuration missing"

**Problem:** No olca.yml configuration
```bash
# Initialize OLCA
olca init -y

# Check configuration exists
ls -la olca.yml

# Manual configuration
cat > olca.yml << 'EOF'
api_keyname: OPENAI_API_KEY_olca
model_name: gpt-4o-mini
recursion_limit: 50
temperature: 0.0
human: true
tracing: false
system_instructions: "You are a helpful musical composition assistant."
user_input: "Help me create music."
EOF
```

### "API key not found"

**Problem:** OpenAI API key not configured
```bash
# Set API key in environment
export OPENAI_API_KEY_olca="your-api-key-here"

# Or add to .env file
echo "OPENAI_API_KEY_olca=your-api-key-here" >> .env

# Check if key is set
echo $OPENAI_API_KEY_olca
```

### "Recursion limit reached"

**Problem:** AI task too complex
```bash
# Increase recursion limit in olca.yml
sed -i 's/recursion_limit: [0-9]*/recursion_limit: 100/' olca.yml

# Or break down complex requests
# Instead of: "Create a symphony"
# Try: "Create a simple melody in C major"
```

### OLCA hangs or gets stuck

**Problem:** Complex request or network issues
```bash
# Stop OLCA
Ctrl+C

# Restart with simpler request
olca
# "Create a simple 8-bar melody"

# Check network connectivity
ping api.openai.com
```

---

## 🐳 Docker Issues

### "Cannot connect to Docker daemon"

**Problem:** Docker not running
```bash
# Start Docker service
sudo systemctl start docker

# Enable auto-start
sudo systemctl enable docker

# Add user to docker group
sudo usermod -aG docker $USER
# Log out and back in

# Test Docker
docker --version
```

### "Permission denied" in container

**Problem:** User permissions in container
```bash
# Check current user in container
cd bin/testapp && dkrun
whoami  # Should be 'jgi'

# Check file permissions
ls -la /app/

# If files not writable, fix locally
chmod -R 755 .
```

### X11 forwarding not working

**Problem:** GUI applications won't start
```bash
# Allow X11 connections
xhost +local:docker

# Check X11 socket
ls -la /tmp/.X11-unix/

# Start container with X11 properly mounted
cd bin/testapp
dkrun
# Should automatically mount X11
```

### Container won't start

**Problem:** Image or network issues
```bash
# Check if image exists
docker images | grep orpheus

# Pull latest image
docker pull jgwill/orpheus:testapp

# Check Docker logs
docker logs [container-id]

# Clean rebuild
cd bin/testapp
docker build -t jgwill/orpheus:testapp .
```

---

## 📁 File and Path Issues

### "File not found" errors

**Problem:** Incorrect file paths
```bash
# Check current directory
pwd

# List ABC files
ls -la *.abc

# Use absolute paths
oabc /full/path/to/song.abc

# Check file permissions
ls -la song.abc
```

### ABC file syntax errors

**Problem:** Invalid ABC notation
```bash
# Common syntax issues:

# Missing headers
X:1
T:Song Title
L:1/4
M:4/4
K:C

# Invalid notes (use proper octaves)
# Wrong: H I J
# Right: c d e

# Missing bar lines
# Wrong: C D E F G A B c
# Right: C D E F | G A B c |

# Check syntax with abc2midi
abc2midi song.abc -o test.mid
```

### Output files not generated

**Problem:** Conversion process fails silently
```bash
# Run with verbose output
oabc song.abc --verbose

# Check intermediate files
ls -la song.*

# Manual step-by-step conversion
abc2midi song.abc -o song.mid
musescore3 -o song.svg song.mid
timidity song.mid -Ow -o song.wav
```

---

## 🌐 Network and API Issues

### "Connection timeout" errors

**Problem:** Network connectivity
```bash
# Test internet connection
ping google.com

# Check firewall settings
sudo ufw status

# Test specific services
curl -I https://api.openai.com
```

### "Rate limit exceeded"

**Problem:** Too many API calls
```bash
# Wait before retrying
sleep 60

# Use different API key
export OPENAI_API_KEY_olca="backup-key"

# Reduce request frequency
# Space out OLCA commands
```

---

## 🔧 Advanced Troubleshooting

### Debug mode for detailed errors

```bash
# Enable Python debug mode
export PYTHONPATH=/path/to/orpheuspypractice/src
python -m pdb -m orpheuspypractice.olca

# Verbose logging
export DEBUG=1
olca

# Check system logs
journalctl -f | grep orpheus
```

### Clean slate reset

```bash
# Remove all configuration
rm -rf .olca/
rm -f olca.yml olca_config.yaml

# Reinstall package
pip uninstall orpheuspypractice
pip install orpheuspypractice

# Reinitialize
olca init -y
```

### System information for support

```bash
# Gather system info
cat > debug_info.txt << 'EOF'
System Information:
OS: $(lsb_release -d | cut -f2)
Python: $(python --version)
Pip: $(pip --version)
OrpheusPyPractice: $(pip show orpheuspypractice | grep Version)
Docker: $(docker --version 2>/dev/null || echo "Not installed")

Musical Tools:
abc2midi: $(abc2midi 2>&1 | head -1 || echo "Not found")
musescore3: $(musescore3 --version 2>/dev/null || echo "Not found")
timidity: $(timidity --version 2>&1 | head -1 || echo "Not found")
EOF
```

---

## 🆘 Getting Help

### Check logs first

```bash
# OLCA logs
ls -la .olca/
cat .olca/instructions.txt

# System logs
tail -f /var/log/syslog | grep -i orpheus
```

### Community resources

| Resource | URL | Description |
|----------|-----|-------------|
| **GitHub Issues** | `github.com/jgwill/orpheuspypractice/issues` | Bug reports & feature requests |
| **Documentation** | `github.com/jgwill/orpheuspypractice/wiki` | Detailed documentation |
| **Examples** | `samples/` folder | Working ABC examples |

### Before reporting bugs

1. **Update to latest version:**
   ```bash
   pip install --upgrade orpheuspypractice
   ```

2. **Try minimal example:**
   ```bash
   echo 'X:1
   T:Test
   L:1/4
   M:4/4
   K:C
   C D E F |' > test.abc
   oabc test.abc
   ```

3. **Include system information:**
   ```bash
   # Run debug info script above
   cat debug_info.txt
   ```

---

## 🎯 Quick Reference Commands

### Essential troubleshooting commands

```bash
# Check installation
pip list | grep orpheus

# Verify dependencies  
odep is_musescore_installed
odep is_abc2midi_installed

# Test basic conversion
oabc samples/Bov_i3.abc

# Reset OLCA
rm -f olca.yml && olca init -y

# Docker quick test
cd bin/testapp && dkrun bash /tests/test_oabc.sh
```

### Common fixes

```bash
# Fix permissions
chmod 755 *.abc
chmod -R 755 .olca/

# Fix Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

# Fix audio
sudo apt-get install timidity fluid-soundfont-gm

# Fix display (for GUI)
export DISPLAY=:0.0
```

---

## 🎵 Still Having Issues?

**Most problems are solved by:**

1. **🔄 Update everything:** `pip install --upgrade orpheuspypractice`
2. **🧹 Clean install:** Remove and reinstall in fresh environment
3. **🔧 Check dependencies:** Run `odep install_musescore install_abc2midi`
4. **📋 Try samples:** Use included ABC files first
5. **🐳 Use Docker:** Guaranteed working environment

**Remember:** The repository is "gold" for music composers because it Just Works™ once properly set up!

---

## 📚 Next Steps

1. **🎵 Go back to creating** → Start with `01-quick-start.md`
2. **🤖 Try AI assistance** → `04-olca-ai-assistant.md`
3. **🔧 Advanced workflows** → `06-advanced-workflows.md`

---

*🛠️ When in doubt, check the samples folder - they're guaranteed to work and show you the correct format!*
