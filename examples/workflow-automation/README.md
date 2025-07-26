# Workflow Automation Example

This example demonstrates the powerful `wfohfi_then_oabc_foreach_json_files` command, which provides complete automation of the music generation pipeline from AI inference to multi-format output.

## Overview

**Command**: `wfohfi_then_oabc_foreach_json_files`
**Purpose**: Full automation of: HF Inference → JSON Processing → ABC Extraction → Multi-format Conversion
**Result**: Complete music library generated from a single command

## What This Command Does

```python
def wfohfi_then_oabc_foreach_json_files():
    print("Run Inferences then convert to abc commands foreach json files in the current directory.")
    jgthfcli_main()  # Runs ohfi - HuggingFace inference
    # Then processes ALL .json files found:
    json_files = [f for f in os.listdir('.') if f.endswith('.json')]
    for json_file in json_files:
        print(f"Processing {json_file}")
        abc_filename = extract_abc_from_json_to_abc_file(json_file)
        res_musicsheet_svg_filepath, res_audio_filepath, res_midi_filepath = pto_post_just_an_abc_file(abc_filename, score_ext="jpg")
```

## Files in this Example

### Input Configuration
- `orpheus-config.yml` - HuggingFace endpoint configuration
- `musical.yml` - Multiple musical composition prompts
- `batch_config.yml` - Additional configuration for batch processing

### Generated Output Structure
```
workflow-automation/
├── MusicLibrary_batch_musical_collection.json    # All prompts collected
├── MusicLibrary_batch_classical_sonata.json      # Individual AI responses
├── MusicLibrary_batch_classical_sonata.txt       # Raw AI output
├── MusicLibrary_batch_classical_sonata.abc       # Extracted ABC notation
├── MusicLibrary_batch_classical_sonata.mid       # MIDI file
├── MusicLibrary_batch_classical_sonata.mp3       # Audio file
├── MusicLibrary_batch_classical_sonata.jpg       # Musical score
├── MusicLibrary_batch_jazz_ballad.json           # Next composition...
├── MusicLibrary_batch_jazz_ballad.txt
├── MusicLibrary_batch_jazz_ballad.abc
├── ... (complete suite for each prompt)
```

## Example Musical Prompts

This example includes diverse musical styles to demonstrate the automation capability:

### Classical Compositions
- Sonata movement in C major
- Baroque invention in two voices
- Romantic character piece

### Popular Music
- Jazz ballad with complex harmony
- Folk song with guitar accompaniment
- Contemporary pop arrangement

### Experimental
- Atonal composition with serial techniques
- World music fusion piece
- Minimalist pattern-based composition

## Running the Automation

### Single Command Execution
```bash
cd examples/workflow-automation/

# Set up your API key
export HUGGINGFACE_API_KEY="your_key_here"

# Run the complete automated workflow
wfohfi_then_oabc_foreach_json_files
```

### What Happens During Execution

#### Phase 1: Mass AI Inference
```
Starting HuggingFace endpoint...
Endpoint status: running
Boot time: X seconds

-------------------------------------------
classical_sonata: Compose a sonata movement in C major...
[AI processing...]
written: MusicLibrary_batch_classical_sonata.json

-------------------------------------------  
jazz_ballad: Create a jazz ballad with sophisticated harmony...
[AI processing...]
written: MusicLibrary_batch_jazz_ballad.json

[Continues for all prompts...]
Suspending endpoint to save costs
```

#### Phase 2: Batch ABC Processing
```
Run Inferences then convert to abc commands foreach json files in the current directory.
Processing MusicLibrary_batch_classical_sonata.json
generated_text: [Full AI response]
abc extracted: ['X:1\nT:Sonata in C Major\n...']

Processing MusicLibrary_batch_jazz_ballad.json  
generated_text: [Full AI response]
abc extracted: ['X:1\nT:Autumn Leaves Reimagined\n...']

[Continues for all JSON files...]
```

#### Phase 3: Multi-format Conversion
```
FILES CREATED:
MusicLibrary_batch_classical_sonata.jpg
MusicLibrary_batch_classical_sonata.mp3  
MusicLibrary_batch_classical_sonata.abc
MusicLibrary_batch_classical_sonata.mid

[Repeats for each composition...]
```

