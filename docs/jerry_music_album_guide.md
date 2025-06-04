# Using orpheuspypractice for AI Music Composition

Jerry, this repository contains various tools that can help you create a music album with AI assistance. Below are some features worth exploring:

## Key Features

- **oabc**: Convert an ABC notation file to a MIDI file. This is useful when you want to transform sheet music into playable MIDI for further editing.
- **ohfi**: Call the ChatMusician API using `omusical.yaml`. This lets you generate musical ideas or arrangements with the help of AI models.
- **wfohfi_then_oabc_foreach_json_files**: Run AI inferences from JSON data and automatically convert the results into sheet music and audio previews.
- **olca**: A command-line agent capable of executing shell and Python commands. It can manage tasks like directory creation, reporting, and GitHub integration, making it easier to organize your music production workflow.

## Getting Started

1. Install the package:
   ```sh
   pip install orpheuspypractice
   ```
2. Run `oabc` or `ohfi` with your music files to generate MIDI or interact with ChatMusician.
3. Configure and experiment with `olca` for advanced automation and project management.

With these tools, you can blend AI-driven composition with your own creativity to build your album efficiently.
