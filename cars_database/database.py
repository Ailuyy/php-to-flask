import sqlite3
from sqlite3 import Error

def create_conn():
    conn = None;
    try:
        conn = sqlite3.connect('cars.db')
        return conn
    except Error as e:
        print(e)

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='cars' ''')
        exists = cursor.fetchone()[0]

        if not exists:
            cursor.execute('''CREATE TABLE cars
                   (id_car INTEGER PRIMARY KEY,
                   brand TEXT,
                   model TEXT,
                   year INTEGER CHECK (year BETWEEN 1900 AND 2023),
                   engine_capacity REAL CHECK (engine_capacity >= 0), 
                   car_mileage INTEGER CHECK (car_mileage >= 0),
                   horsepower INTEGER CHECK (horsepower >= 0),
                   color TEXT,
                   body_type TEXT
                   )''')
            conn.commit()
            conn.close()
            print('Table created successfully')
        else:
            print('Table already exists')
    except Error as e:
        print(e)

def insert_data(conn, brand, model, year, engine_capacity, car_mileage, horsepower, color, body_type):
    try:
        conn.cursor().execute('''INSERT INTO cars (brand, model, year, engine_capacity, 
        car_mileage, horsepower, color, body_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                              (brand, model, year, engine_capacity, car_mileage, horsepower, color, body_type))
        conn.commit()
        conn.close()
        print('Data inserted successfully')
    except Error as e:
        print(e)

def update_data(conn, id_car, brand, model, year, engine_capacity, car_mileage, horsepower, color, body_type):
    try:
        conn.cursor().execute('''UPDATE cars SET brand=?, model=?, year=?, engine_capacity=?, 
        car_mileage=?, horsepower=?, color=?, body_type=? WHERE id_car=?''', (brand, model, year, engine_capacity, car_mileage, horsepower, color, body_type, id_car))
        conn.commit()
        conn.close()
        print('Data updated successfully')
    except Error as e:
        print(e)

def delete_data(conn, id_car):
    try:
        conn.cursor().execute('''DELETE FROM cars WHERE id_car=?''', id_car)
        conn.commit()
        conn.close()
        print('Data deleted successfully')
    except Error as e:
        print(e)

def show_cars(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM cars''')
        cars = cursor.fetchall()
        conn.close()
        return cars
    except Error as e:
        print(e)

def get_car_details(conn, id_car):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM cars WHERE id_car=?''', id_car)
        car = cursor.fetchone()
        return car
    except Error as e:
        print(e)
