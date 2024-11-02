import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("../orbit-d8ec9-firebase-adminsdk-3mpgc-334631a536.json")  # Ścieżka do pliku JSON z kluczem serwisowym
firebase_admin.initialize_app(cred)

db = firestore.client()

def save_celestrak_data(celestrak_data):
    celestrak_ref = db.collection("celestrak_data")
    for index, row in celestrak_data.iterrows():
        celestrak_ref.add(row.to_dict())

def save_space_track_data(space_track_data):
    space_track_ref = db.collection("space_track_data")
    for index, row in space_track_data.iterrows():
        space_track_ref.add(row.to_dict())

def save_rocket_launches_data(data):
    launches_ref = db.collection("rocket_launches")
    for index, row in data.iterrows():
        launches_ref.add(row.to_dict())