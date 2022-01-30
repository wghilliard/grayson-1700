from fastapi import FastAPI, Depends

from .models import NERRequest, NERResult
from .ner import Processor

app = FastAPI()


async def get_ner_processor() -> Processor:
    return Processor()


@app.get("/health")
async def get_health():
    return True


@app.post("/ner", response_model=NERResult)
async def process_ner(request: NERRequest, processor=Depends(get_ner_processor)):
    return processor.extract_ner(request)
