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

    def __repr__(self):
        return f"<Category {self.title} >"

    def save(self):
        db.session.add(self)
        db.session.commit()


'''
Create match 
'''


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_match = db.Column(db.String(100), nullable=False)
    categorie_match = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    heure = db.Column(db.String(100), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):

        db.session.delete(self)
        db.session.commit()

    def update(self, numero_match, categorie_match, description, date, heure):
        self.numero_match = numero_match
        self.categorie_match = categorie_match
        self.description = description
        self.date = date
        self.heure = heure

        db.session.commit()


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_match = db.Column(db.String(100), default='N/A', nullable=False)
    username = db.Column(db.String(100), nullable=False)
    categorie_match = db.Column(db.String(100), nullable=False)
    equipe1 = db.Column(db.String(100), nullable=False)
    equipe2 = db.Column(db.String(100), nullable=False)
    resultat = db.Column(db.String(100), nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):

        db.session.delete(self)
        db.session.commit()

    def update(self, categorie_match, equipe1, equipe2, resultat, numero_match):

        self.categorie_match = categorie_match
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.resultat = resultat
        self.numero_match = numero_match
        db.session.commit()


class MesGrid(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_match = db.Column(db.String(100), default='N/A', nullable=True)
    username = db.Column(db.String(100), nullable=False)
    categorie_match = db.Column(db.String(100), nullable=False)
    equipe1 = db.Column(db.String(100), nullable=False)
    equipe2 = db.Column(db.String(100), nullable=False)
    resultat = db.Column(db.String(100), nullable=True)
    etat = db.Column(db.String(100), nullable=True)
    date_fin = db.Column(db.String(100), nullable=True)
    correct_resultat = db.Column(db.String(100), nullable=True)
    numero_grid = db.Column(db.Integer, nullable=True, default=0)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):

        db.session.delete(self)
        db.session.commit()

    def update(self, categorie_match, equipe1, equipe2, resultat, numero_match):

        self.categorie_match = categorie_match
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.resultat = resultat
        self.numero_match = numero_match

        db.session.commit()


class Scores(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String(100), nullable=True)
    scores = db.Column(db.Integer, default=0, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):

        db.session.delete(self)
        db.session.commit()

    def update(self, scores):

        self.scores = scores

        db.session.commit()

class Coupons(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String(100), nullable=True)
    coupons = db.Column(db.String(100), nullable=False)
    nombre_de_pieces = db.Column(db.Integer, default=10, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):

        db.session.delete(self)
        db.session.commit()

    def update(self, coupons,nombre_de_pieces):

        self.coupons = coupons
        self.nombre_de_pieces = nombre_de_pieces

        db.session.commit()
