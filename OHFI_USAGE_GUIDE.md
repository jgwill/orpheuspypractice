# OHFI (Orpheus HuggingFace Inference) Usage Guide

## Overview

`ohfi` is the core command for AI-powered music generation in the OrpheusPyPractice ecosystem. It manages HuggingFace endpoints, executes AI inference for music generation, and integrates with the complete ABC notation processing pipeline.

## Command Structure

```bash
ohfi                    # Execute with configurations in current/home directory
```

## Configuration System

### Primary Configuration: `orpheus-config.yml`

**Location Priority**:
1. Current working directory: `./orpheus-config.yml`
2. User home directory: `~/orpheus-config.yml`

**Required Structure**:
```yaml
huggingface:
  name: your-endpoint-name              # HuggingFace endpoint identifier
  namespace: your-username              # Your HuggingFace username/organization
  repository: m-a-p/ChatMusician       # Model repository
  token_env_var: HUGGINGFACE_API_KEY   # Environment variable for API token
```

### Musical Prompts: `musical.yml`

**Location**: Current working directory only: `./musical.yml`

**Required Structure**:
```yaml
musical:
  name: ProjectName                     # Project identifier
  sname: version                        # Sub-project or version identifier
  prompts:
    prompt_id1: "Your musical prompt..."
    prompt_id2: "Another musical prompt..."
    # ... additional prompts
```

## Workflow Execution

### Phase 1: Endpoint Management
1. **Authentication**: Retrieves API token from specified environment variable
2. **Endpoint Discovery**: Locates the specified HuggingFace endpoint
3. **Boot Process**: Starts the endpoint if not already running
4. **Status Monitoring**: Waits for 'running' status with progress indicators
5. **Performance Tracking**: Records boot time for optimization

### Phase 2: AI Inference Batch Processing
1. **Prompt Loading**: Reads all prompts from `musical.yml`
2. **Collection Generation**: Creates master JSON file with all prompts
3. **Sequential Processing**: Executes each prompt individually
4. **Response Storage**: Saves individual JSON files for each prompt
5. **Error Handling**: Continues processing even if individual prompts fail

### Phase 3: Resource Cleanup
1. **Automatic Suspension**: Pauses endpoint to minimize costs
2. **Status Verification**: Confirms endpoint is properly suspended
3. **Session Summary**: Provides completion status and file inventory

## Output File Structure

For a configuration with `name: MyProject` and `sname: v1`:

### Master Collection
- `MyProject_musical_v1.json` - All prompts collected in single file

### Individual Responses
- `MyProject_v1_prompt1.json` - AI response for prompt1
- `MyProject_v1_prompt2.json` - AI response for prompt2
- `...` - Additional response files for each prompt

### Post-Processing Files (via oabc)
- `MyProject_v1_prompt1.txt` - Raw AI text response
- `MyProject_v1_prompt1.abc` - Extracted ABC notation
- `MyProject_v1_prompt1.mid` - Generated MIDI file
- `MyProject_v1_prompt1.mp3` - Generated audio file
- `MyProject_v1_prompt1.jpg` - Generated musical score image

## Environment Variables

### Required
- **HUGGINGFACE_API_KEY** (or custom name): Your HuggingFace API token with endpoint access permissions

### Optional but Recommended
- **LANGCHAIN_API_KEY**: For tracing and debugging (when using with AI agents)
- **OPENAI_API_KEY**: For AI agent integration (various naming conventions supported)

## Advanced Usage Patterns

### 1. Basic Single Execution
```bash
cd my_music_project/
# Ensure orpheus-config.yml and musical.yml are present
ohfi
```

### 2. Batch Processing Integration
```bash
# Generate AI responses, then convert all to music formats
ohfi
wfohfi_then_oabc_foreach_json_files
```

### 3. AI Agent Integration
```bash
# Use AI agent to create dynamic configurations
olca -T
# Agent creates musical.yml based on conversation
# Then execute inference
ohfi
```

### 4. Research and Development
```bash
# Generate multiple variations
ohfi  # Creates JSON responses
# Analyze with research agent
oiv "Analyze the musical structures in the generated compositions"
```

## Error Handling and Troubleshooting

### Common Issues and Solutions

#### Configuration Errors
```
Error: orpheus-config.yml not found
```
**Solution**: Create config file in current directory or home directory

```
Error: musical.yml not found  
```
**Solution**: Create musical.yml in current working directory

#### Authentication Issues
```
Error: Invalid token or permission denied
```
**Solution**: 
- Verify API key is correctly set in environment
- Ensure token has endpoint access permissions
- Check endpoint name and namespace are correct

