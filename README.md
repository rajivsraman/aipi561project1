# AIPI 561 (Operationalizing AI) - Week 1 Project
### Author: Rajiv Raman
### Institution: Duke University
### Date: June 15th, 2025

## Overview

This project implements a command-line conversational assistant using Amazon Bedrock's Titan model. The assistant supports message history, error handling, and a test suite with coverage.

## Features

- Uses `amazon.titan-text-premier-v1:0` via AWS Bedrock
- Maintains 6-line conversation history
- Simple interface via `run_chat.py` CLI
- Graceful handling of API and permission errors
- Modular class structure for testing and reuse
- Pytest-based unit tests with coverage support

## File Overview

- `chatbot.py` – `TitanChatBot` class for prompt building and model invocation
- `run_chat.py` – CLI script for interacting with the chatbot
- `tests/test_chatbot.py` – Unit tests for prompt logic and error handling
- `requirements.txt` – Dependency list

## Requirements

- boto3
- pytest
- httpx
- coverage (optional for test reporting)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Chatbot

Use the CLI script:

```bash
python run_chat.py
```

## Running Tests

```bash
pytest --cov=.
```

## Notes

- Make sure you have AWS credentials configured via `aws configure`
- The IAM user must have access to `amazon.titan-text-premier-v1:0`
- Tests are mocked and do not require real AWS API calls

