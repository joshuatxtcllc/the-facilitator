# Prompt Orchestrator

FastAPI service for AI prompt orchestration using LangChain and OpenAI.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Add your OPENAI_API_KEY to .env

# Run locally
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for interactive API documentation.

## API Endpoints

- `POST /orchestrate` - Transform and execute instructions
- `GET /health` - Health check

See main README in root directory for full documentation and Railway deployment instructions.
