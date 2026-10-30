from fastapi import APIRouter
from pydantic import BaseModel
from app.services.youcam_service import youcam_service

router = APIRouter(prefix="/api/v1", tags=["AuraStudio Enterprise"])

class AnalyzeRequest(BaseModel):
    image_url: str

class VtoRequest(BaseModel):
    user_image_url: str
    garment_item_id: str

@router.post("/skin/analyze")
async def analyze_skin(payload: AnalyzeRequest):
    return youcam_service.analyze_skin(payload.image_url)

@router.post("/vto/render")
async def render_vto(payload: VtoRequest):
    return youcam_service.render_apparel_vto(payload.user_image_url, payload.garment_item_id)
