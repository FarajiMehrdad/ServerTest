from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base , Session
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


engine = create_engine('mysql://root:123456@localhost/EmpData?charset=utf8&use_unicode=0', pool_recycle=3600)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
 
@app.route("/")
def hello():
    sans = session.query(Session)
    #return  sans.gender
    return render_template("index.html" , items = sans)



@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    print("hello")
    cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"



@app.route("/footsalon")
def footsalon():

    return render_template("index.html")

 
if __name__ == "__main__":
	#Authenticate() 
    app.run(debug=True)

