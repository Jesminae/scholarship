from flask import Flask, render_template, request, jsonify
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Path to JSON file
JSON_FILE = 'scholarships.json'

# Ensure JSON file exists
if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, 'w') as file:
        json.dump([], file)


@app.route('/')
def home():
    return render_template('officepage2.html')  # Default homepage


@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content


@app.route('/save', methods=['POST'])
def save_scholarship():
    data = request.json
    if not data.get('name') or not data.get('description'):
        return jsonify({'error': 'Name and Description are required.'}), 400

    with open(JSON_FILE, 'r') as file:
        scholarships = json.load(file)

    scholarships.append(data)
    
    if not os.path.exists(JSON_FILE) or os.stat(JSON_FILE).st_size == 0:
        with open(JSON_FILE, 'w') as file:
            json.dump([], file, indent=4)


    with open(JSON_FILE, 'w') as file:
        json.dump(scholarships, file, indent=4)

    return jsonify({'message': 'Scholarship saved successfully!'}), 200


@app.route('/scholarships', methods=['GET'])
def get_scholarships():
    """Retrieve all scholarships."""
    with open(JSON_FILE, 'r') as file:
        scholarships = json.load(file)
    return jsonify(scholarships), 200


@app.route('/addscholarship')
def add_scholarship_page():
    return render_template('addscholarship.html')

@app.route('/stuavailscholarship')
def student_scholarships():
    return render_template('stuavailscholarship.html')



@app.route('/offeditscholarship')
def offeditscholarship_page():
    
    return render_template('offeditscholarship.html')


if __name__ == '__main__':
    app.run(debug=True)
