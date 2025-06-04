# 🐳 Docker Setup - Professional Musical Environment

## What is Docker Integration?

**OrpheusPyPractice** comes with a **complete Docker environment** that provides:
- 🎼 **Pre-configured MuseScore3** for sheet music generation
- 🎵 **ABC2MIDI tools** ready to use
- 🖼️ **ImageMagick** for graphics processing
- 🗂️ **X11 support** for GUI applications
- 🔧 **All dependencies** perfectly configured

**Perfect for:** Production environments, CI/CD, team collaboration, or isolated development.

---

## 🚀 Quick Docker Start

### Option 1: Test Environment (Recommended for beginners)
```bash
# Navigate to test environment
cd bin/testapp

# Run the container (includes samples and tests)
dkrun

# You're now inside the container with everything ready!
# Try converting a sample:
oabc /samples/Bov_i3.abc
```

### Option 2: Production Environment
```bash
# Navigate to production environment  
cd bin/app

# Run the production container
dkrun

# Full musical environment ready
```

### Option 3: Base Environment
```bash
# Just the core tools
cd bin/base
dkrun
```

---

## 🎯 What's Inside the Container

### Pre-installed Musical Tools
- **MuseScore3** - Professional sheet music generation
- **ABC2MIDI** - ABC notation to MIDI conversion  
- **ImageMagick** - Graphics processing for sheet music
- **Xvfb** - Virtual display for GUI applications
- **OrpheusPyPractice** - Complete toolkit installed

### Sample Files Available
```bash
# Inside container, check samples
ls /samples/
# Bov_i3.abc
# loup-01c_tst_240620172717.abc
# ... and more!

# Test files for verification
ls /tests/
# test_oabc.sh
# test_musescore3_mid_2_score.sh
```

### Working Environment
```bash
# Your workspace
/work/     # Mount your local files here
/app/      # Application files
/scripts/  # Helper scripts
/samples/  # Example ABC files
```

---

## 🔧 Container Architecture

### Base Container (`jgwill/orpheus:base`)
```dockerfile
# Ubuntu with Python 3.10
# Musical dependencies: abcmidi, musescore3
# X11 support for GUI applications
# Virtual display setup
```

### App Container (`jgwill/orpheus:app`)
```dockerfile
# Extends base with OrpheusPyPractice installed
# User permissions configured
# Production-ready environment
```

### Test Container (`jgwill/orpheus:testapp`)
```dockerfile
# Extends app with test files
# Sample ABC files included
# Automated testing capabilities
```

---

## 🎼 Container Usage Examples

### Example 1: Convert Sample Files
```bash
# Start test container
cd bin/testapp && dkrun

# Inside container:
cd /samples
oabc Bov_i3.abc
ls -la Bov_i3.*
# Bov_i3.abc  Bov_i3.mid  Bov_i3.mp3  Bov_i3.svg
```

### Example 2: Work with Your Files
```bash
# Your files are mounted at /app
cd bin/testapp && dkrun

# Inside container:
cd /app
# Your local files are here!
ls *.abc
oabc my_song.abc
```

### Example 3: Batch Processing
```bash
# Process multiple files
cd bin/testapp && dkrun

# Inside container:
cd /app
for abc_file in *.abc; do
    echo "Converting $abc_file..."
    oabc "$abc_file"
done
```

### Example 4: AI Assistant in Container
```bash
# Use OLCA inside container
cd bin/testapp && dkrun

# Inside container:
export OPENAI_API_KEY_olca="your-key"
olca init
olca
# Full AI assistance in isolated environment
```

---

## 🔥 Advanced Docker Features

### Volume Mounting
Your local files are automatically mounted:
```bash
# Local directory → Container path
./                → /app/
```

### Environment Variables
```bash
# Display support for GUI apps
DISPLAY=:99

# Qt debugging
QT_DEBUG_PLUGINS=1

# X11 forwarding
/tmp/.X11-unix:/tmp/.X11-unix
```

### User Management
```bash
# Container user: jgi
# Sudo access: Available
# Permissions: Configured for musical tools
```

---

## 🛠️ Build Your Own Container

### Customize Base Container
```bash
# Navigate to base directory
cd bin/base

# Edit Dockerfile for custom needs
vim Dockerfile

# Build custom image
dkbuild
```

### Example Customization
```dockerfile
# Add your favorite tools
RUN apt install -y your-tool

# Add custom scripts
COPY my-scripts/ /scripts/

# Install additional Python packages
RUN pip install your-package
```

