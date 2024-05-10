# Software Testing Tool
This application is meant to serve as software testing tool. It can assist software developers in generating test code for applications to ensure their reliability and robustness.

 # Setup Guide
To run this application, follow the below steps:


## 1. Install Dependenicies
To install dependenices, simply run:
```
poetry install
```

## 2. Add the task you would like the tool to complete 
Open the file `src/autogenWork/multipleAgents/MultipleAgents.py`. In that file, you will see a set of example tasks. you can easily modify the tasks be replacing the tag and message with your own tag and message for your defined task. You can also add additional tasks. To so, create a new task variable and add it to the list of tasks, following the same format of the existing tasks. For example, to add a 5th task, you can do:

```
task5 = {
    "tag": "counter_task", 
    "message": "Open this word counter website: https://looabuzfed.com/. Then, I want you to verify the word counting functionality and ensure it is working correctly."
    }

tasks = [task1, task2, task3, task4, task5]
```

## 3. Run the tool
To run the tool, simply run the below command and specify the task number you want the tool to execute.
```
python MultipleAgents.py <task_number>
```

For example, to run task 3, you would invoke the tool like:
```
python MultipleAgents.py 3
```

# There is more coming soon
The setup is a little clunky, we know. The tool is currently under progress in various aspects, and we're working on making it more effective and eventually more user-friendly. We might even have a UI at one point! Stay tuned for updates :)
