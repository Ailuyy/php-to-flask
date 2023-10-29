from flask import Flask, render_template, request
from multiplication_table import generate_table

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    x, color1, color2, table, with_border = None, None, None, '', False
    if request.method == 'POST':
        x = int(request.form['x'])
        color1 = request.form['color1']
        color2 = request.form['color2']
        with_border = request.form.get('ramka') == 'border'
        table = generate_table(x, color1, color2, with_border)
    return render_template('form.html', table=table, x=x, color1=color1, color2=color2, with_border=with_border)

if __name__ == '__main__':
    app.run(debug=True)