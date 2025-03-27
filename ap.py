from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sponsorship.db"
app.config["JWT_SECRET_KEY"] = "your_secret_key"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

# Database Models
class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    guardian_name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(50), nullable=False)
    needs = db.Column(db.Text, nullable=True)

class Sponsor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Matching(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsor.id'), nullable=False)

# Routes
@app.route('/register_child', methods=['POST'])
def register_child():
    data = request.json
    new_child = Child(
        name=data["name"],
        age=data["age"],
        guardian_name=data["guardian_name"],
        contact=data["contact"],
        needs=data.get("needs", "")
    )
    db.session.add(new_child)
    db.session.commit()
    return jsonify({"message": "Child registered successfully!"})

@app.route('/get_children', methods=['GET'])
def get_children():
    children = Child.query.all()
    return jsonify([{"id": c.id, "name": c.name, "age": c.age, "guardian": c.guardian_name} for c in children])

@app.route('/match_child/<int:child_id>/<int:sponsor_id>', methods=['POST'])
def match_child(child_id, sponsor_id):
    match = Matching(child_id=child_id, sponsor_id=sponsor_id)
    db.session.add(match)
    db.session.commit()
    return jsonify({"message": "Child matched successfully!"})

@app.route('/get_matched_children', methods=['GET'])
def get_matched_children():
    matches = Matching.query.all()
    return jsonify([
        {"child_id": m.child_id, "sponsor_id": m.sponsor_id}
        for m in matches
    ])

# Run Flask App
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
