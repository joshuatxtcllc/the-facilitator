# The Facilitator - Prompt Orchestrator

A FastAPI-based prompt orchestration service that transforms raw user instructions into structured prompts and executes them using AI.

## Features

- 🚀 High-level prompt engineering automation
- 🔄 Two-phase orchestration (Prompt Writing → Execution)
- 🏥 Built-in health checks
- 🌐 RESTful API interface
- ⚡ Fast and scalable with FastAPI

## Quick Start

### Prerequisites

- Python 3.11+
- OpenAI API Key

### Local Development

1. Clone the repository:
```bash
git clone <your-repo-url>
cd the-facilitator
```

2. Navigate to the prompt-orchestrator directory:
```bash
cd prompt-orchestrator
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### POST /orchestrate
Orchestrate a prompt from a raw instruction.

**Request Body:**
```json
{
  "instruction": "your raw instruction here"
}
```

**Response:**
```json
{
  "generated_prompt": "structured prompt...",
  "final_action_output": "execution result..."
}
```

### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "ok"
}
```

## Deployment on Railway

### Method 1: Deploy from GitHub (Recommended)

1. Fork or push this repository to GitHub

2. Visit [Railway.app](https://railway.app) and sign in

3. Click "New Project" → "Deploy from GitHub repo"

4. Select your repository

5. Railway will automatically detect the configuration from `railway.toml` and `nixpacks.toml`

6. Add environment variables:
   - Click on your service
   - Go to "Variables" tab
   - Add `OPENAI_API_KEY` with your OpenAI API key

7. Deploy! Railway will:
   - Install Python 3.11
   - Install dependencies from `requirements.txt`
   - Start the application with uvicorn
   - Provide you with a public URL

### Method 2: Deploy with Railway CLI

1. Install Railway CLI:
```bash
npm install -g @railway/cli
```

2. Login to Railway:
```bash
railway login
```

3. Initialize project:
```bash
railway init
```

4. Add environment variables:
```bash
railway variables set OPENAI_API_KEY=your_key_here
```

5. Deploy:
```bash
railway up
```

### Required Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `PORT` | Server port (automatically set by Railway) | No (default: 8080) |

## Project Structure

```
the-facilitator/
├── prompt-orchestrator/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py        # FastAPI application
│   │   ├── agent.py       # Orchestration logic
│   │   └── tools.py       # Helper tools
│   ├── requirements.txt   # Python dependencies
│   ├── railway.toml       # Railway configuration
│   └── .env.example       # Environment template
├── railway.toml           # Root Railway config
├── nixpacks.toml          # Build configuration
└── README.md              # This file
```

## How It Works

1. **Prompt Writer Phase**: Takes raw user input and transforms it into a structured, detailed prompt with:
   - Role definition
   - Clear goals
   - Constraints
   - Actionable steps

2. **Action Agent Phase**: Executes the structured prompt and returns the result

## Monitoring

Railway provides built-in monitoring:
- View logs in the Railway dashboard
- Monitor deployment status
- Track resource usage
- Set up custom alerts

## Troubleshooting

### Build fails on Railway
- Check that `OPENAI_API_KEY` is set in Railway variables
- Verify `requirements.txt` is in the `prompt-orchestrator` directory
- Check deployment logs in Railway dashboard

### Application crashes on startup
- Ensure `OPENAI_API_KEY` is valid
- Check Railway logs for specific error messages
- Verify all dependencies are installed

### Health check fails
- Ensure the `/health` endpoint is accessible
- Check if the port configuration is correct
- Verify firewall/security settings in Railway

## Development

To extend the application:

1. Add new tools in `app/tools.py`
2. Update agent logic in `app/agent.py`
3. Add new endpoints in `app/main.py`
4. Update `requirements.txt` if adding new dependencies

## License

[Add your license here]

## Support

For issues and questions:
- Check Railway deployment logs
- Review the API documentation at `/docs` (FastAPI auto-generated)
- Open an issue on GitHub
