# Week 1 – Conversational AI Assistant

A simple conversational AI assistant using Amazon Bedrock's Titan model. Includes basic memory, prompt construction, and error handling.

## Features

- Maintains a 6-message prompt history
- Stateless, class-based chatbot design
- Integration with Amazon Titan model via Bedrock Runtime API
- Exception-safe model invocation
- FastAPI REST endpoint for chat access
- Unit tests with monkeypatching
- Test coverage with `pytest-cov`

## File Overview

- `chatbot.py`: Core chatbot logic
- `main.py`: FastAPI API wrapper
- `tests/test_chatbot.py`: Unit tests

## Dependencies

- boto3
- fastapi
- uvicorn
- pytest
- httpx

## Running

Start the API server:

