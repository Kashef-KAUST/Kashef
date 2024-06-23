# Kashef
Kashef is a software testing tool that is meant to automate and improve software testing. It can assist software developers in generating test code for applications to ensure their reliability and robustness.

# Requirements
Python version between 3.11 and 3.13

# Setup Guide
To run this application, follow the below steps:

## 1. Install Dependenicies
To install dependenices, simply run:
```
poetry install
```

## 2. Activate Virtual Envorinment
```
poetry shell
```

## 3. Add the API keys for LLMs
Inside `src/autogenWork/OAI_CONFIG_LIST`, you need to insert the API key to invoke the LLM of your choice. 
- For **GPT** models, you can obtain the API key from you OpenAI account.
- For **Llama 2** and **Code Llama**, you can obtain the API keys from Together AI. 

## 4. Specify the LLM
For flexibility, we allow the user to select the LLM to be used  internally to generate the tests. To specify the LLM you want the Kashef to use, change the `selected_LLM` variable to one of the available options.

## 5. Add the task you would like the tool to complete 
Open the file `src/autogenWork/multipleAgents/MultipleAgents.py`. In that file, you will see a set of example tasks. you can easily modify the tasks be replacing the tag and message with your own tag and message for your defined task. You can also add additional tasks. To so, create a new task variable and add it to the list of tasks, following the same format of the existing tasks. For example, to add a 5th task, you can do:

```
task5 = {
    "tag": "counter_task", 
    "message": "Open this word counter website: https://looabuzfed.com/. Then, I want you to verify the word counting functionality and ensure it is working correctly."
    }

tasks = [task1, task2, task3, task4, task5]
```

## 6. Run the tool
To run the tool, simply run the below command and specify the task number you want the tool to execute.
```
python MultipleAgents.py <task_number>
```

For example, to run task 3, you would invoke the tool like:
```
python MultipleAgents.py 3
```

Note: the above command assumes your current working directory is `src/autogenWork/multipleAgents`. If not, run the following command:
```
cd src/autogenWork/multipleAgents
```

# There is more coming soon
The setup is a little clunky, we know. The tool is currently under progress in various aspects, and we're working on making it more effective and eventually more user-friendly. We might even have a UI at one point! Stay tuned for updates :)
