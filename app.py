from flask import Flask, render_template, request, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = '1234567'

dbClient = MongoClient('mongodb+srv://revathi__1822:revathi@cluster0.hm79x.mongodb.net/')
db = dbClient['chatbotdb']
dbcol = db['chatbotcol']


@app.route('/')
def log():
    return render_template('Login.html')

@app.route('/reg',methods=['POST'])
def register():
    email=request.form['email']
    password=request.form['password']
    existing_user=dbcol.find_one({'email':email})
    if existing_user is None:
        dbcol.insert_one({'email':email, 'password':password})
        return render_template('Login.html',msg='Account created succesfully')
    else:
        session['email']=email
        return render_template('Login.html',msg='Login Successfully')


if __name__ == '__main__':
    app.run(debug=True, port=2002,host='0.0.0.0')
