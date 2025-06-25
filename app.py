import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.wsgi import WSGIMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djapp.settings")

from django.core.wsgi import get_wsgi_application

# Load env variables
S3 = os.environ.get("S3")
DATABASE_URL = os.environ.get("DATABASE_URL")

app = FastAPI()

# Mount Django at /django (optional, for demonstration)
app.mount("/django", WSGIMiddleware(get_wsgi_application()))

@app.get("/health")
def health():
    return JSONResponse({"status": "ok"})