### Custom Environment Variables
```bash
# Edit _env.sh for custom configuration
vim bin/testapp/_env.sh

# Add custom volumes
dkextra=" -v /your/path:/container/path "

# Add environment variables
dkextra="$dkextra -e YOUR_VAR=value"
```

---

## 🎯 CI/CD Integration

### GitHub Actions Example
```yaml
# .github/workflows/music-pipeline.yml
name: Musical Pipeline
on: [push]
jobs:
  test-music:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Test ABC Conversion
      run: |
        cd bin/testapp
        dkrun bash /tests/test_oabc.sh
```

### Docker Compose (Future)
```yaml
# docker-compose.yml
version: '3'
services:
  orpheus:
    image: jgwill/orpheus:testapp
    volumes:
      - .:/app
    environment:
      - DISPLAY=:99
```

---

## 🔧 Container Development Workflow

### 1. Development Cycle
```bash
# Edit source code locally
vim src/orpheuspypractice/...

# Build and test in container
cd bin/testapp
dkbuild          # Build new image
dkrun            # Test changes
```

### 2. Testing Workflow
```bash
# Run automated tests
cd bin/testapp
dkrun bash /tests/test_oabc.sh

# Check all components
dkrun bash /tests/test_musescore3_mid_2_score.sh
```

### 3. Production Deployment
```bash
# Build production image
cd bin/app
dkbuild

# Deploy to production
docker push jgwill/orpheus:app
```

---

## 🎼 Container Scripts

### Useful Container Commands
```bash
# Inside any container:

# Check musical tools
odep is_musescore_installed
odep is_abc2midi_installed
odep is_imagemagick_installed

# Run tests
bash /tests/test_oabc.sh

# Convert samples
cd /samples && oabc *.abc

# Start virtual display (if needed)
sudo Xvfb :99 -screen 0 1024x768x16 &
```

### Automation Scripts
```bash
# /scripts/run.sh - Main container entry point
# /scripts/convert_all.sh - Batch convert ABC files  
# /tests/test_*.sh - Automated testing
```

---

## 🆘 Docker Troubleshooting

### Common Issues

#### "Cannot connect to Docker daemon"
```bash
# Start Docker service
sudo systemctl start docker

# Add user to docker group
sudo usermod -aG docker $USER
# (logout and login again)
```

#### "X11 forwarding not working"
```bash
# Check X11 setup
echo $DISPLAY

# Allow X11 connections (if needed)
xhost +local:docker
```

#### "Permission denied in container"
```bash
# Check user permissions
whoami  # Should be 'jgi'

# Files should be writable
ls -la /app/
```

#### "MuseScore not working"
```bash
# Check virtual display
ps aux | grep Xvfb

# Restart virtual display
sudo pkill Xvfb
sudo Xvfb :99 -screen 0 1024x768x16 &
```

### Performance Issues
```bash
# Check container resources
docker stats

# Clean up old containers
docker system prune

# Rebuild if needed
cd bin/testapp && dkbuild
```

---

## 🔥 Pro Tips

### 1. Persistent Storage
```bash
# Create named volume for persistent data
docker volume create orpheus-data

# Use in container
dkextra=" -v orpheus-data:/persistent "
```

### 2. Development Shortcuts
```bash
# Quick test alias
alias otest='cd bin/testapp && dkrun bash /tests/test_oabc.sh'

# Quick container access
alias odev='cd bin/testapp && dkrun'
```

### 3. Multi-Architecture Support
```bash
# Build for different platforms
docker buildx build --platform linux/amd64,linux/arm64 .
```

### 4. Container Optimization
```bash
# Check image size
docker images | grep orpheus

# Multi-stage builds for smaller images
# (see Dockerfile examples)
```

---

## 🎯 Production Considerations

### Security
```bash
# Run with non-root user (already configured)
# Limit container capabilities
# Use secrets for API keys
# Regular security updates
```

### Monitoring
```bash
# Log management
docker logs orpheus-container

# Health checks
# Container resource monitoring
# Musical tool status monitoring
```

### Scaling
```bash
# Horizontal scaling with Docker Swarm/Kubernetes
# Load balancing for multiple containers
# Shared storage for ABC files
```

---

## 📚 Next Steps

1. **🔧 Advanced workflows** → `06-advanced-workflows.md`
2. **📖 AI storytelling** → `07-ai-storytelling.md`
3. **🆘 Troubleshooting** → `08-troubleshooting.md`

---

*🐳 Docker gives you a perfect, reproducible musical environment - develop anywhere, deploy everywhere!*
