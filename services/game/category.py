from flask import request, jsonify
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required
from models.model import Category
from models.exts import db


category_ns = Namespace('category', description='namespaces categorie match ')

'''
id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_match = db.Column(db.String(100), nullable=False)
    categorie_match = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    heure = db.Column(db.String(100), nullable=False)

'''

# model (serializer)
category_model = category_ns.model(
    "Categorie",
    {
        "id": fields.Integer(),
        "numero_match": fields.String(),
        "categorie_match": fields.String(),
        "description": fields.String(),
        "date": fields.String(),
        "heure": fields.String(),
    }
)


@category_ns.route("/Categories")
class categoryRessource(Resource):

    @category_ns.marshal_list_with(category_model)
    @jwt_required()
    def get(self):
        '''Get all Category'''
        recipies = Category.query.all()
        return recipies

    @category_ns.marshal_with(category_model)
    @category_ns.expect(category_model)
    @jwt_required()
    def post(self):
        '''Create new Category'''
        data = request.get_json()
        new_category = Category(
            numero_match=data.get('numero_match'),
            categorie_match=data.get('categorie_match'),
            description=data.get('description'),
            date=data.get('date'),
            heure=data.get('heure')
        )
        new_category.save()
        return new_category, 201


@category_ns.route("/Category/<int:id>")
class RecipieRessource(Resource):

    @category_ns.marshal_with(category_model)
    @jwt_required()
    def get(self, id):
        '''Get by id Recipie'''
        category = Category.query.get_or_404(id)

        return category

    @category_ns.marshal_with(category_model)
    @jwt_required()
    def put(self, id):
        '''update category'''
        print(id)
        data = request.get_json()
        print(data)
        category_to_update = Category.query.get_or_404(id)
        data = request.get_json()

        category_to_update.update(

            numero_match=data.get('numero_match'),
            categorie_match=data.get('categorie_match'),
            description=data.get('description'),
            date=data.get('date'),
            heure=data.get('heure')
        )

        return category_to_update

    @category_ns.marshal_with(category_model)
    @jwt_required()
    def delete(self, id):
        '''delete recipie'''
        category_to_delete = Category.query.get_or_404(id)
        category_to_delete.delete()
        return category_to_delete
