from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(200)) 
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Note {self.title}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notes', methods=['GET', 'POST'])
def programmer_diary():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        subtitle = request.form.get('subtitle')


        if title and content:
            new_note = Notes(title=title, content=content, subtitle=subtitle)
            try:
                db.session.add(new_note)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(f"Ошибка при сохранении в БД: {e}")
                return "Ошибка при сохранении записи", 500
        return redirect(url_for('programmer_diary'))


    notes = Notes.query.order_by(Notes.date.desc()).all()
    return render_template('notes.html', notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
