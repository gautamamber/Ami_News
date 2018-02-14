from flask import Flask, render_template, request, session, url_for, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask("__name__")

app.config['MONGO_DBNAME'] = "aminews"
app.config['MONGO_URI'] =  "mongodb://amber:amber@ds125716.mlab.com:25716/aminews"
mongo = PyMongo(app)

@app.route('/')
def index():
	if 'username' in session:
		return "you are logged in as" + session['username']
	return render_template('login.html')
@app.route('/', methods = ['POST', 'GET'])
def subscription():
	try:

		if request.method == 'POST':
			users = mongo.db.users 
			users.insert({'Email' : request.form['email']})
		return render_template('index.html') 
	except:
		return "Something is wrong"

@app.route('/dashboard')
def dashboard():
	
        
	return render_template('dashboard.html')




if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run(debug = True)  
