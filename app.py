from flask import Flask,request
import sqlite3

app=Flask(__name__)

con=sqlite3.connect("db.db")
con.execute("CREATE TABLE IF NOT EXISTS favs (id INTEGER PRIMARY KEY AUTOINCREMENT,bid INTEGER)")
con.commit()
con.close()

@app.route("/data")
def dg():
    con=sqlite3.connect("db.db")
    cur=con.cursor()
    cur.execute("SELECT bid FROM favs")
    a=cur.fetchall()
    con.close()

    return(a)

@app.route("/data",methods=['POST'])
def dp():
    # print(request.form.get())
    json=request.json
    list=json["list"]
    con=sqlite3.connect("db.db")
    cur=con.cursor()
    for v in list:
        print(type(v))
        cur.execute(f"INSERT INTO favs (bid) VALUES ('{v}')")
        con.commit()
    con.close()
    return "INSERTED"

@app.route("/del",methods=['POST'])
def dele():
    json=request.json
    ele=json["ele"]
    con=sqlite3.connect("db.db")
    cur=con.cursor()
    cur.execute(f"DELETE FROM favs WHERE bid={ele} ")
    return "DELETED"

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if(__name__=="__main__"):
    app.run(debug=True)