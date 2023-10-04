from flask import Flask, jsonify
import random

app = Flask(__name__)

def read_student_names(file_path):
    with open(file_path, 'r') as file:
        student_names = file.read().splitlines()
    return student_names

student_names_file = 'students_myclass.txt'
student_names = read_student_names(student_names_file)
random.shuffle(student_names)
i = 0

@app.route("/random_student", methods=['GET'])
def random_student():
    global i
    if i >= len(student_names):
        i = 0
    response = jsonify({
        'message': 'Random student selected',
        'student_name': student_names[i]
    })
    i += 1
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)