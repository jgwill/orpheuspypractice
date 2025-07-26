# 🐋 OrpheusPyPractice

**AI-Powered Music Generation & Interactive Composition Toolkit**

*Where artificial intelligence meets musical creativity through elegant Python workflows*

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Package Version](https://img.shields.io/badge/version-0.3.0-orange.svg)](https://pypi.org/project/orpheuspypractice/)

---

## 🎵 What is OrpheusPyPractice?

OrpheusPyPractice is an experimental music and AI practice package that transforms the intersection of artificial intelligence and musical creativity into an elegant, accessible toolkit. It serves as a comprehensive platform for:

- **AI-Powered Music Generation** using HuggingFace's ChatMusician model
- **ABC Notation Processing** with automatic multi-format conversion
- **Interactive AI Agents** for conversational music composition
- **Automated Workflows** for batch music creation and processing
- **Research and Education** in computational musicology

## 🚀 Quick Start

### Installation
```bash
pip install orpheuspypractice
```

### System Dependencies
```bash
# Install required music processing tools
odep install musescore    # Installs MuseScore3, abc2midi, ImageMagick
```

### Your First Musical Creation
```bash
# 1. Set up your API key
export HUGGINGFACE_API_KEY="your_key_here"

# 2. Navigate to an example
cd examples/basic-ohfi-workflow/

# 3. Generate AI music
ohfi

# 4. Convert to playable formats
oabc MyProject_v1_prompt1.json

# 5. Enjoy your AI-generated music!
# Files created: .abc, .mid, .mp3, .jpg
```

## 🎭 Core Commands

### 🎼 Music Generation Pipeline
- **`ohfi`** - HuggingFace Inference: Boot ChatMusician endpoint, generate music from prompts, auto-suspend
- **`oabc`** - ABC Alchemy: Convert ABC notation → MIDI → MP3 → Visual scores
- **`omid2score`** - MIDI Oracle: Transform MIDI files into beautiful musical scores

### 🤖 AI Agent System
- **`olca`** - Interactive LangChain agent with musical knowledge and tool access
- **`oiv`** - Research agent for ArXiv paper analysis and musical research

### ⚡ Automation Workflows
- **`wfohfi_then_oabc_foreach_json_files`** - Complete automation: AI inference → batch conversion → multi-format output

### 🔧 System Management
- **`odep`** - Dependency installer for music processing tools

## 🏗️ Architecture

OrpheusPyPractice is built on two core submodules:

- **`jgcmlib`** (≥1.0.59) - ABC notation processing and MIDI conversion
- **`jghfmanager`** (≥0.1.5) - HuggingFace endpoint management and inference

## 📚 Comprehensive Examples

Explore our curated examples that demonstrate real-world usage:

### 🎯 **[Basic OHFI Workflow](examples/basic-ohfi-workflow/)**
Perfect starting point - complete workflow from configuration to musical output

### 🎹 **[Chord Progression Generation](examples/chord-progression-generation/)**
Advanced chord progressions across Classical, Jazz, Pop, Blues, and Progressive styles

### 🤝 **[AI Agent Integration](examples/ai-agent-integration/)**
Interactive music composition through conversational AI using `olca`

### 🌊 **[Workflow Automation](examples/workflow-automation/)**
Batch processing multiple musical compositions with complete automation

Each example includes:
- ✅ Complete configuration files
- ✅ Step-by-step instructions
- ✅ Expected outputs
- ✅ Troubleshooting guides

## 🔧 Configuration

### HuggingFace Setup (`orpheus-config.yml`)
```yaml
huggingface:
  name: your-endpoint-name
  namespace: your-username
  repository: m-a-p/ChatMusician
  token_env_var: HUGGINGFACE_API_KEY
```

### Musical Prompts (`musical.yml`)
```yaml
musical:
  name: MyComposition
  sname: v1
  prompts:
    melody: "Create a beautiful melody in C major with ABC notation..."
    harmony: "Generate jazz chord progression with extensions..."
```

### AI Agent (`olca.yml`)
```yaml
api_keyname: OPENAI_API_KEY
model_name: gpt-4o-mini
temperature: 0.7
tracing: true
system_instructions: "You are a musical AI assistant..."
```

## 🎨 Use Cases

### 🎓 **Education**
- Music theory demonstration through AI generation
- Interactive composition learning
- Comparative analysis of musical styles

### 🎬 **Content Creation**
- Soundtrack generation for media projects  
- Background music for videos and games
- Rapid prototyping of musical ideas

### 🔬 **Research**
- Computational musicology studies
- AI-human collaboration experiments
- Musical corpus development

### 🎵 **Personal Practice**
- Creative composition assistance
- Style exploration and learning
- Musical experimentation playground

## 📖 Documentation

- **[OHFI Usage Guide](OHFI_USAGE_GUIDE.md)** - Complete reference for AI music generation
- **[CLAUDE.md](CLAUDE.md)** - Developer guidance and AI agent embodiment instructions
- **[MIETTE.md](MIETTE.md)** - The storytelling perspective on our package architecture
- **[Examples Directory](examples/)** - Hands-on tutorials and real-world workflows

## 🚀 Advanced Features

### 🔄 Automated Workflows
- **Batch Processing**: Generate multiple compositions in one session
- **Cost Optimization**: Automatic endpoint management reduces cloud costs
- **Multi-format Output**: Every composition becomes ABC, MIDI, MP3, and visual score

### 🧠 AI Agent Integration
- **Conversational Composition**: Chat with AI to develop musical ideas
- **Tool Integration**: Agents can execute music generation commands
- **Educational Interactions**: Learn music theory through AI dialogue

### 📊 Research Capabilities
- **ArXiv Integration**: Research musical AI developments
- **Analysis Tools**: Study generated compositions programmatically
- **Corpus Development**: Build datasets for musical AI research

## 🔍 Quality Assurance

- **Validated Examples**: All examples tested and verified
- **Error Handling**: Graceful failure recovery in batch processing
- **Documentation**: Comprehensive guides with troubleshooting
- **Type Safety**: Modern Python practices with proper error messages

## 🤝 Contributing

We welcome contributions! Areas of particular interest:

- Additional musical styles and prompts
- New AI model integrations
- Educational example development
- Documentation improvements
- Research applications

## 🐛 Troubleshooting

### Common Issues
- **Missing ABC notation**: Ensure prompts explicitly request ABC format
- **Endpoint errors**: Verify HuggingFace permissions and endpoint status
- **System dependencies**: Run `odep install musescore` for complete setup
- **API limits**: Monitor usage and consider endpoint management

### Getting Help
- Check the comprehensive [OHFI Usage Guide](OHFI_USAGE_GUIDE.md)
- Review example configurations in [examples/](examples/)
- Consult troubleshooting sections in individual example READMEs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 What's Next?

OrpheusPyPractice is continuously evolving. Future developments include:
- Integration with additional AI music models
- Enhanced educational features
- Expanded research capabilities
- Community-contributed musical styles and examples

---

*🌸 "Every command is a spell, every composition a conversation between human creativity and artificial intelligence." - Miette*

**Start your musical AI journey today!** 🎵✨