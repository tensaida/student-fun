from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)


def read_student_names(file_path):
    with open(file_path, 'r') as file:
        student_names = file.read().splitlines()
    return student_names

student_names_file = 'students.txt'
student_names = read_student_names(student_names_file)
i = 0

@app.route("/start_class", methods=['POST'])
def start_class():
    random.shuffle(student_names)
    global i
    i = 0
    response = jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/random_student", methods=['GET'])
def random_student():
    global i
    selected_student = student_names[i]
    i += 1
    response = jsonify({
        'message': 'Random student selected',
        'student_name': selected_student
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)