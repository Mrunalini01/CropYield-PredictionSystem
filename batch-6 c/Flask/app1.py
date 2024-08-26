# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 10:57:58 2021

@author: mruna
"""

import requests
from flask import Flask, render_template, request
import joblib
import pickle
clf = pickle.load(open('yield_modelpkgbr__.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        State_Name = float(request.form['State'])
        District = float(request.form['District'])
        
        Crop = float(request.form['Crop'])
        Season= float(request.form['Season'])
        Area= float(request.form['Area'])
        Rainfall= float(request.form['Rainfall'])
        Temperature= float(request.form['Temperature'])


        pred_args = [State_Name,District,Crop,Season,Area,Rainfall,Temperature]

        mul_reg = open('yield_modelpkgbr__.pkl','rb')
        ml_model = joblib.load(mul_reg)
        model_prediction = ml_model.predict([pred_args])
        #return res
    return render_template('result.html', prediction = model_prediction)

if __name__ == '__main__':
    app.run(debug=False)