from flask import request, jsonify
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required
from models.model import Coupons
from models.exts import db
import random
import string

coupons_ns = Namespace('Coupons', description='namespaces Scores ')

coupons_model = coupons_ns.model(
    "Coupons",
    {
        "id": fields.Integer(),
        "username": fields.String(),
        "coupons": fields.String(),
        "nombre_de_pieces": fields.Integer(),
    }
)


@coupons_ns.route("/generateCoupons/<string:username>")
class GenerateCodeCouponsRessource(Resource):

    



    @coupons_ns.marshal_list_with(coupons_model)
    @jwt_required()
    def get(self, username):
       # print(scores)
        '''Get all matches '''
        letters_and_digits = string.ascii_uppercase + string.digits
        code = ''.join(random.choices(letters_and_digits, k=6))
        
        
        new_user = Coupons(
            username=username,
            coupons=code,
            nombre_de_pieces = 10
        )
        new_user.save()

        return new_user 
    

@coupons_ns.route("/getMyCoupons/<string:username>")
class GenerateCodeCouponsRessource(Resource):

    



    @coupons_ns.marshal_list_with(coupons_model)
    @jwt_required()
    def get(self, username):
       # print(scores)
        '''Get all matches '''
        mycoupons = Coupons.query.filter_by(username=username).first()

        return mycoupons 