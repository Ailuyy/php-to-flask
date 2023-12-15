from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

@app.route('/')
def index():
    global show_cars
    show_cars = True
    conn = database.create_conn()
    cars = database.show_cars(conn)
    return render_template('form.html', route='/', show_cars = show_cars, cars=cars)

@app.route('/ukryj_samochody', methods=['GET'])
def hide_cars():
    global show_cars
    show_cars = False
    return render_template('form.html', route='/', show_cars=show_cars)

@app.route('/dodaj_samochod', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        year = request.form['year']
        engine_capacity = request.form['engine_capacity'].replace(',', '.')
        mileage = request.form['mileage']
        horsepower = request.form['horsepower']
        color = request.form['color']
        body_type = request.form['body_type']

        conn = database.create_conn()
        database.insert_data(conn, brand, model, year, engine_capacity, mileage, horsepower, color, body_type)
        return redirect('/')
    return render_template('form.html', route='dodaj_samochod')

@app.route('/usun_samochod', methods=['GET', 'POST'])
def delete_car():
    if request.method == 'POST':
        car_to_delete = request.form.get('car_to_delete')
        if car_to_delete:
            conn = database.create_conn()
            database.delete_data(conn, car_to_delete)
        return redirect('/')
    else:
        conn = database.create_conn()
        cars = database.show_cars(conn)
        return render_template('form.html', route='usun_samochod', cars=cars)

@app.route('/modyfikuj_samochod', methods=['GET', 'POST'])
def update_car():
    if request.method == 'POST':
        car_to_update = request.form.get('car_to_update')
        if car_to_update:
            conn = database.create_conn()
            car = database.get_car_details(conn, car_to_update)

            brand = request.form['brand'] if request.form['brand'] else car[1]
            model = request.form['model'] if request.form['model'] else car[2]
            year = request.form['year'] if request.form['year'] else car[3]
            engine_capacity = request.form['engine_capacity'].replace(',', '.') if request.form['engine_capacity'] else car[4]
            mileage = request.form['mileage'] if request.form['mileage'] else car[5]
            horsepower = request.form['horsepower'] if request.form['horsepower'] else car[6]
            color = request.form['color'] if request.form['color'] else car[7]
            body_type = request.form['body_type'] if request.form['body_type'] else car[8]

            database.update_data(conn, car_to_update, brand, model, year, engine_capacity, mileage, horsepower, color, body_type)
        return redirect('/')
    else:
            conn = database.create_conn()
            cars = database.show_cars(conn)
            return render_template('form.html', route='modyfikuj_samochod', cars=cars)

if __name__ == '__main__':
    conn = database.create_conn()
    database.create_table(conn)
    app.run(debug=True)