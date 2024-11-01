# orpheuspypractice

A Practice Package to Experiment with Orpheus's goals.

## Installation

You can install orpheuspypractice using pip:

```shell
pip install orpheuspypractice
```

## Commands

* oabc: Convert an ABC file to a MIDI file.
* ohfi: Call ChatMusician API with the omusical.yaml
* odep: Install dependencies for Orpheus
* olca: Experimental langchain agent with shell action and python interpretation tooling(at your own risk)

### Olca

The olca.py script is designed to function as a command-line interface (CLI) agent. It performs various tasks based on given inputs and files present in the directory. The agent is capable of creating directories, producing reports, and writing instructions for self-learning. It operates within a GitHub repository environment and can commit and push changes if provided with an issue ID. The script ensures that it logs its internal actions and follows specific guidelines for handling tasks and reporting, without modifying certain configuration files or checking out branches unless explicitly instructed.
