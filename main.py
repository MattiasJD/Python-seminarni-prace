from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

meta = MetaData()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recept.db'
db = SQLAlchemy(app)


class Recept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazev = db.Column(db.String(60))
    text = db.Column(db.String(600))
    ingredience = db.Column(db.String(200))
    path = db.Column(db.String(200))

    def __repr__(self):
        return f'<User {self.name}>'


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/recepty')
def receptyy():
    recepty = Recept.query.all()
    return render_template('recepty.html', recepty=recepty)

@app.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete_product(id):
    product = Recept.query.get(id)
    if not product:
        return 'Recept nenalezen', 404
    db.session.delete(product)
    db.session.commit()
    return 'Recept uspesne smazan'


@app.route('/pridat_recept', methods=['GET', 'POST'])
def pridat_recept():
    if request.method == 'POST':
        nazev = request.form['nazev']
        text = request.form['text']
        path = request.files['path']
        filename = path.filename
        # path.save(f'templates/pictures/{filename}')
        path.save(f'./{filename}')
        ingredience = request.form['ingredience']
        recept = Recept(nazev=nazev, text=text, ingredience=ingredience,
                        # path=f'C:/Users/matyd/PycharmProjects/piton-seminarni-arbeit/{filename}')
                        path=f'../image/{filename}')
        db.session.add(recept)
        db.session.commit()
        return 'Recept uspesne pridan!'
    return render_template('pridat_recept.html')


@app.route('/image/<string:custom_url>')
def get_image(custom_url):
    filename = f'{custom_url}'
    return send_file(filename, mimetype='image/jpg')


if __name__ == '__main__':
    app.run(debug=True)
