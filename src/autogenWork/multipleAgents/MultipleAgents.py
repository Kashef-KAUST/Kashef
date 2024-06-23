import sys
from typing import List, Dict

import autogen
from autogen import Agent

from logger import logThisRun
from constants import (
    swe_system_message, 
    html_system_message, 
    gpt3_swe_system_message, 
    codellama_swe_system_message, 
    llama2_swe_system_message,)

# Get command-line arguments
#---------------------------------------------------------------
task_idx = 0 # the index representing which task to pick
if len(sys.argv) > 1:
    try:
        task_idx = int(sys.argv[1]) - 1
    except ValueError:
        print(f"Invalid argument: '{sys.argv[1]}'. Please provide a valid integer.")
        exit()


# Add Tasks here
#---------------------------------------------------------------
task1 = {
    "tag": "boutique_task", 
    "message": "Checkout a random item from my own website https://cymbal-shops.retail.cymbal.dev. Make sure to complete the entire checkout process and randomize the item selection. When you reach the shipping and payment page, use the pre-filled information."
    }
task2 = {
    "tag": "counter_task", 
    "message": "Open this word counter website: https://looabuzfed.com/. Then, I want you to verify the word counting functionality and ensure it is working correctly."
    }
task3 = {
    "tag": "projoodle_task", 
    "message": "I have a website for to-do list at the address https://www.projoodle.com. Open the website and create a to-do by clicking on 'create projoodle'. When having to input information, just provide random information. For date inputs, format the date like MM/DD/YY"
    }
task4 = {
    "tag": "pastebin_task", 
    "message": "I want you to verify the functionality of this pastebin website https://privatebin.net. Specifically, you have to ensure the post data is persistent by comparing the text you posted with the text found in the generated pastebin link."
    }

tasks = [task1, task2, task3, task4]

# Select prompt message from above tasks 
#---------------------------------------------------------------
task = tasks[task_idx]


# LLM configurations
#---------------------------------------------------------------
gpt_3_tag = {"tags": ["gpt3.5turbo"]}
code_llama_tag = {"tags": ["codellama"]}
llama2_tag = {"tags": ["llama2"]}
gpt_4_tag = {"tags": ["gpt4"]}

gpt_3 = autogen.config_list_from_json(
    "../OAI_CONFIG_LIST", filter_dict=gpt_3_tag
)
code_llama = autogen.config_list_from_json(
    "../OAI_CONFIG_LIST", filter_dict=code_llama_tag
)
llama2 = autogen.config_list_from_json(
    "../OAI_CONFIG_LIST", filter_dict=llama2_tag
)
gpt_4 = autogen.config_list_from_json(
    "../OAI_CONFIG_LIST", filter_dict=gpt_4_tag
)

# LLM options to select from
#---------------------------------------------------------------
gpt_3_config = {
    "config_list": gpt_3,
    "temperature": 0,
    "timeout": 120,
    "cache_seed": None,
}
code_llama_config = {
    "config_list": code_llama,
    "temperature": 0.9,
    "timeout": 120,
    "cache_seed": None,
}
llama2_config = {
    "config_list": llama2,
    "temperature": 0,
    "timeout": 120,
    "cache_seed": None,
}
gpt_4_config = {
    "config_list": gpt_4,
    "temperature": 0,
    "timeout": 120,
    "cache_seed": None,
}

# Select LLM (CAN BE MODIFIED BY USER)
#---------------------------------------------------------------
selected_LLM = code_llama_config # replace this with the LLM you want from above options
model_tag = selected_LLM.get('config_list')[0].get('model')

# Select the appropriate swe system message
#---------------------------------------------------------------
selected_system_message = swe_system_message
if (selected_LLM == gpt_3_config):
    selected_system_message = gpt3_swe_system_message
elif (selected_LLM == code_llama_config):
    selected_system_message = codellama_swe_system_message
elif (selected_LLM == llama2_config):
    selected_system_message = llama2_swe_system_message


# Agent configurations
#---------------------------------------------------------------
executor = autogen.UserProxyAgent(
    name="Executor",
    system_message="Execute the code written by the engineer and report the result.",
    human_input_mode="ALWAYS",
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
)

swe = autogen.AssistantAgent(
    name="SWE",
    system_message=selected_system_message,
    llm_config=selected_LLM,
)

html = autogen.AssistantAgent(
    name="html",
    llm_config=selected_LLM,
    system_message=html_system_message,
)

admin = autogen.UserProxyAgent(
    name="Admin",
    code_execution_config=False,
)


# Routing logic
#---------------------------------------------------------------
def is_html(content):
    words = ["<html", "</html>"]

    is_html = False
    for word in words:
        if word in content:
            is_html = True
            break

    return is_html

def custom_speaker_selection_func(last_speaker: Agent, groupchat: autogen.GroupChat):
    messages = groupchat.messages

    # Termination condition
    if "FINAL ANSWER" in messages[-1]["content"]:
        return None

    if len(messages) <= 1:
        return swe

    if last_speaker is swe:
        return executor
    elif last_speaker is html:
        return swe
    elif last_speaker is executor:
        if is_html(messages[-1]["content"]):
            return html
        else:
            return swe

    else:
        return "random"


# Initiate workflow
#---------------------------------------------------------------
groupchat = autogen.GroupChat(
    agents=[swe, html, executor, admin],
    messages=[],
    max_round=30,
    speaker_selection_method=custom_speaker_selection_func,
)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=selected_LLM)

logThisRun(f"{model_tag}/{task['tag']}/")

print(
    f"LLM: {model_tag}\n\n\
    swe_system_message:\n{selected_system_message}\n\n\
    html_system_message:\n{html_system_message}\n\n\
    prompt:{task['message']}\n\n\
    Starting chat logging:\n"
    )

admin.initiate_chat(
    manager, message=task["message"]
)