import logging
from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    logging.info("Adding CORS middleware")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://localhost:5173"],  # Adjust this to your frontend's URLs
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )