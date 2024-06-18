import joblib
import numpy as np
import keras

reconstructed_model = keras.models.load_model(
    "/Users/alankwiecien/Documents/Studia/PJATK_Informatyka/Semestr VIII/SUML/Projekt/SUML/utils/test_prediction_model.keras")
scaler_loaded = joblib.load(
    '/Users/alankwiecien/Documents/Studia/PJATK_Informatyka/Semestr VIII/SUML/Projekt/SUML/utils/scaler.pkl')


def predict(dataset):
    my_dataset = np.array(dataset).astype(np.int16)
    my_dataset = my_dataset.reshape(1, -1)
    my_dataset = scaler_loaded.transform(my_dataset)
    prediction = reconstructed_model.predict(my_dataset)
    return prediction.item()

