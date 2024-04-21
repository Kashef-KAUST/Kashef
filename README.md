# Directed Research
 This repo is intended for the code we (Mustafa Almutawa and Qusai Ghabrah) write while working on our directed research requirment for KAUST.

# Software Testing Tool
This application is meant to serve as software testing tool. It can assist software developers in generating test code for applications to ensure their reliability and robustness.

 # Setup Guide
To run this application, follow the below steps:


## 1. Install Ollama
- Follow the instructions on [Ollama](https://ollama.com/)'s website to install Ollama

## 2. Pull the desired LLMs
- After installing Ollama, pull the desired LLM from [Ollama](https://ollama.com/library)'s library of models. To do this, open the terminal and run the following:
```
ollama pull <model name>
```
- Note: replace \<model name> with the LLM you want to download

## 3. Install Dependencies
- To install the project's required dependencies, run the following command:
```
poetry install
```

## 4. Run the Software Testing Assistant!
- To run the software testing tool, simply run:
```
python codellama.py
```