import pandas as pd
from firebase_integration import save_celestrak_data, save_space_track_data, save_rocket_launches_data
from .data_fetcher import fetch_celestrak_data, fetch_space_track_data, fetch_rocket_launches

def clean_and_process_data(celestrak_file_path, space_track_file_path):
    celestrak_data = pd.read_csv(celestrak_file_path, sep="\s+", header=None)
    space_track_data = pd.read_csv(space_track_file_path, sep="\s+", header=None)

    rocket_launches = fetch_rocket_launches()
    if rocket_launches:
        launch_df = pd.DataFrame(rocket_launches)
        save_rocket_launches_data(launch_df)


    save_celestrak_data(celestrak_data)
    save_space_track_data(space_track_data)

    return celestrak_data, space_track_data, launch_df
