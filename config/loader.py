import os
import pickle

BASE_DIR = os.path.dirname(__file__)  # path to /config

with open(os.path.join(BASE_DIR, 'xgbr_model.pkl'), 'rb') as file:
    XGBR_Model = pickle.load(file)

with open(os.path.join(BASE_DIR, 'feature_columns.pkl'), 'rb') as file:
    feature_columns = pickle.load(file)

with open(os.path.join(BASE_DIR, 'scaler.pkl'), 'rb') as file:
    scaler = pickle.load(file)

with open(os.path.join(BASE_DIR, 'encoder.pkl'), 'rb') as file:
    encoder = pickle.load(file)
