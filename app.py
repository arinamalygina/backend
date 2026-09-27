from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    text = data.get('text', '')
    
    with open('data.txt', 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    
    return jsonify({'status': 'success', 'message': 'Данные сохранены'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)