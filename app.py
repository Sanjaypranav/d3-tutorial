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

# @app.route("/nandhini")
# def nandhini():
#     return "Hello, World!"

# @app.route('/test')
# def test():
#     return render_template('displaytable.html')

@app.route('/api/getData', methods=['GET'])
def get_data():
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM mytable")
        data = cur.fetchall()
        column_names = [desc[0] for desc in cur.description]  # Get column names
        
        data_with_columns = {"columns": column_names, "data": data}
        print(data_with_columns)
        return jsonify(data_with_columns)
        # df = pd.DataFrame(data, columns=[
        #     "fixed acidity",
        #     "volatile acidity",
        #     "citric acid",
        #     "residual sugar",
        #     "chlorides",
        #     "free sulfur dioxide",
        #     "total sulfur dioxide",
        #     "density",
        #     "pH",
        #     "sulphates",
        #     "alcohol",
        #     "quality"
        # ])
        # df.to_csv('data.csv', index=False)
        # return jsonify(df.to_dict(orient='records'))
        # cur.close()
        # conn.close()
        # return jsonify(data)
    
        
    except Exception as e:
        return str(e), 500

# uvicorn app:app --reload
if __name__ == '__main__':
    app.run(debug=True)