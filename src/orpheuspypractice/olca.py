#%%
import os
from click import prompt
import dotenv
from langchain import hub
import argparse
import yaml


SYSTEM_PROMPT_APPEND="""
You do what is above and consider the following when doing the task:
---
* Create any non-existent directories.
* create a subfolder .olca in the current directory if dont exist and :
* Write or append instructions to ./.olca/instructions.txt on how to perform tasks (in terms of reflection and action steps. example: cli syntax to execute something).  You read that file to learn how to do your job if it exists.  You update it with what you learned and keep it up to date. You dont erase the content of the file.  If what you find in it is not related to your task, you ignore it. Dont output all these details you do internally to the standard output. 
* Produce a report in ./report-olca-[TIMESTAMP].md
* Stop and report to the user if repeated errors are encountered.
* Output the iteration number and plan to the standard output during each loop.
* If you are given an issue_id, you commit the work to that issue and push your results (dont output the git push to the standard output).
* Do not comment on your final results; just output them but keep logging your action steps you do internally (all reflection and action steps).
* Dont modify the file: olca_config.yaml 
* If github issue related, dont checkout a branch except if asked otherwise. 
* You dont checkout branches, I repeat, you dont checkout branches.
* Generate your TIMESTAMP with the following command: date +'%Y%m%d%H%M%S' only once at the beginning of your script.
* Make sure if you Switched to branch, you switch back to main before the end of your script.
* Try to observe that you keep doing the same thing over and over again and stop right away if you see that.
"""


def load_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config


#%%

dotenv.load_dotenv()

#%%
#from dotenv in ./.env , load key

#%%

# First we initialize the model we want to use.
from json import load
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent

from langchain_community.agent_toolkits.load_tools import load_tools

import warnings
#

# Suppress the specific UserWarning
warnings.filterwarnings("ignore", category=UserWarning, message="The shell tool has no safeguards by default. Use at your own risk.")

from langchain_community.tools.shell import ShellTool



from typing import Literal

from langchain_core.tools import tool

from langgraph.prebuilt import create_react_agent
from langgraph.errors import GraphRecursionError

@tool
def get_weather(city: Literal["nyc", "sf"]):
    """Use this to get weather information."""
    if city == "nyc":
        return "It might be cloudy in nyc"
    elif city == "sf":
        return "It's always sunny in sf"
    else:
        raise AssertionError("Unknown city")


def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

def prepare_input(user_input, system_instructions,append_prompt=True):
    appended_prompt = system_instructions + SYSTEM_PROMPT_APPEND if append_prompt else system_instructions
    inputs = {"messages": [
    ("system",
     appended_prompt),
    ("user", user_input     )
    ]}
        
    return inputs

def _parse_args():
    parser = argparse.ArgumentParser(description="Orpheus Langchain CLI Assistant")
    parser.add_argument("-D","--disable-system-append", action="store_true", help="Disable prompt appended to system instructions")
    return parser.parse_args()

def main():
    olca_config_file = 'olca_config.yaml'
    #if not os.path.exists(olca_config_file):, print an example and exit
    if not os.path.exists(olca_config_file):
        print("#Example olca_config.yaml:")
        print("api_keyname: 'OPENAI_API_KEY_olca'")
        print("model_name: 'gpt-4o-mini'")
        print("recursion_limit: 12")
        print("temperature: 0")
        print("system_instructions: 'Hello, I am a chatbot. How can I help you today?'")
        print("user_input: 'What is the weather in NYC?'")
        return
    config = load_config(olca_config_file)
    
    
    try:
            
        api_key_variable = "OPENAI_API_KEY"
        api_keyname=config.get('api_keyname',"OPENAI_API_KEY_olca")

        api_key_lcpractices2409 = os.getenv(api_keyname)
        #print(api_key_lcpractices2409)
        os.environ[api_key_variable] = api_key_lcpractices2409
    except :
        pass
    
    system_instructions = config.get('system_instructions', '')
    user_input = config.get('user_input', '')
    model_name=config.get('model_name', "gpt-4o-mini")
    recursion_limit=config.get('recursion_limit', 15)
    disable_system_append = _parse_args().disable_system_append
    
    # Use the system_instructions and user_input in your CLI logic
    print("System Instructions:", system_instructions)
    print("User Input:", user_input)
    print("Model Name:", model_name)
    print("Recursion Limit:", recursion_limit)
    
    
    
    shell_tool = ShellTool()
    model = ChatOpenAI(model=model_name, temperature=0)
    tools = [get_weather, shell_tool]
    
    # Define the graph
    graph = create_react_agent(model, tools=tools)
    
    if graph.config is None:
      graph.config = {}
    graph.config["recursion_limit"] = recursion_limit
    
    inputs = prepare_input(user_input, system_instructions, not disable_system_append)
    

    try:
        print_stream(graph.stream(inputs, stream_mode="values"))
    except GraphRecursionError as e:
        #print(f"Error: {e}")
        print("Recursion limit reached. Please increase the 'recursion_limit' in the olca_config.yaml file.")
        print("For troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/GRAPH_RECURSION_LIMIT")

if __name__ == "__main__":
    main()