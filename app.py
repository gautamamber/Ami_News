from flask import Flask, render_template, request, session, url_for, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask("__name__")

app.config['MONGO_DBNAME'] = "aminews"
app.config['MONGO_URI'] =  "mongodb://amber:amber@ds125716.mlab.com:25716/aminews"
mongo = PyMongo(app)

@app.route('/')
def index():
	getdata =  mongo.db.users.find_one()
	if getdata > 0:
		return render_template("index.html" , getdata = getdata)
	else:
		msg = "nothing"
		return render_template("index.html" , getdata = getdata)


	
@app.route('/', methods = ['POST', 'GET'])
def subscription():
	try:

		if request.method == 'POST':
			users = mongo.db.users 
			users.insert({'Email' : request.form['email']})
		return render_template('index.html') 
	except:
		return "Something is wrong"


@app.route('/dashboard', methods = ['POST' ,'GET'])
def dashboard():
	try:
		if request.method == 'POST':
			data = mongo.db.data
			data.insert({'Title' : request.form['title'], 'Description' : request.form['description'], 'Link' : request.form['link']})
		return render_template("dashboard.html")
	except:
		return "something went wrong"

	
        
	return render_template('dashboard.html')
@app.route('/login', methods = ['POST' , 'GET'])
def login():
	if request.method == "POST":
		username = request.form['firstname']
		password = request.form['lastname']
		if username == "amber" and password == "gautam":
			return render_template("dashboard.html")
		else: 
			return render_template("login.html")
	
	return render_template("login.html")






if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run(debug = True)  
