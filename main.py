import mysql.connector
from flask import *
from flask_cors import CORS

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='sgdb'
)
db = mydb.cursor()


headers = {
  'Access-Control-Allow-Origin': '*'
}

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    db.execute("SELECT * FROM User WHERE mobile = %s AND password = %s", (data['mobile'], data['password']))
    user = db.fetchone()
    if user:
        return jsonify({"data":True, 'status': 200})
    else:
        return jsonify({'status': 404})
    
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    db.execute("SELECT * FROM User WHERE mobile = %s AND password = %s", (data['mobile'], data['password']))
    user = db.fetchone()
    if user:
        return jsonify({'status': 404, 'message':"User already exists"})
    db.execute("INSERT INTO User (email,LatLong, mobile, password) VALUES (%s,%s, %s, %s)",(data["email"],data['LatLong'], data['mobile'], data['password']))
    mydb.commit()
    return jsonify({'status': 200, 'message':"User registered successfully"})

@app.route('/iologin', methods=['POST'])
def iologin():
    data = request.get_json()
    db.execute("SELECT * FROM IO WHERE mobile = %s AND password = %s", (data['mobile'], data['password']))
    user = db.fetchone()
    if user:
        return jsonify({"data":True, 'status': 200})
    else:
        return jsonify({'status': 404})

@app.route('/addReport', methods=['POST'])
def addReport():
    data = request.get_json()
    db.execute("INSERT INTO Report (email,LatLong, mobile, password) VALUES (%s,%s, %s, %s)",(data["email"],data['LatLong'], data['mobile'], data['password']))
    mydb.commit()
    return jsonify({'status': 200, 'message':"Report added successfully"})

app.run(debug=True)