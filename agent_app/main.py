from fastapi import FastAPI
from pydantic import BaseModel
from agent_app.agent import ask_agent

app = FastAPI(title="ADK MCP AI Agent")


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def health():
    return {"status": "ok", "service": "adk-mcp-ai-agent"}


@app.post("/ask")
def ask(request: QueryRequest):
    return ask_agent(request.query)
