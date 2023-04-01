from flask import Flask, render_template,request, redirect, url_for
import mysql.connector
from pickle import load
import pandas as pd


app=Flask(__name__)

mydb=mysql.connector.connect(host='127.0.0.1',user='root',password='******',database='MLlogin')

@app.route('/',methods=['GET','POST'])
def main():
    if request.method == 'POST':
        name = request.form['username']
        passw = request.form['password']
        confirm_passw = request.form['confirm_password']

        if passw != confirm_passw:
            error = 'Passwords do not match. Please try again.'
            return render_template('signup.html', error=error)
        
        cur = mydb.cursor()
        query = "SELECT * FROM login_tbl WHERE usrname=%s"
        cur.execute(query, (name,))
        user = cur.fetchone()

        if user:
            error = 'Username already exists. Please try again with a different username.'
            return render_template('signup.html', error=error)
        query = "INSERT INTO login_tbl (usrname, passwrd) VALUES (%s, %s)"
        values = (name, passw)
        cur.execute(query, values)
        mydb.commit()
        return redirect('/login')
    
    return render_template('signup.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        usrnm=request.form['username']
        pwd=request.form['password']

        cur = mydb.cursor(dictionary=True)
        cur.execute("SELECT * FROM login_tbl where usrname = '"+ usrnm +"' and passwrd = '"+ pwd +"';")
        res = cur.fetchone()

        if res is None:
            return render_template('login.html',error='Invalid Username or Password')
        else:
            return redirect(url_for('success'))
    return render_template('login.html')
@app.route('/success', methods=['GET','POST'])
def success():
    

    sel_col=['cap-surface', 'bruises', 'odor', 'gill-attachment', 'gill-spacing',
       'gill-size', 'gill-color', 'stalk-shape', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'ring-number', 'spore-print-color',
       'habitat']    
    if request.method == 'POST':
        features = []
        for col in sel_col: 
            features.append(request.form[col])
        print(features)
        feat = pd.DataFrame([features], columns=sel_col)

        encoder=load(open('encoder.pkl','rb'))
        for col in sel_col:
            feat[col] = encoder[col].transform(feat[col])
            
        scaler = load(open('scaler.pkl', 'rb'))
        feat = scaler.transform(feat)
        feat = pd.DataFrame(feat,columns=sel_col)

        model = load(open('model.pkl', 'rb'))
        pred = model.predict(feat)          
        if pred==0:
            pr='Edible'
        else:
            pr='Inedible'
        
        return render_template('result.html', prediction=pr)

    return render_template('success.html')
    

if __name__=='__main__':
    app.run(debug=True)
