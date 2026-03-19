from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Student Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    course = db.Column(db.String(100))
    year_level = db.Column(db.String(20))

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "year_level": self.year_level
        }

# Create database
@app.before_first_request
def create_tables():
    db.create_all()

# ------------------ API ROUTES ------------------

# ➤ Add Student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    new_student = Student(
        student_id=data['student_id'],
        name=data['name'],
        age=data.get('age'),
        course=data.get('course'),
        year_level=data.get('year_level')
    )

    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Student added successfully"}), 201


# ➤ Get All Students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([s.to_dict() for s in students])


# ➤ Get Single Student
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict())


# ➤ Update Student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()

    student.student_id = data.get('student_id', student.student_id)
    student.name = data.get('name', student.name)
    student.age = data.get('age', student.age)
    student.course = data.get('course', student.course)
    student.year_level = data.get('year_level', student.year_level)

    db.session.commit()

    return jsonify({"message": "Student updated successfully"})


# ➤ Delete Student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student deleted successfully"})


# Run Server
if _name_ == '_main_':
    app.run(debug=True)