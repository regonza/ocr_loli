from fastapi import APIRouter, HTTPException
from backend.agents.langgraph_agent import LangGraphAgent

router = APIRouter()
agent = LangGraphAgent()

@router.post("/agent/")
async def interact_with_agent(prompt: str):
    """ Endpoint para interactuar con el agente LangGraph """
    try:
        response = agent.run(prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))