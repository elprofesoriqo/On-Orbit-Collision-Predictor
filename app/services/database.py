from app.config import db

def save_orbital_data(data):
    """
    Zapisuje dane orbitalne do Firestore.

    :param data: DataFrame z danymi orbitalnymi
    """
    for index, row in data.iterrows():
        db.collection("orbital_data").add(row.to_dict())

def get_orbital_data_from_firestore():
    """
    Pobiera dane orbitalne z Firestore.

    :return: Lista dokumentów
    """
    docs = db.collection("orbital_data").stream()
    return [doc.to_dict() for doc in docs]
