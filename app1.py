from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'  # SQLite Database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100))
    section = db.Column(db.String(10))
    subject = db.Column(db.String(50))
    marks = db.Column(db.Integer)
    result = db.Column(db.String(10))

# Route to fetch all students without any filter
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()  # Fetch all students from the database
    return render_template('students_table.html', students=students)

# Ensure the database and tables are created
def init_db():
    with app.app_context():
        db.create_all()  # Create tables if not already created

# Run the app and initialize the database
if __name__ == '__main__':
    init_db()  # Initialize the database before running the app
    app.run(debug=True)
