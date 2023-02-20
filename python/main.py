import VALUES as VALUES
import sql as sql
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/ahoj<name>')
def kamil(name):
    return 'ahoj %s' %name

@app.route('/add_recipe')
def add_recipe():
    return ''

@app.route('/index' , methods = ['POST', 'GET'])
def write_recipes():
    if request.method == 'POST':
        try:
            name = request.form['name']
            author = request.form['author']
            text = request.form['text']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO students (name,author,text)
                VALUES(?, ?, ?, ?)",(nm,addr,city,pin) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()

if __name__ == '__main__':
        app.run(debug = True)