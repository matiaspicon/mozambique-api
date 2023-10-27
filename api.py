from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

db_path = "database.db"

@app.route('/sales', methods=['GET','POST'])
def guardar_y_recuperar_datos():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON format"}), 400

        user_id = data.get('user_id')
        barcode = data.get('barcode')
        invoice_number = data.get('invoice_number')
        supplier_id = data.get('supplier_id')
        n_units = data.get('n_units')

        if not all([user_id, barcode, invoice_number, supplier_id, n_units]):
            return jsonify({"error": "Missing required fields"}), 400

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO sales (user_id, barcode, invoice_number, supplier_id, n_units) VALUES (?, ?, ?, ?, ?)",
                    (user_id, barcode, invoice_number, supplier_id, n_units))

        conn.commit()
        conn.close()

        return jsonify({"message": "Data saved successfully"})
    
    elif request.method == 'GET':
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM sales")
        sales = cursor.fetchall()

        conn.close()

        return jsonify({"sales": sales})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
