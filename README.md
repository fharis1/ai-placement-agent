# AI Placement Preparation Agent

A FastAPI backend application that uses Pydantic AI to generate personalized placement preparation plans, interview questions, and resume feedback.

## 📁 Project Structure & File Explanations

### `main.py`
**Purpose**: The main FastAPI application file that serves as the entry point for the API server.

**What it does**:
- Initializes the FastAPI application with title, description, and version
- Configures CORS (Cross-Origin Resource Sharing) middleware to allow frontend requests
- Defines the `/generate-plan` POST endpoint that accepts placement requests
- Handles errors and returns appropriate HTTP status codes
- Includes a root endpoint (`/`) for health checks

**Key Components**:
- FastAPI app instance
- CORS middleware configuration
- `/generate-plan` endpoint handler

---

### `models.py`
**Purpose**: Defines Pydantic models for request/response validation and data structure.

**What it does**:
- **`PlacementRequest`**: Validates incoming API requests with fields:
  - `resume_text`: User's resume content (50-5000 characters)
  - `target_role`: Target job role (3-200 characters)
  - `weak_areas`: Areas needing improvement (10-500 characters)
  
- **`PlacementResponse`**: Structures the API response with:
  - `study_plan`: Contains a detailed study plan
  - `interview_questions`: Contains a list of interview questions
  - `resume_feedback`: Contains feedback and improvement suggestions

**Why it's important**: Pydantic automatically validates incoming data and generates clear error messages if validation fails, ensuring data quality.

---

### `agent.py`
**Purpose**: Contains the AI agent logic using Pydantic AI library.

**What it does**:
- Initializes an AI agent using `pydantic_ai` with OpenRouter model integration
- Configures the agent with a system prompt defining its role as a career counselor
- Uses a free OpenRouter model (`qwen/qwen-2.5-7b-instruct`)
- Implements `generate_placement_plan()` function that:
  - Takes resume text, target role, and weak areas as input
  - Constructs a detailed prompt for the AI
  - Calls the AI agent to generate the response
  - Returns structured data matching the `PlacementResponse` model

**Key Features**:
- Environment variable management for API keys
- Error handling for missing API keys
- Structured output using Pydantic models

---

### `requirements.txt`
**Purpose**: Lists all Python package dependencies needed for the project.

**Dependencies**:
- `fastapi`: Web framework for building APIs
- `uvicorn`: ASGI server to run the FastAPI application
- `pydantic`: Data validation library
- `pydantic-ai`: AI agent framework that integrates with various LLM providers
- `python-dotenv`: Loads environment variables from `.env` file
- `httpx`: HTTP client library (dependency of pydantic-ai)

---

### `.env.example`
**Purpose**: Template file showing what environment variables are needed.

**What it contains**:
- Example format for `OPENROUTER_API_KEY`
- Instructions on where to get the API key

**Usage**: Copy this file to `.env` and fill in your actual API key.

---

### `.gitignore`
**Purpose**: Prevents sensitive files and build artifacts from being committed to version control.

**What it ignores**:
- Python cache files (`__pycache__/`)
- Virtual environments (`venv/`, `env/`)
- Environment files (`.env` containing API keys)
- IDE configuration files
- OS-specific files

---

## 🚀 Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Get a free OpenRouter API key:
   - Visit https://openrouter.ai/
   - Create an account
   - Generate an API key
   - Add it to your `.env` file:
     ```
     OPENROUTER_API_KEY=your_actual_api_key_here
     ```

### 3. Run the Server
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### 4. Test the API
Visit `http://localhost:8000/docs` for interactive API documentation (Swagger UI)

Or use curl:
```bash
curl -X POST "http://localhost:8000/generate-plan" \
  -H "Content-Type: application/json" \
  -d '{
    "resume_text": "Software Engineer with 2 years experience in Python and web development...",
    "target_role": "Senior Software Engineer",
    "weak_areas": "System design, Algorithms, Data structures"
  }'
```

## 📝 API Endpoint

### POST `/generate-plan`

**Request Body**:
```json
{
  "resume_text": "Your resume content here...",
  "target_role": "Target Job Role",
  "weak_areas": "Areas to improve"
}
```

**Response**:
```json
{
  "study_plan": {
    "plan": "Week-by-week study plan..."
  },
  "interview_questions": {
    "questions": ["Question 1", "Question 2", ...]
  },
  "resume_feedback": {
    "feedback": "Detailed feedback...",
    "suggestions": ["Suggestion 1", "Suggestion 2", ...]
  }
}
```

## 🔧 Customization

### Changing the AI Model
In `agent.py`, you can change the `model_id` to any other free model available on OpenRouter:
```python
model=OpenRouterModel(
    model_id='google/gemini-flash-1.5-8b',  # Change this
    api_key=OPENROUTER_API_KEY,
)
```

### Adjusting Validation Rules
In `models.py`, modify the `Field()` parameters to change validation rules (min/max length, etc.)

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic AI Documentation](https://ai.pydantic.dev/)
- [OpenRouter Models](https://openrouter.ai/models)
