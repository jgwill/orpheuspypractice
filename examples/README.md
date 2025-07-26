# OrpheusPyPractice Examples

This directory contains comprehensive examples demonstrating the complete workflow of the OrpheusPyPractice package, showcasing AI-powered music generation, ABC notation processing, and multi-format conversion.

## Examples Overview

### 1. **basic-ohfi-workflow/** - Complete HuggingFace Inference to Music Pipeline
**Purpose**: Demonstrates the core `ohfi` command workflow from AI inference to musical output
**Workflow**: Configuration → AI Inference → ABC Extraction → MIDI/Audio/Score Generation

### 2. **chord-progression-generation/** - Chord Progression Creation
**Purpose**: Shows how to generate smooth chord progressions using ChatMusician
**Focus**: Multiple prompt variations for chord progression development

### 3. **musical-composition/** - Full Musical Work Development
**Purpose**: Complete musical composition creation with multiple approaches
**Features**: Structural analysis, melodic development, motif creation

### 4. **batch-processing/** - Multiple Prompt Processing
**Purpose**: Demonstrates batch processing of multiple musical prompts
**Workflow**: Single configuration → Multiple outputs → Batch conversion

### 5. **ai-agent-integration/** - AI Agent Music Creation
**Purpose**: Shows integration with `olca` AI agent for interactive music creation
**Features**: Agent-driven prompting, conversational music development

### 6. **workflow-automation/** - Complete Automation Pipeline
**Purpose**: Demonstrates `wfohfi_then_oabc_foreach_json_files` command
**Workflow**: Automated inference → Batch ABC conversion → Multi-format output

## Quick Start

Each example folder contains:
- **Configuration files**: `orpheus-config.yml`, `musical.yml`, `olca.yml`
- **Sample outputs**: Generated JSON, ABC, MIDI, Audio, Score files
- **README.md**: Detailed instructions and explanations
- **Expected results**: What you should see when running the examples

## Prerequisites

Before running examples, ensure you have:
1. **orpheuspypractice** installed: `pip install -e .`
2. **System dependencies**: MuseScore3, ImageMagick, abc2midi
3. **API Keys**: HuggingFace API key, OpenAI API key (for AI agents)
4. **Environment**: Proper environment variables set

## Common Workflow Pattern

Most examples follow this pattern:
```bash
# 1. Navigate to example directory
cd examples/basic-ohfi-workflow/

# 2. Configure your API keys
export HUGGINGFACE_API_KEY="your_key_here"

# 3. Run the inference
ohfi

# 4. Convert JSON outputs to music formats
oabc generated_output.json

# 5. View/play the results
# - View ABC notation: cat *.abc
# - Play MIDI: *.mid
# - View score: *.jpg/*.svg
# - Play audio: *.mp3
```

## Advanced Workflows

### AI Agent Integration
```bash
cd examples/ai-agent-integration/
export OPENAI_API_KEY__o450olca241128="your_key_here"
olca -T  # Start interactive AI agent with tracing
```

### Batch Processing
```bash
cd examples/batch-processing/
ohfi  # Generates multiple JSON files
wfohfi_then_oabc_foreach_json_files  # Converts all JSON to music
```

## Troubleshooting

### Common Issues
1. **Missing API Keys**: Ensure environment variables are set correctly
2. **System Dependencies**: Install MuseScore3, abc2midi, ImageMagick
3. **Endpoint Issues**: Check HuggingFace endpoint status and permissions
4. **ABC Extraction Fails**: Verify the AI model generated valid ABC notation

### Debug Tips
- Use `--help` flag on commands for detailed options
- Check generated `.txt` files for raw AI responses
- Verify configuration files are properly formatted YAML
- Test individual components: `oabc test.abc`, `omid2score test.mid`

## Contributing Examples

When adding new examples:
1. Create a descriptive folder name
2. Include all necessary configuration files
3. Provide clear README.md with step-by-step instructions
4. Include expected output files (or descriptions)
5. Test the example thoroughly before committing

## Support

For issues with examples:
- Check the main project README.md
- Review the CLAUDE.md files in submodules
- Test individual commands in isolation
- Verify all dependencies are properly installed