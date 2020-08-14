# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:20:15 2020

@author: Anku
"""

import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    int_feature=[int(x) for x in request.form.values()]
    final_feature=[np.array(int_feature)]
    prediction=model.predict(final_feature)
    
    output=round(prediction[0],2)
    
    return render_template('index.html',prediction_text='Employee salary should be $ {}'.format(output))

if __name__ == "__main__":
    app.run()