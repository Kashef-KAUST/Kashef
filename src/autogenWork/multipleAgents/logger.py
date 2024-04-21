""" 
In your script, write `from logger import logThisRun`. Then, before the initiate_chat function, write `print(f'system_message:\n{system_message}\n\nprompt:{message}\n\nStarting chat logging:\n')`

It should look something like this:

```
from logger import logThisRun

.
.
.

logThisRun()

print(f'system_message:\n{system_message}\n\nprompt:{message}\n\nStarting chat logging:\n')

chat_res = user_proxy.initiate_chat(
    assistant,
    message=message,
    summary_method="reflection_with_llm",
)

.
.
.
```

"""

import os
import sys
import time

class DualOutput:
    def __init__(self, filename):
        self.terminal = sys.stdout
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        self.log = open(filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self): # needed for Python 3 compatibility
        # This flush method is needed because some streams might
        # use buffered output in certain contexts.
        self.terminal.flush()
        self.log.flush()

def logThisRun(sub_folder = ""):
    current_time = time.localtime()
    time_str = time.strftime("%d_%m_%y_%H_%M_%S", current_time)
    print(sub_folder)
    # Usage
    sys.stdout = DualOutput(f"logs/{sub_folder}" + f'{time_str}_log.txt')