"""Static host for the Screwfix Selling Platform vendor landing page."""
import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(title="Screwfix Selling Platform")


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html", media_type="text/html")


@app.get("/health")
def health():
    return {"status": "ok"}


# Everything else (e.g. static/assets/ logo) served straight from static/
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("DATABRICKS_APP_PORT", "8000")))
