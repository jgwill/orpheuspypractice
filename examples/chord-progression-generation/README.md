# Chord Progression Generation Example

This example demonstrates advanced chord progression generation using the ChatMusician model, showcasing various musical styles and complexity levels.

## Overview

**Focus**: Multiple chord progression variations with increasing complexity
**Styles**: Classical, Jazz, Pop, Blues, and Progressive
**Output**: Professional-quality chord progressions in ABC notation

## Files in this Example

### Configuration
- `orpheus-config.yml` - HuggingFace endpoint setup
- `musical.yml` - Multiple chord progression prompts
- `run_example.sh` - Automated execution script

### Generated Outputs (after running)
- `ChordProgressions_advanced_musical_collection.json` - All prompts collected
- `ChordProgressions_advanced_classical.json/.abc/.mid/.mp3/.jpg` - Classical progression
- `ChordProgressions_advanced_jazz.json/.abc/.mid/.mp3/.jpg` - Jazz progression
- `ChordProgressions_advanced_pop.json/.abc/.mid/.mp3/.jpg` - Pop progression
- `ChordProgressions_advanced_blues.json/.abc/.mid/.mp3/.jpg` - Blues progression
- `ChordProgressions_advanced_progressive.json/.abc/.mid/.mp3/.jpg` - Progressive rock

## Prompt Engineering Techniques

This example demonstrates several advanced prompting techniques:

### 1. Style-Specific Prompts
```yaml
classical: "Create a classical chord progression in D major using traditional voice leading..."
jazz: "Generate a jazz ii-V-I progression with extended chords and alterations..."
```

### 2. Complexity Gradation
- **Basic**: Simple triads with clear resolution
- **Intermediate**: Seventh chords with inversions
- **Advanced**: Extended harmonies with alterations

### 3. Musical Context
- Key signatures specified
- Time signatures included
- Tempo and style markings
- Voice leading instructions

## Running the Example

### Quick Start
```bash
cd examples/chord-progression-generation/
./run_example.sh
```

### Manual Execution
```bash
# Set up environment
export HUGGINGFACE_API_KEY="your_key_here"

# Run inference for all chord progressions
ohfi

# Convert specific outputs
oabc ChordProgressions_advanced_jazz.json
oabc ChordProgressions_advanced_classical.json

# Listen to results
mpg123 ChordProgressions_advanced_jazz.mp3
```

## Expected Musical Results

### Classical Progression (D Major)
- **Structure**: I-vi-IV-V-I (D-Bm-G-A-D)
- **Voice Leading**: Smooth soprano line, bass in root position
- **Style**: Baroque-influenced with appropriate cadences

### Jazz Progression (C Major)
- **Structure**: ii-V-I with extensions (Dm7-G7-Cmaj7)
- **Extensions**: 7ths, 9ths, possible alterations
- **Voice Leading**: Jazz-appropriate chord voicings

### Pop Progression (G Major)
- **Structure**: vi-IV-I-V (Em-C-G-D)
- **Style**: Contemporary popular music harmony
- **Rhythm**: Even quarter note patterns

### Blues Progression (E Major)
- **Structure**: 12-bar blues (E7-A7-B7)
- **Extensions**: Dominant 7th chords throughout
- **Style**: Traditional blues harmony with possible walking bass

### Progressive Rock (Multiple Keys)
- **Structure**: Complex modulations and time signature changes
- **Harmony**: Extended and altered chords
- **Style**: Sophisticated harmonic movement

## Analysis Features

Each generated progression includes:
- **Harmonic Analysis**: Roman numeral notation
- **Voice Leading**: Smooth connections between chords
- **Functional Harmony**: Clear tonic-predominant-dominant relationships
- **Style Adherence**: Genre-appropriate characteristics

## Advanced Usage

### Custom Prompt Creation
```yaml
your_style: "Create a [style] chord progression in [key] using [specific chords/techniques]..."
```

### Batch Processing
```bash
# Generate all progressions then convert all at once
ohfi
wfohfi_then_oabc_foreach_json_files
```

### Integration with AI Agents
```bash
# Use olca agent for interactive progression development
olca -T
# Then in the agent: "Help me develop chord progressions based on the examples"
```

## Educational Value

This example teaches:
1. **Harmonic Theory**: Functional harmony in different styles
2. **Voice Leading**: Smooth connections between chords
3. **Style Characteristics**: How different genres use harmony
4. **AI Prompting**: Effective techniques for musical AI models
5. **Workflow Management**: Batch processing musical content

## Troubleshooting

### Poor AI Results
- Make prompts more specific about desired style
- Include examples of chord symbols in prompts
- Specify key, time signature, and tempo explicitly
- Request ABC notation format explicitly

### Musical Quality Issues
- Check if the AI model understands musical terminology
- Verify ABC notation syntax in generated files
- Try simpler progressions first, then increase complexity
- Use music theory terminology correctly in prompts

## Next Steps

After mastering chord progressions:
1. Explore melodic development over these progressions
2. Try different time signatures and rhythmic patterns
3. Experiment with modulation between keys
4. Combine with the AI agent examples for interactive development