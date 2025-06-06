# ABC Pro Generator - Musical & Storytelling Assistant

A Python module that uses submodules and exposes useful functions for musical and storytelling assistance.

## Core Functionality

### 1. ABC Notation Processing
- Parse and validate ABC notation
- Generate ABC from natural language prompts
- Convert between formats (ABC ↔ MIDI ↔ WAV ↔ MP3)

### 2. CLI Agent (oabc-pro.py)
- Natural language interface for musical requests
- Learning system that stores knowledge
- Python code interpretation and shell actions

### 3. Configuration (oabc-pro.conf)
- User preferences and musical styles
- LLM provider settings
- Learning parameters

### 4. Knowledge Management
- `.oabc-pro-instructions.md` - Learned instructions
- `.oabc-pro-db.json` - Knowledge database

## Quick Start

```bash
# Basic usage
python oabc-pro.py "Generate a happy birthday melody in C major"

# CLI interface
python oabc-pro.py --interactive

# Process files
python oabc-pro.py process song.abc --format midi
```

## Installation

```bash
pip install -r requirements.txt
```

## Acronyms
- abc = ABC Notation in Music
- midi = Musical Instrument Digital Interface  
- wav = Waveform Audio File Format
- mp3 = MPEG-1 Audio Layer 3
