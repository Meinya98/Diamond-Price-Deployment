import streamlit as st

def inject_css():
    st.markdown("""
        <style>
        .main {
            background-color: #f8f9fa;
        }
        .stApp {
            background-color: #ffffff;
        }
        .sidebar .sidebar-content {
            background-color: #ffffff !important;
            border-right: 1px solid #e0e0e0;
        }
        .stButton>button {
            background-color: #4b6cb7;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 12px 24px;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            width: 100%;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #3a5a9c;
            transform: translateY(-1px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stNumberInput, .stSelectbox {
            background-color: #ffffff;
            border-radius: 8px;
            border: 1px solid #ced4da;
        }
        .stNumberInput input, .stSelectbox select {
            color: #495057 !important;
        }
        .stSuccess {
            background-color: rgba(0, 200, 83, 0.1) !important;
            border: 1px solid #00c853 !important;
            border-radius: 8px;
            padding: 15px;
            font-size: 18px;
            text-align: center;
            color: #00c853 !important;
        }
        .header-box {
            background-color: #f1f3f5;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            border-left: 5px solid #4b6cb7;
        }
        .section-title {
            color: #4b6cb7;
            font-weight: 600;
            margin-bottom: 15px;
        }
        .input-label {
            font-weight: 500;
            color: #495057;
            margin-bottom: 5px;
        }
        .input-description {
            font-size: 12px;
            color: #6c757d;
            margin-top: 3px;
        }
        </style>
    """, unsafe_allow_html=True)
