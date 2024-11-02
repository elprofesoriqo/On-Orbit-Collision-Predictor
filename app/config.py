
import firebase_admin
from firebase_admin import credentials, firestore

# Inicjalizacja Firebase
cred = credentials.Certificate("../orbit-d8ec9-firebase-adminsdk-3mpgc-334631a536.json")  # Ścieżka do pliku JSON z kluczem serwisowym
firebase_admin.initialize_app(cred)

# Inicjalizacja Firestore
db = firestore.client()
