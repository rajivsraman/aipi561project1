# AIPI 561 (Operationalizing AI) - Week 1 Project
### Author: Rajiv Raman
### Institution: Duke University
### Date: June 15th, 2025

## Overview

This project implements a lightweight conversational assistant using Amazon Bedrock's Titan model. It includes memory-aware prompt construction, error handling, and a testable API interface.

## Features

- Basic prompt management with 6-message conversation memory
- Integration with Amazon Bedrock Titan model
- Error handling with detailed failure messages
- FastAPI-based REST endpoint (`/chat`)
- Unit tests using `pytest` and `monkeypatch`
- Test coverage reporting with `pytest-cov`

## File Overview

- `chatbot.py` – Chat logic and prompt construction
- `main.py` – FastAPI application for the chat endpoint
- `tests/test_chatbot.py` – Unit tests for core logic

## Requirements

- boto3
- fastapi
- uvicorn
- pytest
- httpx

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn main:app --reload
```

Access Swagger UI at:

```
http://127.0.0.1:8000/docs
```

## Running Tests

```bash
pytest --cov=.
```

## Notes

- AWS credentials must be configured using `aws configure`
- Ensure access to `amazon.titan-text-premier-v1:0` via Bedrock
