from fastapi import FastAPI
from .routers import orbital_data, predictions
from .services.data_processor import clean_and_process_data

app = FastAPI()

# Dodanie routerów dla endpointów
app.include_router(orbital_data.router)
app.include_router(predictions.router)

@app.on_event("startup")
async def startup_event():
    # Wywołaj funkcję czyszczenia i przetwarzania danych
    clean_and_process_data("../data/celestrak_data.txt", "../data/space_track_data.txt")

@app.get("/")
async def root():
    return {"message": "Welcome to the On-Orbit Collision Predictor API"}
