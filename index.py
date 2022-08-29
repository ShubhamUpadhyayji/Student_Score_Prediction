import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from PIL import Image


st.write("""
# Simple Marks Prediction App
This app predicts the **Marks** scored by the student!
""")

image=Image.open("college.png")
st.image(image,use_column_width=True)

st.sidebar.markdown('''
            By Shubham Upadhyay [SoleCodr](https://github.com/Shubham12356789) \n
            GitHub Repo for the [App](https://github.com/Shubham12356789/Student_SC_Prediction/blob/main/index.py)
    ''')

st.dataframe(data)

st.dataframe(s_data)


st.write('''
        **Assuming the study hours to be maximum 10 hours.**
        ''')
    

def user_input():
    hr = st.number_input("Number of Hours of Study",0.00,10.00,6.2)
    hr = np.array([[hr]]).astype(np.float64)
    return hr

pred = user_input()

#Loading dataset
df = pd.read_csv("https://raw.githubusercontent.com/SoleCodr/Prediction-of-Marks-scored-by-student/master/Data.txt?token=AGEY7MBIGAHSIIG6U7BN7ES7FWEOO")

attr = df.iloc[:,:-1].values
labels = df.iloc[:,1].values

LR = LinearRegression()
LR.fit(attr,labels)

prediction = round(float(LR.predict(pred)),2)

if pred > 9.97:
    st.button("Predict")
    st.success("The Predicted Percentage is 100.00")
else:
    st.button("Predict")
    st.success("The Predicted Percentage is {}".format(prediction))
 
 
