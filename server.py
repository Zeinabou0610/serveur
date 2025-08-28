from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Import
import os

app = Flask(__name__)
CORS(app)  # ✅ Autorise toutes les origines

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Pas de fichier'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nom de fichier vide'}), 400
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return jsonify({'message': 'Upload réussi', 'file_path': filepath}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