## Advanced Configuration

### musical.yml - Production Music Library
```yaml
musical:
  name: MusicLibrary
  sname: batch
  prompts:
    classical_sonata: "Compose the exposition of a sonata movement in C major, following classical form with primary and secondary themes. Include development techniques and proper voice leading. Return in ABC notation."
    
    baroque_invention: "Create a two-voice invention in the style of Bach, in D minor. Use imitative counterpoint with subject and answer, including stretto passages. Provide in ABC notation format."
    
    jazz_ballad: "Compose a jazz ballad with sophisticated harmony including ii-V-I progressions, altered dominants, and extended chords. Structure: AABA form in F major. Return in ABC notation."
    
    folk_arrangement: "Arrange a folk melody with guitar accompaniment, using fingerpicking patterns and open chord voicings. Key of G major, moderate tempo. Provide in ABC notation."
    
    minimalist_piece: "Create a minimalist composition using phase shifting and additive processes. Start with a simple motif and gradually develop it through repetition and variation. ABC notation format."
    
    world_fusion: "Compose a piece blending Western harmony with modal scales from world music traditions. Use 7/8 time signature and incorporate ornaments. Return in ABC notation."
    
    contemporary_pop: "Write a contemporary pop song structure with verse-chorus-bridge form. Include chord symbols and a memorable melody line. Key of A major. ABC notation format."
    
    atonal_study: "Create a short atonal composition using twelve-tone technique. Ensure all twelve chromatic pitches are used before repetition. Return in ABC notation format."
```

### Batch Processing Features

#### Automatic Error Handling
- Skips JSON files that don't contain valid ABC notation
- Continues processing even if individual files fail
- Logs errors for later review

#### File Organization
- Maintains consistent naming conventions
- Creates complete suites for each composition
- Preserves original JSON responses for reference

#### Quality Control
- Validates ABC notation syntax before processing
- Ensures MIDI files are properly generated
- Verifies audio and score outputs

## Production Use Cases

### 1. Music Library Creation
Generate complete music libraries for:
- Educational institutions
- Content creators
- Music therapy applications
- Game development soundtracks

### 2. Style Studies
Create comprehensive collections of:
- Historical period studies
- Genre explorations
- Technique demonstrations
- Composition exercises

### 3. Research Applications
- Comparative analysis of AI-generated music
- Style transfer studies
- Musical corpus development
- Algorithm evaluation datasets

## Performance Optimization

### Parallel Processing Considerations
- HuggingFace endpoint warm-up time
- Sequential ABC processing prevents conflicts
- Batch inference more cost-effective than individual calls

### Resource Management
- Automatic endpoint suspension saves costs
- Local file processing after cloud inference
- Efficient memory usage for large batches

## Troubleshooting

### Large Batch Issues
```bash
# Monitor progress
tail -f output.log

# Resume from interruption
# Remove successfully processed JSON files and re-run
rm processed_*.json
wfohfi_then_oabc_foreach_json_files
```

### Quality Control
```bash
# Check for missing ABC files
ls *.json | while read f; do
  abc_file="${f%.json}.abc"
  if [ ! -f "$abc_file" ]; then
    echo "Missing ABC: $f"
  fi
done

# Validate ABC syntax
for abc_file in *.abc; do
  abc2midi "$abc_file" -o /dev/null 2>/dev/null || echo "Invalid ABC: $abc_file"
done
```

### Selective Processing
```bash
# Process only specific types
rm *_experimental_*.json  # Remove experimental prompts
wfohfi_then_oabc_foreach_json_files  # Process only classical/jazz/pop
```

## Integration with Other Examples

### Combine with AI Agent
```bash
# Use agent to generate custom musical.yml
olca -T
# Agent creates musical.yml based on conversation
# Then run automated workflow
wfohfi_then_oabc_foreach_json_files
```

### Extend with Research Tools
```bash
# After automation, use research agent for analysis
oiv "Analyze the harmonic progressions in the generated classical pieces"
```

## Next Steps

After mastering workflow automation:
1. Create custom batch configurations for specific projects
2. Integrate with database systems for music library management
3. Develop quality metrics and automated analysis
4. Create web interfaces for batch job management
5. Explore distributed processing for very large batches