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
from langchain_openai import ChatOpenAI,OpenAI
from langchain.agents import AgentExecutor, create_react_agent

from langchain_community.agent_toolkits.load_tools import load_tools

import warnings
#

# Suppress the specific UserWarning
warnings.filterwarnings("ignore", category=UserWarning, message="The shell tool has no safeguards by default. Use at your own risk.")

from langchain_community.tools.shell import ShellTool


# %%
from langchain_core.tools import Tool


# %%

from typing import Literal

from langchain_core.tools import tool

from langgraph.prebuilt import create_react_agent
from langgraph.errors import GraphRecursionError


# %%


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

# %%


recursion_limit=11

shell_tool = ShellTool()
model_name="gpt-4o"
model_name="gpt-4o-mini"
llm = ChatOpenAI(model=model_name, temperature=0)
math_llm = OpenAI(temperature=0.0)
#tools = [shell_tool, ]
tools = load_tools(
    ["human", "llm-math","terminal"],
    llm=math_llm,
    allow_dangerous_tools=True,
)

# Define the graph
graph = create_react_agent(llm, tools=tools)

if graph.config is None:
  graph.config = {}
graph.config["recursion_limit"] = recursion_limit

outpath="/b/Dropbox/_jgongery/orpheus/x/321-olca/olca_tst_python_interpret_241031b"
system_instructions="You are going to explore the creation of capabilities by creating python code, saving and running these functions. Commit and push your work to the repository linked to issue #343. Store in ./src your code."
user_input=" Create a CLI that generate fractal images and have great arguments to parametrize the fractal being generated.  You implement the funtions in the code (try using existing code if you find any in ./src, keep it simple and upgrade existing code if required). Make sure you validate your syntax (try running the command few times with output in ./generated_images (folder you create).  You tend just to badly escape the input and output of the command.  You can use the following libraries: PIL, numpy, matplotlib, and click.  You can use the following code as a base: "
inputs = prepare_input(user_input, system_instructions)

try:
  print_stream(graph.stream(inputs, stream_mode="values"))
except GraphRecursionError as e:
  print("Recursion limit reached. Please increase the 'recursion_limit' in the olca_config.yaml file.")
  print("For troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/GRAPH_RECURSION_LIMIT")
# %%
