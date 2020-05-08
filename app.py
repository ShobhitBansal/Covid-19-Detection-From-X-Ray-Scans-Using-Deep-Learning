import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

from flask import Flask, render_template, redirect, request
import PredictDisease as PD

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/', methods= ['POST'])
def disease():
	if request.method == 'POST':

		f = request.files['userfile']
		path = "./static/image.jpg"
		f.save(path)

		prediction = PD.predictdisease(path)
		print(prediction)

		result_dic = {
		'image' : path,
		'prediction' : prediction
		}

		return render_template("index.html", result = result_dic)


if __name__ == '__main__':
	app.run(threaded = False)