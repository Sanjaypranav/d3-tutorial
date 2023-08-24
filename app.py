from flask import Flask, render_template, jsonify
import psycopg2
import numpy as np
import pandas as pd

app = Flask(__name__)

# Replace these with your actual database credentials
db_params = {
    'host': 'localhost',
    'database': 'mydb',
    'user': 'postgres',
    'password': '2509',
    'port': 5432,
}

@app.route('/')
def index():
    return render_template('displaypostgressql.html')

@app.route('/api/getData', methods=['GET'])
def get_data():
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM mytable")
        data = cur.fetchall()
        df = pd.DataFrame(data)
        # return jsonify(df.to_dict(orient='records'))
        
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
