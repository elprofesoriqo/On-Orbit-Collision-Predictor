from fastapi import FastAPI
from .routers import orbital_data, predictions

app = FastAPI()

# Dodanie routerów dla endpointów
app.include_router(orbital_data.router)
app.include_router(predictions.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the On-Orbit Collision Predictor API"}
