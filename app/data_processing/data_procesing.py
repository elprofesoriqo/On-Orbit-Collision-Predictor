from .firebase_integration import save_celestrak_data, save_space_track_data
from .data_fetcher import fetch_celestrak_data, fetch_space_track_data
import pandas as pd

def main_data_processing_function():
    fetch_celestrak_data()
    fetch_space_track_data()

    celestrak_data = pd.read_csv("../data/celestrak_data.txt", sep="\s+", header=None)
    space_track_data = pd.read_csv("../data/space_track_data.txt", sep="\s+", header=None)


    save_celestrak_data(celestrak_data)
    save_space_track_data(space_track_data)
