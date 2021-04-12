import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def census_income_authentication(age, education_num, marital_status, occupation, relationship, capital_gain, hours_per_week):
    if marital_status == 'Divorced':
        marital_status = 0
    elif marital_status == 'Married-AF-spouse':
        marital_status = 1
    elif marital_status == 'Married-civ-spouse':
        marital_status = 2
    elif marital_status == 'Married-spouse-absent':
        marital_status = 3
    elif marital_status == 'Never-married':
        marital_status = 4
    elif marital_status == 'Separated':
        marital_status = 5
    elif marital_status == 'Widowed':
        marital_status = 6
        
    if occupation == 'Adm-clerical':
        occupation = 0
    elif occupation == 'Armed-Forces':
        occupation = 1
    elif occupation == 'Craft-repair':
        occupation = 2
    elif occupation == 'Exec-managerial':
        occupation = 3
    elif occupation == 'Farming-fishing':
        occupation = 4
    elif occupation == 'Handlers-cleaners':
        occupation = 5
    elif occupation == 'Machine-op-inspct':
        occupation = 6
    elif occupation == 'Other-service':
        occupation = 7
    elif occupation == 'Priv-house-serv':
        occupation = 8
    elif occupation == 'Prof-specialty':
        occupation = 9
    elif occupation == 'Protective-serv':
        occupation = 10
    elif occupation == 'Sales':
        occupation = 11
    elif occupation == 'Tech-support':
        occupation = 12
    elif occupation == 'Transport-moving':
        occupation = 13
    
    if relationship == 'Husband':
        relationship = 0
    elif relationship == 'Not-in-family':
        relationship = 1
    elif relationship == 'Other-relative':
        relationship = 2
    elif relationship == 'Own-child':
        relationship = 3
    elif relationship == 'Unmarried':
        relationship = 4
    elif relationship == 'Wife':
        relationship = 5
        
    prediction=classifier.predict([[age, education_num, marital_status, occupation, relationship, capital_gain, hours_per_week]])
    print(prediction)
    if prediction == 0:
        pred = 'Income is <=50K'
    else:
        pred = 'Income is >50K'
    return pred
    


def main():
    st.title("Census Income Prediction")
    html_temp = """
    <div style="background-color:white;padding:10px">
    <h2 style="color:black;text-align:center;">Census Income Prediction ML App </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("Age","Type Here")
    education_num = st.text_input("Education_num","Min. 1 to Max. 16")
    marital_status = st.selectbox('Marital_Status',("Married-civ-spouse", "Never-married", "Divorced", "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse")) 
    occupation = st.selectbox('Occupation',("Prof-specialty", "Craft-repair", "Exec-managerial", "Adm-clerical", "Sales", "Other-service", "Machine-op-inspct", "Transport-moving", "Handlers-cleaners", "Farming-fishing", "Tech-support", "Protective-serv", "Priv-house-serv", "Armed-Forces")) 
    relationship = st.selectbox("Relationship",("Husband", "Not-in-family", "Own-child", "Unmarried", "Wife", "Other-relative"))
    capital_gain = st.text_input("Capital_gain","Type Here")
    hours_per_week = st.text_input("Hours_per_week","Type Here")
    result=""
    if st.button("Predict"):
        result = census_income_authentication(age, education_num, marital_status, occupation, relationship,capital_gain, hours_per_week)
    st.success('The output is {}'.format(result))
    if st.button("Contributors"):
        st.success('1. Shubhanshu Arya')
        st.success('2. Anubhav Ranjan')
        st.success('3. Ankush Kunwar')
        st.success('4. Hitesh Raghuwanshi')

        

if __name__=='__main__':
    main()