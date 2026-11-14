from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Хранилище записей: { "Заголовок": { "content": "Текст", "date": "Дата" } }
notes = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notes', methods=['GET', 'POST'])
def programmer_diary():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if title and content:
            # Сохраняем запись с датой создания
            notes[title] = {
                'content': content,
                'date': datetime.now().strftime('%d.%m.%Y %H:%M')
            }
        return redirect(url_for('programmer_diary'))
    
    return render_template('notes.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
