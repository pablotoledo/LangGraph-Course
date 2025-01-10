# LangChain Reflection Agent

## Overview

This project demonstrates the use of LangChain and AzureChatOpenAI to create a reflection agent for Twitter posts. The agent can generate critique and recommendations for tweets, as well as write excellent Twitter posts.

## Setting Up the .env File

To configure the environment variables for this project, create a `.env` file in the `exercise_1` directory with the following content:

```
    LANGCHAIN_TRACING_V2=true
    LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
    LANGCHAIN_API_KEY="your_langchain_api_key"
    LANGCHAIN_PROJECT="learning-reflection-agent"
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="your_azure_openai_endpoint"
```

## Project Structure

The project consists of the following files:

- `src/main.py`: Main script that processes tweets using the reflection and generation chains.
- `src/chains.py`: Defines the prompts and chains for generating critique, recommendations, and Twitter posts.

## Usage

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Set up the `.env` file with your API keys.

3. Run the script:
   ```bash
   python src/main.py
   ```

4. The script will process an input tweet and print the steps and final response.
