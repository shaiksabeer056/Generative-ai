import sys
import os
import uvicorn
from dotenv import load_dotenv

# Set the base directory to the project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Add the backend folder to sys.path so Python can find 'app'
sys.path.insert(0, os.path.join(BASE_DIR, "backend"))

# Load environment variables from backend/.env
load_dotenv(os.path.join(BASE_DIR, "backend", ".env"))

# Import the FastAPI app
try:
    from app.main import app
except ImportError as e:
    print(f"Error importing FastAPI app: {e}")
    sys.exit(1)

if __name__ == "__main__":
    print("Starting FinRelief AI Backend server...")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