#### Endpoint Issues
```
Error: Endpoint not found
```
**Solution**:
- Verify endpoint exists in your HuggingFace account
- Check endpoint name and namespace spelling
- Ensure endpoint is not deleted or suspended

```
Endpoint stuck in 'starting' state
```
**Solution**:
- Wait longer (some endpoints take several minutes)
- Check HuggingFace console for endpoint status
- Verify endpoint has sufficient resources allocated

#### Inference Failures
```
Error in inferences...
```
**Solution**:
- Check if endpoint is properly running
- Verify prompt formatting and content
- Review endpoint logs in HuggingFace console
- Ensure prompts are appropriate for the model

#### ABC Extraction Issues
```
Error: Could not extract the abc notation from the json file
```
**Solution**:
- Review generated .txt files for AI responses
- Ensure prompts explicitly request ABC notation format
- Check if AI model supports ABC notation generation
- Try different prompt formulations

## Performance Optimization

### Cost Management
- **Automatic Suspension**: Endpoints are suspended after use
- **Batch Processing**: Multiple prompts processed in single session
- **Efficient Resource Usage**: Minimal endpoint uptime

### Speed Optimization
- **Sequential Processing**: Prevents API rate limiting
- **Local File Operations**: All post-processing done locally
- **Progress Monitoring**: Real-time status updates

### Quality Assurance
- **Error Continuation**: Failed prompts don't stop batch processing
- **Individual File Storage**: Each response preserved separately
- **Validation Ready**: Outputs ready for quality checking

## Integration Points

### With jgcmlib (ABC Processing)
```bash
# After ohfi generates JSON files
oabc MyProject_v1_prompt1.json    # Convert specific file
# Or use helper functions in python
```

### With AI Agents (olca)
```bash
# Agent can create configurations and execute ohfi
olca -T
# In conversation: "Create a jazz composition and generate it"
```

### With Research Tools (oiv)
```bash
# Analyze generated music
oiv "Compare the harmonic progressions in these generated pieces"
```

### With Workflow Automation
```bash
# Complete automated pipeline
wfohfi_then_oabc_foreach_json_files
```

## Best Practices

### Configuration Management
1. **Version Control**: Keep configuration files in version control
2. **Environment Separation**: Use different endpoints for development/production
3. **API Key Security**: Never commit API keys to repositories
4. **Configuration Validation**: Test configurations with simple prompts first

### Prompt Engineering
1. **Explicit Format Requests**: Always request "ABC notation format" in prompts
2. **Musical Specificity**: Include key, tempo, style, and structural details
3. **Model Limitations**: Understand what musical concepts the AI model supports
4. **Iterative Refinement**: Test and refine prompts based on results

### Resource Management
1. **Endpoint Lifecycle**: Monitor endpoint usage and costs
2. **Batch Efficiency**: Group related prompts in single sessions
3. **Storage Management**: Regularly clean up generated files
4. **Error Monitoring**: Review failed inferences for pattern identification

### Quality Control
1. **Output Validation**: Verify ABC syntax and musical logic
2. **Manual Review**: Listen to generated audio files
3. **Comparative Analysis**: Compare results across different prompts
4. **Documentation**: Keep notes on successful prompt patterns

## Advanced Configuration Examples

### Multi-Style Music Library
```yaml
# orpheus-config.yml
huggingface:
  name: chatmusician-library
  namespace: musicresearcher
  repository: m-a-p/ChatMusician
  token_env_var: HUGGINGFACE_API_KEY

# musical.yml  
musical:
  name: StyleLibrary
  sname: comprehensive
  prompts:
    baroque_fugue: "Compose a baroque fugue subject in D minor with answer at the fifth..."
    jazz_standard: "Create a jazz standard with AABA form in F major..."
    folk_melody: "Write a traditional folk melody with modal characteristics..."
    # ... up to dozens of prompts
```

### Educational Series
```yaml
# musical.yml for music education
musical:
  name: TheoryExamples
  sname: semester1
  prompts:
    major_scale: "Demonstrate a C major scale with proper ABC notation..."
    intervals: "Show examples of all interval types within an octave..."
    chord_progressions: "Create examples of common chord progressions..."
```

### Research Dataset
```yaml
# musical.yml for academic research
musical:
  name: AICompositionStudy
  sname: dataset_v2
  prompts:
    control_classical: "Compose in strict classical style with traditional harmony..."
    experimental_atonal: "Create atonal composition using twelve-tone technique..."
    hybrid_fusion: "Blend classical harmony with contemporary rhythm patterns..."
```

This comprehensive guide covers all aspects of using `ohfi` effectively within the OrpheusPyPractice ecosystem, from basic usage to advanced research applications.