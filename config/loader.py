import pickle

# Load models and preprocessing objects
with open('xgbr_model.pkl', 'rb') as file:
    XGBR_Model = pickle.load(file)
    
with open('feature_columns.pkl', 'rb') as file:
    feature_columns = pickle.load(file)
    
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)