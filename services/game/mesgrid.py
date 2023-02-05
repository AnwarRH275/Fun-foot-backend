from flask import request, jsonify
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required
from models.model import MesGrid
from models.exts import db


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
    }
)


@mesgrid_ns.route("/mesgrid/<string:categorie_match>/<string:username>")
class matchsByCategoryRessource(Resource):

    @mesgrid_ns.marshal_list_with(mesgrid_model)
    @jwt_required()
    def get(self, categorie_match, username):
        print(categorie_match)
        '''Get all matches in categorie_match'''
        mesgrid = MesGrid.query.filter_by(
            categorie_match=categorie_match, username=username).all()

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
        all_data = request.get_json()
        print(all_data)
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
                correct_resultat=data.get('correct_resultat')
            )
            new_mesgrid.save()
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
            correct_resultat=data.get('correct_resultat')
        )

        return match_to_update

    @mesgrid_ns.marshal_with(mesgrid_model)
    @jwt_required()
    def delete(self, id):
        '''delete match'''
        category_to_delete = MesGrid.query.get_or_404(id)
        category_to_delete.delete()
        return category_to_delete
