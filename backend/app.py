from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySQL Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/studentsystem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'studentsystem_db'

    student_id = db.Column(db.String(50), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(db.String(30))
    birthdate = db.Column(db.Date)
    address = db.Column(db.String(100))
    contact_number = db.Column(db.String(50))
    course_id = db.Column(db.String(50))
    course_name = db.Column(db.String(50))
    course_code = db.Column(db.String(50))
    enrollment_id = db.Column(db.String(50))

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "birthdate": str(self.birthdate),
            "address": self.address,
            "contact_number": self.contact_number,
            "course_id": self.course_id,
            "course_name": self.course_name,
            "course_code": self.course_code,
            "enrollment_id": self.enrollment_id
        }

# GET
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([s.to_dict() for s in students])

# ADD
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    student = Student(**data)

    db.session.add(student)
    db.session.commit()

    return jsonify({"message": "Student added successfully"})

# UPDATE
@app.route('/students/<string:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    data = request.get_json()

    for key, value in data.items():
        setattr(student, key, value)

    db.session.commit()

    return jsonify({"message": "Student updated successfully"})

# DELETE
@app.route('/students/<string:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
