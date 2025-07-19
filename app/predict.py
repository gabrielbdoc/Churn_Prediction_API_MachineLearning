import pandas as pd
from app.model import model, columns


def predict_churn(data):
    input_dict = {col: getattr(data, col) for col in columns}
    input_df = pd.DataFrame([input_dict], columns=columns)
    prediction = model.predict(input_df)[0]
    return int(prediction)