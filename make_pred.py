import joblib
import numpy as np
from tensorflow import keras

reconstructed_model = keras.models.load_model(
    "./utils/test_prediction_model.keras")
scaler_loaded = joblib.load(
    './utils/scaler.pkl')


def predict(input_dataset):
    dataset = np.array(input_dataset).astype(np.int16)
    dataset = dataset.reshape(1, -1)
    dataset = scaler_loaded.transform(dataset)
    prediction = reconstructed_model.predict(dataset)
    return prediction.item()
