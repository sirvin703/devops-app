from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# Small change for webhook trigger test

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/myappdb'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120))

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created', 'id': user.id})

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [{'id': u.id, 'name': u.name, 'email': u.email} for u in users]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
