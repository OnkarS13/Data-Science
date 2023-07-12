from flask import Flask,render_template,url_for,request
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
import joblib
import os

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
	df= pd.read_csv(r"C:/Users/asus/Desktop/Trainings/Python_class codes/Flask codes/Simple Linear Regression/Salary_Data/Salary_Data.csv")
	
	regressor = LinearRegression()
	regressor.fit(df.YearsExperience.values.reshape(30,1),df.Salary)

	if request.method == 'POST':
		Year_of_Experience = request.form['Year_of_Experience']
		pred = pd.DataFrame([Year_of_Experience])
		pred.columns=['YearsExperience']
		my_pred = regressor.predict(pred)
	return render_template('result.html',prediction=my_pred)



if __name__ == '__main__':
	app.run(debug=True,use_reloader=False)