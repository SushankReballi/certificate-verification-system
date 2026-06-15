@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    cert_id = data['certificate_id']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM certificates WHERE certificate_id=?", (cert_id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return {"status": "valid"}
    else:
        return {"status": "invalid"}
