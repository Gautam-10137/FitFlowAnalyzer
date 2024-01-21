from flask import Flask,request, jsonify

from src.pipeline.predict_pipeline import CustomData,PredictPipeline
from src.exception import CustomException
import os
import sys
app=Flask(__name__)

@app.route("/predict",methods=["GET"])
def get_sleep_disorder():
    try:
       
        data=CustomData(
            Gender=request.form.get('Gender'),
            Age=int(request.form.get('Age')),
            Occupation=request.form.get('Occupation'),
            Sleep_Duration=float(request.form.get('Sleep_Duration')),
            Quality_of_Sleep=int(request.form.get('Quality_of_Sleep')),
            Physical_Activity_Level=int(request.form.get('Physical_Activity_Level')),
            Stress_Level=int(request.form.get('Stress_Level')),
            BMI_Category=request.form.get('BMI_Category'),
            Blood_Pressure=request.form.get('Blood_Pressure'),
            Heart_Rate=int(request.form.get('Heart_Rate')),
            Daily_Steps=int(request.form.get('Daily_Steps'))
        )
        data_df=data.get_data_as_data_frame()
        predict_pipeline=PredictPipeline()
        result=predict_pipeline.predict(data_df)
      
        result=int(result)
        return jsonify({"sleep_disorder":result})

    except Exception as e:
        raise CustomException(e,sys)

if __name__=="__main__":
    port = 5000
    app.run(host="0.0.0.0", port=port,debug=True)


