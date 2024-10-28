#%%
import os
from click import prompt
import dotenv
from langchain import hub
import argparse
import yaml


SYSTEM_PROMPT_APPEND=". Dont modify the file: olca_config.yaml"


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

def prepare_input(user_input, system_instructions):
    inputs = {"messages": [
    ("system",
     system_instructions + SYSTEM_PROMPT_APPEND),
    ("user", user_input     )
    ]}
        
    return inputs


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
    recursion_limit=config.get('recursion_limit', 12)
    
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
    
    inputs = prepare_input(user_input, system_instructions)
    
    print_stream(graph.stream(inputs, stream_mode="values"))
    

if __name__ == "__main__":
    main()