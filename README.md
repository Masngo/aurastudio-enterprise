# 🌟 AuraStudio Enterprise
### Autonomous Multi-Modal Skin-VTO Agentic Platform

> **Submitted to:** YouCam API Skin AI & eCommerce VTO Hackathon  
> **Core Innovation:** Bridging clinical-grade skin diagnostics with cross-category apparel virtual try-on using an autonomous multi-agent orchestration swarm.

---

## 🚀 Overview
Shoppers rarely buy skincare and fashion in isolation—skin health and personal styling are intrinsically linked self-image experiences. **AuraStudio Enterprise** is an AI-powered retail concierge built with **YouCam APIs** that transforms static e-commerce into an intelligent, personalized, and interactive journey.

Instead of a surface-level wrapper, AuraStudio deploys an **agentic architecture** that analyzes 28+ skin concerns via YouCam's Skin AI, maps facial undertones using the Color Tone API, and dynamically coordinates apparel Virtual Try-On (VTO) to deliver complete, tailored retail recommendations.

---

## 🛠️ Architecture & Tech Stack

```text
  [ Next.js 14 Frontend ] <--- REST / JSON ---> [ FastAPI Python Backend ]
                                                           |
                                                [ LangGraph Agent Swarm ]
                                                /           |          \
                                              (Skin AI)  (Color)     (VTO API)
Frontend: Next.js (App Router), TypeScript, Tailwind CSS, Lucide Icons

Backend: Python, FastAPI, Pydantic, Uvicorn

Agent Orchestration: LangGraph / Multi-Agent Decision Engine

APIs Integrated: YouCam Skin AI Analysis API, Facial Color Tones API, and Apparel VTO API

Deployment & Containerization: Docker & Docker Compose

🏁 Quick Start (Run Locally with Docker)
Clone the repository and navigate to the root directory:
cd aurastudio-enterprise
Configure your environment variables:
Create a .env file in the root directory:
YOUCAM_API_KEY=your_actual_youcam_api_key_here
YOUCAM_BASE_URL=[https://api.perfectcorp.com/v1](https://api.perfectcorp.com/v1)
(Note: Built-in mock fallback handlers ensure smooth offline testing if credentials are pending).

Build and run via Docker Compose:
docker compose up --build -d
Access the Application:

Frontend UI: http://localhost:3000

Backend API Docs (Swagger): http://localhost:8000/docs

💡 Key Features
Autonomous Skin Diagnostics: Processes YouCam Skin AI payloads to evaluate wrinkles, spots, texture, and redness with severity scoring.

Intelligent Product & Outfit Matching: Cross-references facial undertones with seasonal apparel catalogs.

Seamless VTO Pipeline: Renders virtual try-ons that bridge skincare outcomes with apparel styling.
