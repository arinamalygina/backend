from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    text = data.get('text', '')
    
    with open('data.txt', 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    
    return jsonify({'status': 'success', 'message': 'Данные сохранены'})

@app.route('/read', methods=['GET'])
def read_data():
    if not os.path.exists('data.txt'):
        return jsonify({'content': 'Файл пуст'})
    
    with open('data.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    return jsonify({'content': content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)