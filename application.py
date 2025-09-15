import pickle
from flask import Flask,request,render_template,url_for,redirect
import numpy as np
import pandas as pd

application = Flask(__name__)
app=application

gnb_model=pickle.load(open('models/gnb.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/sucessif/<name>/<score>')
def successif(name,score):
    return render_template('result.html', name=name, score=score)

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
        name=request.form.get('name')
        IQ = int(request.form.get('IQ'))
        CGPA = float(request.form.get('CGPA'))
        Academic_Performance = int(request.form.get('Academic_Performance'))
        Internship_Experience = int(request.form.get('Internship_Experience'))
        Extra_Curricular_Score = int(request.form.get('Extra_Curricular_Score'))
        Communication_Skills = int(request.form.get('Communication_Skills'))
        Projects_Completed = int(request.form.get('Projects_Completed'))

        new_data = np.array([[IQ,CGPA,Academic_Performance,Internship_Experience,Extra_Curricular_Score,Communication_Skills,Projects_Completed]])
        result=gnb_model.predict(new_data)
    
    else:
        return render_template('home.html')
    return redirect(url_for('successif', name=name, score=(result[0])))


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)