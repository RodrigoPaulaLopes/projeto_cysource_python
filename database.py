from flask_sqlalchemy import SQLAlchemy


def createDatabase(app):
    return SQLAlchemy(app)

def createModelUser(db):
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100))
        last_name = db.Column(db.String(100))
        date_born = db.Column(db.String(100))
        cpf = db.Column(db.String(100))
        rg = db.Column(db.String(100))
        phone = db.Column(db.String(100))
        email = db.Column(db.String(100))

        def __str__(self):
            return f"id: {self.id}, name: {self.name}, last_name: {self.last_name}, date_born: {self.date_born}, cpf: {self.cpf}, rg: {self.rg}, phone: {self.phone}, email: {self.email}"
    return User