from pages import home, predict
import streamlit as st

def main():
    st.sidebar.title("Navigation")
    menu = ["Home", "Price Prediction"]
    choice = st.sidebar.selectbox("Go to", menu)

    if choice == "Home":
        home.show()
    elif choice == "Price Prediction":
        predict.show()

if __name__ == "__main__":
    main()
