from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .agent import run_orchestration

app = FastAPI(title="PromptOrchestratorAPI")

class RequestModel(BaseModel):
    instruction: str

@app.post("/orchestrate")
async def orchestrate(request: RequestModel):
    try:
        result = run_orchestration(request.instruction)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}
