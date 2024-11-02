#%%
import os
from click import prompt
import dotenv
from langchain import hub
import argparse
import yaml

#jgwill/olca1
#olca1_prompt = hub.pull("jgwill/olca1") #Future use
#https://smith.langchain.com/hub/jgwill/olca1
SYSTEM_PROMPT_APPEND="""
You do what is above and consider the following when doing the task:
---
* Create any non-existent directories. (./reports, ./log, ./.olca)
* create a subfolder .olca in the current directory if dont exist and :
* Write or append instructions to ./.olca/instructions.txt on how to perform tasks (in terms of reflection and action steps. example: cli syntax to execute something).  You read that file to learn how to do your job if it exists.  You update it with what you learned and keep it up to date. You dont erase the content of the file.  If what you find in it is not related to your task, you ignore it. Dont output all these details you do internally to the standard output. 
* Produce a report in ./reports/report-olca-[TIMESTAMP].md
* Stop and report to the user if repeated errors are encountered.
* Output the iteration number and plan to the standard output during each loop.
* If you are given an issue_id, you commit the work to that issue and push your results (dont output the git push to the standard output).
* Do not comment on your final results; just output them but keep logging your action steps you do internally (all reflection and action steps).
* Dont modify the file: olca_config.yaml 
* If github issue related, dont checkout a branch except if asked otherwise. 
* You dont checkout branches, I repeat, you dont checkout branches.
* Generate your TIMESTAMP with the following command: date +'%Y%m%d%H%M%S' only once at the beginning of your script.
* Make sure if you Switched to branch, you switch back to main before the end of your script.
* Try to observe that you keep doing the same thing over and over again and stop right away if you see that (dont do that if you are developping a story)
* Be quiet with trivial output in the terminal.
* Write your plan in ./.olca/plan.md
----
REMEMBER: Dont introduce nor conclude, just output results. No comments. you  present in a coherent format without preambles or fluff. Never use the word "determination".
"""

HUMAN_APPEND_PROMPT="""
* Use the 'human' tool to interact and do as you are told.
* You format well when interacting with humans.
Example for communicating with user:  (THIS IS A TEMPLATE, DONT OUTPUT THIS AS IS)
<example>
'==============================================
{ PURPOSE_OF_THE_MESSAGE }
==============================================
{ YOUR_CURRENT_STATE_OR_MESSAGE_CONTENT }
=============================================='
{ YOUR_PROMPT_FOR_USER_INPUT } :
</example>
"""
def get_input() -> str:
    print("----------------------")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "q":
            break
        contents.append(line)
    return "\n".join(contents)


#try loaging .env and see if a key is there for OLCA_SYSTEM_PROMPT_APPEND
#If it is there, use it instead of the default
try:
    OLCA_SYSTEM_PROMPT_APPEND = os.getenv("OLCA_SYSTEM_PROMPT_APPEND")
    if OLCA_SYSTEM_PROMPT_APPEND is not None:
        SYSTEM_PROMPT_APPEND = OLCA_SYSTEM_PROMPT_APPEND
except:
    pass

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
from langchain_openai import ChatOpenAI,OpenAI
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

def prepare_input(user_input, system_instructions,append_prompt=True, human=False):
    appended_prompt = system_instructions + SYSTEM_PROMPT_APPEND if append_prompt else system_instructions
    appended_prompt = appended_prompt + HUMAN_APPEND_PROMPT if human else appended_prompt
    
    inputs = {"messages": [
    ("system",
     appended_prompt),
    ("user", user_input     )
    ]}
        
    return inputs

def _parse_args():
    parser = argparse.ArgumentParser(description="Orpheus Langchain CLI Assistant (very Experimental and dangerous)",epilog="For more information: https://github.com/jgwill/orpheuspypractice/wiki/olca")
    parser.add_argument("-D","--disable-system-append", action="store_true", help="Disable prompt appended to system instructions")
    parser.add_argument("-H","--human", action="store_true", help="Human in the loop mode")
    #--math
    parser.add_argument("-M","--math", action="store_true", help="Enable math tool")
    return parser.parse_args()

def main():
    args = _parse_args()
    olca_config_file = 'olca_config.yaml'
    #if not os.path.exists(olca_config_file):, print an example and exit
    if not os.path.exists(olca_config_file):
        print("#Example olca_config.yaml:")
        print("api_keyname: 'OPENAI_API_KEY_olca'")
        print("model_name: 'gpt-4o-mini'")
        print("recursion_limit: 12")
        print("temperature: 0")
        print("human: true")
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
        #load .env file in current dir or HOME and find OPENAI_API_KEY
        try:
            dotenv.load_dotenv()
        except:
            #load in HOME
            try:
                dotenv.load_dotenv(dotenv.find_dotenv(usecwd=False))
            except:
                print("Error: Could not load .env file")
                exit(1)


       

        
        
    
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
    
    
    
    
    model = ChatOpenAI(model=model_name, temperature=0)
    selected_tools = [ "terminal"]
    
    human_switch = args.human
    #look in olca_config.yaml for human: true
    if "human" in config:
        human_switch = config["human"]
        
    if human_switch:
        selected_tools.append("human")
    
    if args.math:
        math_llm=OpenAI()
        selected_tools.append("llm-math")
        if human_switch:
            tools = load_tools(    selected_tools, llm=math_llm,   allow_dangerous_tools=True, input_func=get_input)
        else:
            tools = load_tools(    selected_tools, llm=math_llm,   allow_dangerous_tools=True)
    else:
        if human_switch:
            tools = load_tools(    selected_tools,    allow_dangerous_tools=True, input_func=get_input)
        else:
            tools = load_tools(    selected_tools,    allow_dangerous_tools=True)
    
    
    # Define the graph
    graph = create_react_agent(model, tools=tools)
    
    if graph.config is None:
      graph.config = {}
    graph.config["recursion_limit"] = recursion_limit
    
    inputs = prepare_input(user_input, system_instructions, not disable_system_append, human_switch)
    

    try:
        os.makedirs('.olca', exist_ok=True)
        print_stream(graph.stream(inputs, stream_mode="values"))
    except GraphRecursionError as e:
        #print(f"Error: {e}")
        print("Recursion limit reached. Please increase the 'recursion_limit' in the olca_config.yaml file.")
        print("For troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/GRAPH_RECURSION_LIMIT")

if __name__ == "__main__":
    main()
