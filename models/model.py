from models.exts import db

'''
    create Recipie

'''


class Recipie(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"<Recipie {self.title} >"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, title, description):
        self.title = title
        self.description = description
        db.session.commit()


'''
Create users Model
'''


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self) -> str:
        return f"<username {self.username}"

    def save(self):
        db.session.add(self)
        db.session.commit()
