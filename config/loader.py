import pickle

def load_pickle(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

XGBR_Model = load_pickle('xgbr_model.pkl')
feature_columns = load_pickle('feature_columns.pkl')
scaler = load_pickle('scaler.pkl')
encoder = load_pickle('encoder.pkl')
