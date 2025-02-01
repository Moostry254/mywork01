from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Initialize the FastAPI app
app = FastAPI()

# Mount the static directory for CSS, images, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up the templates directory using Jinja2
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    """
    The main route that renders the portfolio homepage.
    """
    return {"message": "Hello, FastAPI is running!"}
