from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = '/app/data.txt'

@app.route('/api/data', methods=['POST', 'GET'])
def handle_data():
    if request.method == 'POST':
        # Сохраняем данные
        data = request.json
        text = data.get('text', '')
        with open(DATA_FILE, 'a', encoding='utf-8') as f:
            f.write(text + '\n')
        return jsonify({'status': 'ok'})
    else:
        # Читаем данные
        if not os.path.exists(DATA_FILE):
            return jsonify({'content': ''})
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        return jsonify({'content': content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)