from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
import json

app = FastAPI()


class Item(BaseModel):
    prompt: str


@app.get("/.well-known/ai-plugin.json", include_in_schema=False)
async def serve_manifest():
    try:
        with open(".well-known/ai-plugin.json") as file:
            manifestData = file.read()
        return JSONResponse(content=json.loads(manifestData))
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="manifest file not found")
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
