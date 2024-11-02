from sqlalchemy import create_engine
import pandas as pd

def save_to_database(data, db_url):
    engine = create_engine(db_url)
    with engine.connect() as connection:
        pd.DataFrame(data).to_sql('celestrak_data', con=connection, if_exists='replace', index=False)
