import streamlit as st
from styles.custom_css import inject_css

def show():
    inject_css()

    st.markdown("""
<div class="header-box">
    <h1 style="color: #2c3e50; text-align: center; margin-bottom: 5px;">
        Diamond Price Prediction
    </h1>
    <p style="color: #6c757d; text-align: center; font-size: 16px;">
        Estimate the market value of your diamond with precision
    </p>
</div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style="background-color: #f8f9fa; border-radius: 10px; padding: 20px; margin-bottom: 20px;">
    <h3 style="color: #2c3e50;">About This App</h3>
    <p style="color: #495057;">
        This tool helps you estimate the market value of diamonds based on their unique characteristics. 
        Our advanced machine learning model analyzes various diamond attributes to provide an accurate price prediction.
    </p>
</div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style="background-color: #f8f9fa; border-radius: 10px; padding: 20px; margin-bottom: 20px;">
    <h3 style="color: #2c3e50;">How To Use</h3>
    <ol style="color: #495057;">
        <li>Navigate to the <b>Price Prediction</b> section</li>
        <li>Enter your diamond's specifications</li>
        <li>Click "Predict Diamond Price"</li>
        <li>View your estimated diamond value</li>
    </ol>
</div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style="background-color: #f8f9fa; border-radius: 10px; padding: 20px;">
    <h3 style="color: #2c3e50;">Data Source</h3>
    <p style="color: #495057;">
        Our model was trained on a comprehensive dataset from Kaggle:<br>
        <a href="https://www.kaggle.com/datasets/nancyalaswad90/diamonds-prices/data" 
           style="color: #4b6cb7; text-decoration: none;">
           Diamond Prices Dataset
        </a>
    </p>
</div>
    """, unsafe_allow_html=True)
