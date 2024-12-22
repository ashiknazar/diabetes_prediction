import pickle

from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline


app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_datapoint',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data= CustomData(
            Pregnancies=request.form.get('Pregnancies'),
            Glucose=request.form.get('Glucose'),
            BloodPressure=request.form.get('BloodPressure'),
            SkinThickness=request.form.get('SkinThickness'),
            Insulin=request.form.get('Insulin'),
            BMI=request.form.get('BMI'),
            DiabetesPedigreeFunction=request.form.get('DiabetesPedigreeFunction'),
            Age=request.form.get('Age'),
        )
        pred_df=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        prediction=predict_pipeline.predict(pred_df)
        return render_template('home.html',prediction=prediction)
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
