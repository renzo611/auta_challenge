from fastapi import APIRouter
from services.additional_service import AdditionalService
from schemas.additional import Additional

app = APIRouter()

@app.get("/resolve")
async def get_all(additional: Additional):
    return AdditionalService.is_balanced_word(additional.word)