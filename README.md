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

#### Tracing

Olca now supports tracing functionality to help monitor and debug its operations. You can enable tracing by using the `-T` or `--tracing` flag when running the script. Ensure that the `LANGCHAIN_API_KEY` environment variable is set for tracing to work.

#### Initialization

To initialize `olca`, you need to create a configuration file named `olca.yml`. This file contains various settings that `olca` will use to perform its tasks. Below is an example of the `olca.yml` file:

```yaml
api_keyname: OPENAI_API_KEY__o450olca241128
human: true
model_name: gpt-4o-mini
recursion_limit: 300
system_instructions: You focus on interacting with human and do what they ask.  Make sure you dont quit the program.
temperature: 0.0
tracing: true
user_input: Look in the file 3act.md and in ./story, we have created a story point by point and we need you to generate the next iteration of the book in the folder ./book.  You use what you find in ./story to start the work.  Give me your plan to correct or accept.
```

#### Usage

To run `olca`, use the following command:

```shell
olca -T
```

This command will enable tracing and start the agent. You can also use the `--trace` flag to achieve the same result.

#### Configuration

The `olca.yml` file allows you to configure various aspects of `olca`, such as the API key (so you can know how much your experimetation cost you), model name, recursion limit, system instructions, temperature, and user input. You can customize these settings to suit your needs and preferences.

#### Command-Line Interface (CLI)

The `olca` script provides a user-friendly CLI that allows you to interact with the agent and perform various tasks. You can use flags and options to control the agent's behavior and provide input for its operations. The CLI also includes error handling mechanisms to notify you of any issues or missing configuration settings.

#### GitHub Integration

`olca` is designed to integrate seamlessly with GitHub workflows and issue management. You can provide an issue ID to the agent, and it will commit and push changes directly to the specified issue. This feature streamlines the development process and reduces the need for manual intervention. Additionally, `olca` maintains detailed logs of its actions and updates, ensuring transparency and traceability in its operations.

#### Conclusion

The enhancements to `olca` make it a powerful and versatile tool for developers working on musical and storytelling projects. With improved configurability, debugging capabilities, and integration with GitHub workflows, `olca` offers a comprehensive solution for creating and managing interactive storytelling experiences. Try out `olca` today and see how it can enhance your development process!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
