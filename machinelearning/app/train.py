import joblib
import numpy as np

def model():
    # Load the trained model
    loaded_model = joblib.load('app\\training\KNN.pkl')
    return loaded_model

def get_prediction(model, input_dict):
    model= model()
    numeric_input = {k: float(v) for k, v in input_dict.items() if isinstance(v, (int, float)) or v.isnumeric()}

    input_data = np.array(list(numeric_input.values())).reshape(1, -1)

    prediction = model.predict(input_data)

    labels = {0: "lành tính", 1: "ác tính"}
    prediction_label = labels[prediction[0]]

    return prediction_label