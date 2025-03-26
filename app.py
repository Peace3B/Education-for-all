from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sponsorship.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = True
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
mail = Mail(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    needs = db.Column(db.String(255), nullable=False)
    guardian_email = db.Column(db.String(100), nullable=False)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsor.id'), nullable=True)
    progress_report = db.Column(db.Text, nullable=True)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Sponsor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    funding_capacity = db.Column(db.Integer, nullable=False)
    preferences = db.Column(db.String(255), nullable=True)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

@app.route('/dashboard/<int:sponsor_id>', methods=['GET'])
@jwt_required()
def sponsor_dashboard(sponsor_id):
    sponsored_children = Child.query.filter_by(sponsor_id=sponsor_id).all()
    children_data = [{"name": child.name, "age": child.age, "progress_report": child.progress_report} for child in sponsored_children]
    return jsonify({"sponsored_children": children_data})

@app.route('/update_progress', methods=['POST'])
@jwt_required()
def update_progress():
    data = request.json
    child = Child.query.get(data['child_id'])
    if not child:
        return jsonify({"message": "Child not found"}), 404
    child.progress_report = data['progress_report']
    db.session.commit()
    return jsonify({"message": "Progress report updated successfully"})

@app.route('/send_sms', methods=['POST'])
@jwt_required()
def send_sms():
    data = request.json
    # Placeholder for SMS sending logic
    return jsonify({"message": "SMS sent successfully to " + data['recipient']})

@app.route('/send_email', methods=['POST'])
@jwt_required()
def send_email():
    data = request.json
    msg = Message(data['subject'], sender='your_email@example.com', recipients=[data['recipient']])
    msg.body = data['message']
    mail.send(msg)
    return jsonify({"message": "Email sent successfully"})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
