# Basic OHFI Workflow Example

*🎵 [← Back to Examples Overview](../README.md) | [Next: Chord Progressions →](../chord-progression-generation/README.md)*

This example demonstrates the complete `ohfi` (Orpheus HuggingFace Inference) workflow from AI model inference to musical output generation.

## Overview

**Workflow**: Configuration → HuggingFace Endpoint → AI Inference → ABC Extraction → MIDI/Audio/Score Generation

**What this example does**:
1. Boots a ChatMusician HuggingFace endpoint
2. Sends musical prompts for chord progression generation
3. Extracts ABC notation from AI responses
4. Converts ABC to MIDI, MP3, and visual score formats
5. Automatically suspends the endpoint to save costs

## Files in this Example

### Configuration Files
- `orpheus-config.yml` - HuggingFace endpoint configuration
- `musical.yml` - Musical prompts and project settings

### Expected Output Files (after running)
- `ChordProgression_basic_musical_v1.json` - Collection of all prompts
- `ChordProgression_v1_prompt1.json` - AI response for prompt1
- `ChordProgression_v1_prompt1.txt` - Raw AI text response
- `ChordProgression_v1_prompt1.abc` - Extracted ABC notation
- `ChordProgression_v1_prompt1.mid` - Generated MIDI file
- `ChordProgression_v1_prompt1.mp3` - Generated audio file
- `ChordProgression_v1_prompt1.jpg` - Generated musical score image

## Step-by-Step Instructions

### Prerequisites
1. Install orpheuspypractice: `pip install -e .` (from project root)
2. Install system dependencies: `odep install musescore`
3. Set up HuggingFace API key: `export HUGGINGFACE_API_KEY="your_key_here"`
4. Ensure you have a ChatMusician endpoint configured in HuggingFace

### Running the Example

```bash
# 1. Navigate to this example directory
cd examples/basic-ohfi-workflow/

# 2. Verify your API key is set
echo $HUGGINGFACE_API_KEY

# 3. Run the complete inference workflow
ohfi

# 4. (Optional) Convert additional JSON files to music formats
oabc ChordProgression_v1_prompt1.json

# 5. View the generated ABC notation
cat ChordProgression_v1_prompt1.abc

# 6. Play the generated audio (if supported by your system)
# mpg123 ChordProgression_v1_prompt1.mp3
# or open the MP3 file in your preferred audio player

# 7. View the musical score
# Open ChordProgression_v1_prompt1.jpg in an image viewer
```

## What Happens During Execution

### Phase 1: Endpoint Management
```
Starting HuggingFace endpoint: chatmusician-example
Endpoint status: running
Boot time: X seconds
```

### Phase 2: AI Inference
```
-------------------------------------------
prompt1 Generate a smooth chord progression using Em, Am, D7, G
[AI Response Processing]
```

### Phase 3: File Generation
```
written: ChordProgression_basic_musical_v1.json
written: ChordProgression_v1_prompt1.json
generated_text: [AI response with ABC notation]
abc extracted: ['X:1\nT:Chord Progression\n...']
```

### Phase 4: Music Format Conversion
```
FILES CREATED:
ChordProgression_v1_prompt1.jpg    # Musical score image
ChordProgression_v1_prompt1.mp3    # Audio file
ChordProgression_v1_prompt1.abc    # ABC notation
ChordProgression_v1_prompt1.mid    # MIDI file
```

### Phase 5: Cleanup
```
Suspending endpoint to save costs
Endpoint status: paused
```

## Configuration Details

### orpheus-config.yml
```yaml
huggingface:
  name: chatmusician-example          # Your endpoint name
  namespace: your-username            # Your HuggingFace username
  repository: m-a-p/ChatMusician     # Model repository
  token_env_var: HUGGINGFACE_API_KEY # Environment variable name
```

### musical.yml
```yaml
musical:
  name: ChordProgression              # Project name
  sname: v1                          # Version/iteration name
  prompts:
    prompt1: "Generate a smooth chord progression using Em, Am, D7, G"
    prompt2: "Create a jazz chord progression in the key of C major"
```

## Troubleshooting

### Common Issues

1. **"Error: orpheus-config.yml not found"**
   - Ensure the config file is in the current directory or your home directory
   - Check file permissions and YAML syntax

2. **"Endpoint not found" or permission errors**
   - Verify your HuggingFace endpoint name and namespace
   - Ensure your API key has the correct permissions
   - Check that the endpoint exists and is not deleted

3. **"Could not extract ABC notation"**
   - The AI model may not have generated valid ABC notation
   - Check the `.txt` file to see the raw AI response
   - Try different prompts that explicitly request ABC format

4. **"Could not convert ABC to MIDI"**
   - Ensure `abc2midi` is installed and in your PATH
   - Check that the ABC notation is syntactically correct
   - Verify the ABC file was created successfully

5. **"Could not convert MIDI to score/audio"**
   - Ensure MuseScore3 is installed: `odep install musescore`
   - Try with different MuseScore versions (musescore vs musescore3)
   - Check system PATH includes MuseScore binary location

### Debug Commands
```bash
# Test individual components
abc2midi --help                    # Verify abc2midi installation
musescore3 --help                  # Verify MuseScore installation
oabc --help                        # View ABC conversion options
ohfi --help                        # View inference options (if available)

# Manual conversion testing
oabc sample.abc                    # Test ABC to music conversion
omid2score sample.mid              # Test MIDI to score conversion
```

## Expected Results

After successful execution, you should have:
- **JSON files**: Raw AI responses and collected prompts
- **ABC files**: Clean musical notation in ABC format
- **MIDI files**: Playable MIDI sequences
- **MP3 files**: Audio renderings of the music
- **JPG files**: Visual musical scores

The generated music should reflect the chord progressions specified in your prompts, rendered in standard musical notation format.

## Next Steps

Once comfortable with this basic workflow, explore:
- `../chord-progression-generation/` - More complex chord progressions
- `../batch-processing/` - Multiple prompts at once
- `../ai-agent-integration/` - Interactive AI-driven music creation
- `../workflow-automation/` - Fully automated batch processing