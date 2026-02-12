import os
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .agent import run_orchestration

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Prompt Orchestrator API",
    description="AI-powered prompt orchestration service",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this based on your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestModel(BaseModel):
    instruction: str

    class Config:
        json_schema_extra = {
            "example": {
                "instruction": "Create a detailed plan for building a web application"
            }
        }

@app.on_event("startup")
async def startup_event():
    logger.info("Starting Prompt Orchestrator API")
    logger.info(f"Environment: {os.getenv('RAILWAY_ENVIRONMENT', 'local')}")

    # Verify OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        logger.warning("OPENAI_API_KEY not set - API calls will fail")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Prompt Orchestrator API")

@app.get("/")
def root():
    """Root endpoint with API information"""
    return {
        "name": "Prompt Orchestrator API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }

@app.get("/health")
def health():
    """Health check endpoint for Railway and monitoring"""
    return {
        "status": "ok",
        "service": "prompt-orchestrator"
    }

@app.post("/orchestrate")
async def orchestrate(request: RequestModel):
    """
    Orchestrate a prompt from raw instruction.

    Takes a user instruction, converts it to a structured prompt,
    and executes it with an AI agent.
    """
    try:
        logger.info(f"Processing orchestration request: {request.instruction[:100]}...")
        result = run_orchestration(request.instruction)
        logger.info("Orchestration completed successfully")
        return result
    except Exception as e:
        logger.error(f"Orchestration failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
