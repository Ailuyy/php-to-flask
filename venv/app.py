from flask import Flask, render_template, request
from multiplication_table import generate_table

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    table = None
    if request.method == 'POST':
        x = int(request.form['x'])
        color1 = request.form['color1']
        color2 = request.form['color2']
        table = generate_table(x, color1, color2)
    return render_template('form.html', table=table)

if __name__ == '__main__':
    app.run(debug=True)