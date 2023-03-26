from flask import Flask, jsonify, request
from database import createDatabase, createModelUser
from helper import serializeUser
from flask_cors import CORS

app = Flask("__main__")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'

CORS(app, origins="*", methods=["POST", "GET", "PUT", "DELETE"])

db = createDatabase(app)
User = createModelUser(db)

@app.route("/drop", methods=["GET"])
def drop():
    db.drop_all()
    return "ok"

@app.route("/migrate", methods=["GET"])
def migrate():
    db.create_all()
    return "ok"


@app.route("/api/v1/users", methods=["GET"])
def all():
    try:
        if not request.args:
            users = User.query.all()
            user_list = []

            for user in users:
                print(user)

            for user in users:
                user_dict = serializeUser(user)
                user_list.append(user_dict)
            return jsonify(user_list)
        else:
            id = request.args["id"]
            user = User.query.filter_by(id=id).first()

            user = serializeUser(user)
            return jsonify(user)
    except Exception as e:
        return jsonify({"error": e})

@app.route("/api/v1/users", methods=["POST"])
def save():
    try:
        data = request.json
        user = User()

        user.name = data["name"]
        user.last_name = data["last_name"]
        user.date_born = data["date_born"]
        user.cpf = data["cpf"]
        user.rg = data["rg"]
        user.phone = data["phone"]
        user.email = data["email"]

        db.session.add(user)
        db.session.commit()


        return jsonify({"response": "data insert with success"})
    except Exception as e:
        return jsonify({"error": e})

@app.route("/api/v1/users/<id>", methods=["PUT"])
def update(id):

    try:
        user = User.query.filter_by(id=id).first()

        data = request.json

        user.name = data["name"]
        user.last_name = data["last_name"]
        user.date_born = data["date_born"]
        user.cpf = data["cpf"]
        user.rg = data["rg"]
        user.phone = data["phone"]
        user.email = data["email"]

        db.session.commit()

        return jsonify({"response": "user updated with success"})
    except Exception as e:
        return jsonify({"error": e})

@app.route("/api/v1/users/<id>", methods=["DELETE"])
def delete(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"response": "deleted with success"})
    except Exception as e:
        return jsonify({"error": e})

if __name__ == '__main__':

    app.run(debug=True)

