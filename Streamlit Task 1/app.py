import streamlit as st
import tensorflow as tf
import pickle
#Load ML model
filename = 'DecisionTree_Model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


with st.form("my_form"):
   st.write("Dicision Tree Application")
   s1 = st.number_input("Percentage")
   # Every form must have a submit button.
   submitted = st.form_submit_button("Predict Grade")

   if submitted:
       y_pred = loaded_model.predict([[s1]])
       st.write("Predicted Grade:",y_pred)