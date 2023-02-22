from flask import request, jsonify
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required
from models.model import MesGrid
from models.model import Scores
from models.exts import db
from sqlalchemy import func

mesgrid_ns = Namespace('mesgrid', description='namespaces mesgrid ')

'''
id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_match = db.Column(db.String(100), nullable=False)
    categorie_match = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    heure = db.Column(db.String(100), nullable=False)

'''

# model (serializer)
mesgrid_model = mesgrid_ns.model(
    "MesGrid",
    {
        "id": fields.Integer(),
        "numero_match": fields.String(),
        "username": fields.String(),
        "categorie_match": fields.String(),
        "equipe1": fields.String(),
        "equipe2": fields.String(),
        "resultat": fields.String(),
        "etat": fields.String(),
        "date_fin": fields.String(),
        "correct_resultat": fields.String(),
        "numero_grid": fields.Integer()
    }
)


@mesgrid_ns.route("/mesgridDistinct/<string:username>")
class matchsByCategoryRessource(Resource):

    @mesgrid_ns.marshal_list_with(mesgrid_model)
    @jwt_required()
    def get(self, username):
        '''Get all matches in categorie_match'''
        mesgrid = db.session.query(MesGrid.numero_grid, MesGrid.categorie_match,
                                   MesGrid.numero_match, MesGrid.username).filter_by(username=username).distinct().all()

        return mesgrid

    @mesgrid_ns.marshal_list_with(mesgrid_model)
    @jwt_required()
    def post(self, username):
        '''Get all matches in categorie_match'''
        data = request.get_json()
        numero_match = data.get('numero_match')
        categorie_match = data.get('categorie_match')
        numero_grid = data.get('numero_grid')
        mesgrid = MesGrid.query.filter_by(
            username=username, numero_match=numero_match, categorie_match=categorie_match, numero_grid=numero_grid).all()

        return mesgrid


@mesgrid_ns.route("/getMesGrids")
class getMesGridsRessource(Resource):

    @mesgrid_ns.marshal_list_with(mesgrid_model)
    @jwt_required()
    def post(self):
        '''Get all matches in categorie_match'''
        data = request.get_json()
        numero_match = data.get('numero_match')
        categorie_match = data.get('categorie_match')
        numero_grid = data.get('numero_grid')
        username = data.get('username')
        mesgrid = MesGrid.query.filter_by(
            username=username, numero_match=numero_match, categorie_match=categorie_match, numero_grid=numero_grid).all()

        return mesgrid


@mesgrid_ns.route("/mesgrids")
class mesgridsRessource(Resource):

    @mesgrid_ns.marshal_list_with(mesgrid_model)
    @jwt_required()
    def get(self):
        '''Get all '''
        matchs = MesGrid.query.all()

        return matchs

    @mesgrid_ns.marshal_with(mesgrid_model)
    @mesgrid_ns.expect(mesgrid_model)
    @jwt_required()
    def post(self):
        '''Create new Category'''
        user = ''
        all_data = request.get_json()
        print(all_data)
        user = all_data[0].get('username')

        max_numero_grid = db.session.query(
            func.max(MesGrid.numero_grid)).filter_by(username=user).first()

        if(max_numero_grid[0] == None):
            max_numero_grid = 1
        else:
            max_numero_grid = max_numero_grid[0] + 1

        for data in all_data:
            new_mesgrid = MesGrid(
                numero_match=data.get('numero_match'),
                username=data.get('username'),
                categorie_match=data.get('categorie_match'),
                equipe1=data.get('equipe1'),
                equipe2=data.get('equipe2'),
                resultat=data.get('resultat'),
                etat=data.get('etat'),
                date_fin=data.get('date_fin'),
                correct_resultat=data.get('correct_resultat'),
                numero_grid=max_numero_grid
            )

            new_mesgrid.save()

        update_scores = Scores.query.filter_by(
            username=user).first_or_404()
        new_score = update_scores.scores + 1
        print(new_score)
        update_scores.scores = new_score
        db.session.commit()
        return new_mesgrid, 201


@mesgrid_ns.route("/mesgrid/<int:id>")
class mesgridRessource(Resource):

    @mesgrid_ns.marshal_with(mesgrid_model)
    @jwt_required()
    def get(self, id):
        ''' Get by id '''
        match = MesGrid.query.get_or_404(id)
        return match

    @mesgrid_ns.marshal_with(mesgrid_model)
    @jwt_required()
    def put(self, id):
        '''update category'''

        match_to_update = MesGrid.query.get_or_404(id)
        data = request.get_json()

        match_to_update.update(
            numero_match=data.get('numero_match'),
            username=data.get('username'),
            categorie_match=data.get('categorie_match'),
            equipe1=data.get('equipe1'),
            equipe2=data.get('equipe2'),
            resultat=data.get('resultat'),
            etat=data.get('etat'),
            date_fin=data.get('date_fin'),
            correct_resultat=data.get('correct_resultat'),
            numero_grid=data.get('numero_grid')
        )

        return match_to_update

    @mesgrid_ns.marshal_with(mesgrid_model)
    @jwt_required()
    def delete(self, id):
        '''delete match'''
        category_to_delete = MesGrid.query.get_or_404(id)
        category_to_delete.delete()
        return category_to_delete
