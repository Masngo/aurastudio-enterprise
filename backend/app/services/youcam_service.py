import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class YouCamAPIService:
    def __init__(self):
        self.api_key = os.getenv("YOUCAM_API_KEY")
        self.base_url = os.getenv("YOUCAM_BASE_URL", "https://api.perfectcorp.com/v1")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}" if self.api_key else "",
            "Content-Type": "application/json"
        }

    def analyze_skin(self, image_url: str) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/skin-ai/analyze"
        try:
            response = requests.post(endpoint, json={"image_url": image_url}, headers=self.headers, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {
                "status": "success",
                "mock": True,
                "skin_score": 82,
                "metrics": {
                    "wrinkles": {"score": 12, "severity": "low"},
                    "spots": {"score": 25, "severity": "moderate"},
                    "texture": {"score": 18, "severity": "low"},
                    "redness": {"score": 30, "severity": "moderate"}
                },
                "error": str(e)
            }

    def render_apparel_vto(self, user_image_url: str, garment_item_id: str) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/vto/apparel"
        try:
            response = requests.post(endpoint, json={"user_image_url": user_image_url, "garment_item_id": garment_item_id}, headers=self.headers, timeout=45)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {
                "status": "success",
                "mock": True,
                "rendered_vto_url": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=800&q=80",
                "error": str(e)
            }

youcam_service = YouCamAPIService()
