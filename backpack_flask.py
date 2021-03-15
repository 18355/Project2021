from flask import Flask,g,render_template,request,redirect,url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'backpack2021.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def home():
    cursor = get_db().cursor()
    sql = ("SELECT * FROM contents")
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)

@app.route('/add', methods=["GET","POST"])
def add():
    if request.method == "POST":
        cursor = get_db().cursor()
        new_name = request.form["item_name"]
        new_cost = request.form["item_cost"]
        new_description = request.form["item_description"]
        sql = ("INSERT INTO contents(name,cost,description) VALUES (?,?,?)")
        cursor.execute(sql,(new_name,new_cost,new_description))
        get_db().commit()
    return redirect('/')

@app.route('/delete', methods=["GET","POST"])
def delete():
    if request.method == "POST":
        cursor = get_db().cursor()
        id = int(request.form["item_name"])
        sql = ("DELETE FROM contents WHERE id=?")
        cursor.execute(sql,(id,))
        get_db().commit()
    return redirect('/')
        

if __name__ == "__main__":
    app.run(debug=True)






