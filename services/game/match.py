from flask import request, jsonify
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required
from models.model import Match
from models.exts import db


match_ns = Namespace('match', description='namespaces categorie match ')

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
        "username": fields.String(),
        "categorie_match": fields.String(),
        "equipe1": fields.String(),
        "equipe2": fields.String(),
        "resultat": fields.String(),
    }
)


@match_ns.route("/matchs")
class categoryRessource(Resource):

    @match_ns.marshal_list_with(match_model)
    @jwt_required()
    def get(self):
        '''Get all Category'''
        recipies = Match.query.all()
        return recipies

    @match_ns.marshal_with(match_model)
    @match_ns.expect(match_model)
    @jwt_required()
    def post(self):
        '''Create new Category'''
        data = request.get_json()
        new_match = Match(
            username=data.get('username'),
            categorie_match=data.get('categorie_match'),
            equipe1=data.get('equipe1'),
            equipe2=data.get('equipe2'),
            resultat=data.get('resultat')
        )
        new_match.save()
        return new_match, 201


@match_ns.route("/match/<int:id>")
class RecipieRessource(Resource):

    @match_ns.marshal_with(match_model)
    @jwt_required()
    def get(self, id):
        '''Get by id Recipie'''
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
        '''delete recipie'''
        category_to_delete = Match.query.get_or_404(id)
        category_to_delete.delete()
        return category_to_delete
