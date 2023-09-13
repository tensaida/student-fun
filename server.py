from flask import Flask, jsonify
import random

app = Flask(__name__)

def read_student_names(file_path):
    with open(file_path, 'r') as file:
        student_names = file.read().splitlines()
    return student_names

student_names_file = 'students.txt'
student_names = read_student_names(student_names_file)

@app.route("/random_student", methods=['GET'])
def random_student():
    selected_student = random.choice(student_names)
    response = {
        'message': 'Random student selected',
        'student_name': selected_student
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)