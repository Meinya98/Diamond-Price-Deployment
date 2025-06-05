import streamlit as st
import pandas as pd
from model.predictor import predict
from styles.custom_css import inject_css

def show():
    inject_css()
    st.markdown("""
    <div style="background-color: #f1f3f5; border-radius: 10px; padding: 15px 20px; margin-bottom: 25px;">
        <h2 style="color: #2c3e50; margin: 0;">Diamond Specifications</h2>
        <p style="color: #6c757d; margin: 5px 0 0 0;">
            Please enter all required details about your diamond
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Create form structure with clear sections
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<p class="section-title">Basic Attributes</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="input-label">Carat Weight</p>', unsafe_allow_html=True)
        carat = st.number_input('', min_value=0.001, max_value=10.0, value=1.0, step=0.01, 
                               key='carat_input', label_visibility="collapsed")
        st.markdown('<p class="input-description">Weight of the diamond in carats (1 carat = 0.2 grams)</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="input-label">Cut Quality</p>', unsafe_allow_html=True)
        cut = st.selectbox('', ('Fair', 'Good', 'Very Good', 'Premium', 'Ideal'),
                          key='cut_select', label_visibility="collapsed")
        st.markdown('<p class="input-description">Quality of the diamond cut (Ideal is best)</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="input-label">Color Grade</p>', unsafe_allow_html=True)
        color = st.selectbox('', ('D', 'E', 'F', 'G', 'H', 'I', 'J'),
                            key='color_select', label_visibility="collapsed")
        st.markdown('<p class="input-description">D (colorless) to J (light color)</p>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<p class="section-title">Quality Metrics</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="input-label">Clarity Grade</p>', unsafe_allow_html=True)
        clarity = st.selectbox('', ('IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'),
                             key='clarity_select', label_visibility="collapsed")
        st.markdown('<p class="input-description">IF (flawless) to I1 (visible inclusions)</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="input-label">Depth Percentage</p>', unsafe_allow_html=True)
        depth = st.number_input('', min_value=0.001, max_value=100.0, value=60.0, step=0.1,
                              key='depth_input', label_visibility="collapsed")
        st.markdown('<p class="input-description">Total depth percentage (depth/mean diameter)</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="input-label">Table Width</p>', unsafe_allow_html=True)
        table = st.number_input('', min_value=0.001, max_value=100.0, value=55.0, step=0.1,
                              key='table_input', label_visibility="collapsed")
        st.markdown('<p class="input-description">Width of diamond\'s table (top flat surface)</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="section-title">Dimensions (in millimeters)</p>', unsafe_allow_html=True)
    dim_col1, dim_col2, dim_col3 = st.columns(3)
    with dim_col1:
        st.markdown('<p class="input-label">Length (X)</p>', unsafe_allow_html=True)
        x = st.number_input('', min_value=0.001, value=5.0, step=0.01,
                           key='x_input', label_visibility="collapsed")
        st.markdown('<p class="input-description">Length dimension in mm</p>', unsafe_allow_html=True)
    with dim_col2:
        st.markdown('<p class="input-label">Width (Y)</p>', unsafe_allow_html=True)
        y = st.number_input('', min_value=0.001, value=5.0, step=0.01,
                           key='y_input', label_visibility="collapsed")
        st.markdown('<p class="input-description">Width dimension in mm</p>', unsafe_allow_html=True)
    with dim_col3:
        st.markdown('<p class="input-label">Depth (Z)</p>', unsafe_allow_html=True)
        z = st.number_input('', min_value=0.001, value=3.0, step=0.01,
                           key='z_input', label_visibility="collapsed")
        st.markdown('<p class="input-description">Depth dimension in mm</p>', unsafe_allow_html=True)
    
    # Predict button
    st.markdown("<div style='margin: 30px 0;'>", unsafe_allow_html=True)
    button = st.button("Predict Diamond Price", key="predict_button")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # If button is clicked
    if button:
        with st.spinner('Calculating value...'):
            result = predict(carat, cut, color, clarity, depth, table, x, y, z)
            st.success(f"The estimated value for this diamond is: **${result:,.2f}**")
