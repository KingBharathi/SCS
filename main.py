from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__)


@app.route('/Home')
def hello():
    return 'Dear Students<br> <font color=red size=7>Python Flask Frameworks</font>'


@app.route('/Db')
def database():
    con = sqlite3.connect("database.db")
    con.execute('CREATE TABLE if not exists students (reg TEXT, name TEXT, city TEXT)')
    con.execute("insert into students values('1001','Ananthan','Cuddalore')")
    con.execute("insert into students values('1002','Sara','Kumbakonam')")
    con.execute("insert into students values('1003','Shiva','Pondicherry')")
    con.commit()
    con.close()
    return 'Database Created'


@app.route('/')
def Student():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute('select * from students')
    rs = cur.fetchall()
    con.close()
    return render_template("Students.html", data=rs)


@app.route('/StudentSave', methods=['GET', 'POST'])
def studentSave():
    a = request.form.get("reg")
    b = request.form.get("sname")
    c = request.form.get("city")
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("insert into students values('"+a+"','"+b+"','"+c+"')")
    con.commit()
    con.close()
    return redirect(url_for('Student'))


@app.route('/StudentEntry')
def studentEntry():
    return render_template("StudentEntry.html")


if __name__ == '__main__':
    app.run(host='172.15.2.6')


