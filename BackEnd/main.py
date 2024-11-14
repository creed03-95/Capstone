from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.chat_router import router as chat_router

app = FastAPI(
    title="Chat API",
    description="""
    This API provides endpoints for generating AI chat responses using LangChain and OpenAI.
    
    ## Features
    
    * Generate AI responses using GPT models
    * Provide context for more accurate responses
    * Easy-to-use REST API
    
    ## Authentication
    
    This API requires an OpenAI API key to be set in the environment variables.
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api/v1", tags=["chat"])