import streamlit as st
import streamlit.components.v1 as stc

from ml_app import run_ml_app
from eda_app import run_eda_app

html_temp="""
            <div style="padding:10px; background-color:#3872fb; border-radius:10px;">
                <h1 style="color:white">Employee Promotion Prediction App</h1>
                <h4 style="color:white">This website belongs to HR Team | Copyright by @Kharisma 2024</h4>
            </div>        
        """

desc_temp = """
                ### Employee Promotion Prediction App
                This app is used by HR team to help predict wheter
                an employee get a promotion or not

                ### App Content
                - Exploratory Data Analysis
                - Machine Learning Section
            """
def main():
    stc.html(html_temp)

    menu = ["Home", "EDA", "ML Section"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "EDA":
        #Run EDA App
        run_eda_app()
    elif choice == "ML Section":
        #Run ML App
        run_ml_app()

if __name__ == '__main__':
    main()