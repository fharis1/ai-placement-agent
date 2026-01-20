"""
FastAPI application for the AI Placement Preparation Agent.
This is the main entry point of the application that sets up the API server
and defines the /generate-plan endpoint.
""" 
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import PlacementRequest, PlacementResponse
from agent import generate_placement_plan

# Initialize FastAPI application
app = FastAPI(
    title="AI Placement Preparation Agent",
    description="An AI-powered backend for generating personalized placement preparation plans",
    version="1.0.0"
)

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "message": "AI Placement Preparation Agent API",
        "status": "running",
        "endpoints": {
            "/generate-plan": "POST - Generate placement preparation plan"
        }
    }


from fastapi.responses import PlainTextResponse

@app.post("/generate-plan", response_class=PlainTextResponse)
async def generate_plan(request: PlacementRequest):
    try:
        result = await generate_placement_plan(
            request.resume_text,
            request.target_role,
            request.weak_areas
        )

        return str(result)   # 🔥 FORCE STRING

    except Exception as e:
        return PlainTextResponse(
            content=f"Error generating placement plan: {str(e)}",
            status_code=500
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating placement plan: {str(e)}"
        )
