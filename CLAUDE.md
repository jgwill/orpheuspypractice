# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**orpheuspypractice** is an experimental music and AI practice package (v0.2.65) designed to explore the intersection of music generation, AI agents, and interactive storytelling. It serves as a testing ground for musical ABC notation processing, AI agent interactions, and LangChain-based tooling.

## Core Architecture

### Main Package Structure
- **Source**: `src/orpheuspypractice/` - Main Python package
- **Dependencies**: Two core submodules via git submodules:
  - `jgcmlib` (>= 1.0.59): Music notation and ABC file processing
  - `jghfmanager` (>= 0.1.5): HuggingFace model management and inference

### Key Components

#### Music Processing (`oabc`, `omid2score`)
- **ABC Notation**: Convert ABC music files to MIDI using `jgcmlib`
- **MIDI to Score**: Convert MIDI files to musical scores via MuseScore3
- **Workflow Integration**: `wfohfi_then_oabc_foreach_json_files()` - Run HF inference then convert JSON outputs to ABC files

#### AI Agent System (`olca`)
- **Configuration-driven**: Uses `olca.yml` for agent behavior settings
- **LangChain Integration**: Full LangGraph + LangSmith support with shell and Python tools
- **Interactive CLI**: Continuous conversation loop with tracing support
- **GitHub Integration**: Can commit and push changes when provided issue ID

#### Research Agent (`oiv`)
- **ArXiv Integration**: Research paper analysis and summarization
- **Configurable Models**: Supports multiple ChatGPT models via hub tags
- **Output Formats**: JSON and Markdown serialization

#### Dependency Management (`odep`)
- **System Dependencies**: Install/manage MuseScore, ImageMagick, abc2midi
- **Cross-platform**: Handles different package managers (apt, brew, pacman)

## Build and Development Commands

### Building and Testing
```bash
# Clean build artifacts
make clean

# Build distribution
make dist

# Run version bump
make bump_version

# Full release cycle
make release
```

### Development Workflow
```bash
# Set up environment (loads from /opt/binscripts/load.sh)
./_build.sh

# Install in development mode
pip install -e .

# Test specific functionality
python -m pytest tests/
```

### Command Line Tools
```bash
# Music processing
oabc file.abc                    # Convert ABC to MIDI
omid2score file.mid              # Convert MIDI to score
ohfi                            # HuggingFace model inference

# AI agents
olca -T                         # Start agent with tracing
oiv "research query"            # ArXiv research agent

# Workflow automation
wfohfi_then_oabc_foreach_json_files  # HF inference → ABC conversion

# System setup
odep install musescore          # Install music dependencies
```

## Configuration Files

### `olca.yml` (AI Agent Configuration)
```yaml
api_keyname: OPENAI_API_KEY__o450olca241128  # Environment variable for API key
human: true                                  # Interactive mode
model_name: gpt-4o-mini                     # LLM model
recursion_limit: 300                        # LangGraph recursion limit
temperature: 0.0                            # Model temperature
tracing: true                               # Enable LangSmith tracing
system_instructions: "Your agent behavior"  # System prompt
user_input: "Initial user query"            # Starting prompt
```

### Environment Variables
- `OPENAI_API_KEY__*`: OpenAI API keys (configurable suffix)
- `LANGCHAIN_API_KEY`: Required for tracing functionality
- `PYTHONPATH`: Set to `$(pwd)/src` during development

## Key Dependencies

### Core Libraries
- **music21**: Music analysis and processing
- **langchain**: AI agent framework with experimental features
- **langchain_openai**: OpenAI integration
- **langchain_community**: Community tools and utilities
- **langgraph**: Graph-based agent workflows
- **langsmith**: Agent tracing and monitoring

### External Tools
- **MuseScore3**: Music score rendering and MIDI conversion
- **ImageMagick**: Image processing for score generation
- **abc2midi**: ABC notation to MIDI conversion

## Development Notes

### Git Submodules
The project uses git submodules for `jgcmlib` and `jghfmanager`. These must be properly initialized:
```bash
git submodule update --init --recursive
```

### Testing Infrastructure
- Test files located in `tests/` directory
- Sample files in `samples/` for ABC and MIDI processing
- Shell scripts for integration testing

### Build System
- Uses `setuptools` with entry points for CLI commands
- Version management via `bump_version.py`
- PyPI deployment via `twine`
- Docker support available (`Dockerfile` present)

## Important Context

This is primarily an **experimental practice package** designed for rapid prototyping of music AI concepts. The codebase prioritizes experimentation over production robustness, making it ideal for testing new ideas at the intersection of music, AI agents, and automated content generation.