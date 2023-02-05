from flask import request, jsonify
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required
from models.model import Match
from models.exts import db


match_ns = Namespace('match', description='namespaces match ')

'''
id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_match = db.Column(db.String(100), nullable=False)
    categorie_match = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    heure = db.Column(db.String(100), nullable=False)

'''

# model (serializer)
match_model = match_ns.model(
    "Match",
    {
        "id": fields.Integer(),
        "numero_match": fields.String(),
        "username": fields.String(),
        "categorie_match": fields.String(),
        "equipe1": fields.String(),
        "equipe2": fields.String(),
        "resultat": fields.String(),
    }
)


@match_ns.route("/matchs/<string:categorie_match>")
class matchsByCategoryRessource(Resource):

    @match_ns.marshal_list_with(match_model)
    @jwt_required()
    def get(self, categorie_match):
        print(categorie_match)
        '''Get all matches in categorie_match'''
        matches = Match.query.filter_by(
            categorie_match=categorie_match, username='admin').all()

        return matches


@match_ns.route("/matchs")
class matchsRessource(Resource):

    @match_ns.marshal_list_with(match_model)
    @jwt_required()
    def get(self):
        '''Get all '''
        matchs = Match.query.all()

        return matchs

    @match_ns.marshal_with(match_model)
    @match_ns.expect(match_model)
    @jwt_required()
    def post(self):
        '''Create new Category'''
        data = request.get_json()
        new_match = Match(
            numero_match=data.get('numero_match'),
            username=data.get('username'),
            categorie_match=data.get('categorie_match'),
            equipe1=data.get('equipe1'),
            equipe2=data.get('equipe2'),
            resultat=data.get('resultat')
        )
        new_match.save()
        return new_match, 201


@match_ns.route("/match/<int:id>")
class matchsRessource(Resource):

    @match_ns.marshal_with(match_model)
    @jwt_required()
    def get(self, id):
        ''' Get by id '''
        match = Match.query.get_or_404(id)
        return match

    @match_ns.marshal_with(match_model)
    @jwt_required()
    def put(self, id):
        '''update category'''

        match_to_update = Match.query.get_or_404(id)
        data = request.get_json()

        match_to_update.update(

            username=data.get('username'),
            categorie_match=data.get('categorie_match'),
            equipe1=data.get('equipe1'),
            equipe2=data.get('equipe2'),
            resultat=data.get('resultat')
        )

        return match_to_update

    @match_ns.marshal_with(match_model)
    @jwt_required()
    def delete(self, id):
        '''delete match'''
        category_to_delete = Match.query.get_or_404(id)
        category_to_delete.delete()
        return category_to_delete
