import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

#load model
with open('car_price_model.pkl','rb') as file:              #load
    model=pkl.load(file)
#Streamlit app UI
st.title("Car Price Prediction App")
st.markdown("Enter car specification to predict the price")

#Input fields for selected features
constant=st.selectbox("constant",[0,1])
carwidth=st.number_input("Car Width (inches)", min_value=50.0, max_value=80.0,value=65.0)
curbweight=st.number_input("Curb Weight (kg)",min_value=500.0, max_value=2000.0, value=1200.0)
enginesize=st.number_input("Engine Size (cc)",min_value=60.0, max_value=400.0, value=150.0)
borratio=st.number_input("Bore ratio", min_value=2.0, max_value=5.0, value=3.2)
rotor=st.selectbox("Has Rotor Brakes?",[0,1])
three=st.selectbox("Is three gear present ?",[0,1])
highend=st.selectbox("Is Highend Brand?",[0,1])
bmw=st.selectbox("Is BMW?",[0,1])
rear=st.selectbox("Rear Wheel Drive?",[0,1])

#Crete input Frame
input_data=pd.DataFrame({
    'const':[constant],
    'carwidth':[carwidth],
    'curbweight':[curbweight],
    'enginesize':[enginesize],
    'borratio':[borratio],
    'rotor':[rotor],
    'three':[three],
    'Highend':[highend],
    'bmw':[bmw],
    'rear':[rear]
})
#	const	carwidth	curbweight	enginesize	boreratio	rotor	three	Highend	bmw	rear
#Prediction
if st.button("Predict Price"):
    prediction=model.predict(input_data)
    st.success('car price is {}'.format(prediction))