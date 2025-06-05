import pandas as pd
import numpy as np
from config.loader import XGBR_Model, feature_columns, scaler, encoder

def predict(carat, cut, color, clarity, depth, table, x, y, z):
    # Processing user input
    input_data = {
        'carat': carat,
        'cut': cut,
        'color': color,
        'clarity': clarity,
        'depth': depth,
        'table': table,
        'x': x,
        'y': y,
        'z': z
    }
    df_predict = pd.DataFrame([input_data])
    df_predict = df_predict.drop(columns=['depth'], errors='ignore')
    
    # Encoding ordinal features
    df_predict[['cut', 'color', 'clarity']] = encoder.fit_transform(
        df_predict[['cut', 'color', 'clarity']])
    
    # Reindex to match the model's expected input
    df_predict = df_predict.reindex(columns=feature_columns, fill_value=0)

    # Scaling the features
    df_predict = scaler.transform(df_predict[feature_columns])

    # Making prediction
    log_prediction = XGBR_Model.predict(df_predict)
    result = np.expm1(log_prediction)[0]  # Inverse log transformation
    
    # Round result to 2 decimal places for currency
    return round(result, 2)