from flask import request, jsonify
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required
from models.model import Scores
from models.exts import db


scores_ns = Namespace('Scores', description='namespaces Scores ')

'''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   

'''

# model (serializer)
scores_model = scores_ns.model(
    "Scores",
    {
        "id": fields.Integer(),

        "username": fields.String(),

        "scores": fields.Integer(),
    }
)


@scores_ns.route("/scores/<string:username>")
class scoresByUsernameRessource(Resource):

    @scores_ns.marshal_list_with(scores_model)
    @jwt_required()
    def get(self, username):
       # print(scores)
        '''Get all matches '''
        scores = Scores.query.filter_by(username=username).first()

        return scores

    @scores_ns.marshal_with(scores_model)
    @jwt_required()
    def put(self, username):
        '''update scores'''

        scores_to_update = Scores.query.filter_by(
            username=username).first_or_404()
        data = request.get_json()

        scores_to_update.update(

            username=data.get('username'),

            scores=data.get('scores')
        )

        return scores_to_update


@scores_ns.route("/scores")
class scoresRessource(Resource):

    @scores_ns.marshal_list_with(scores_model)
    @jwt_required()
    def get(self):
        '''Get all '''
        scores = Scores.query.all()

        return scores

    @scores_ns.marshal_with(scores_model)
    @scores_ns.expect(scores_model)
    @jwt_required()
    def post(self):
        '''Create new Scores'''
        data = request.get_json()
        new_match = Scores(

            username=data.get('username'),
            scores=data.get('scores')
        )
        new_match.save()
        return new_match, 201


@scores_ns.route("/scores/<int:id>")
class scoresRessource(Resource):

    @scores_ns.marshal_with(scores_model)
    @jwt_required()
    def get(self, id):
        ''' Get by id scores '''
        match = Scores.query.get_or_404(id)
        return match

    @scores_ns.marshal_with(scores_model)
    @jwt_required()
    def put(self, id):
        '''update scores'''

        scores_to_update = Scores.query.get_or_404(id)
        data = request.get_json()

        scores_to_update.update(

            username=data.get('username'),

            scores=data.get('scores')
        )

        return scores_to_update

    @scores_ns.marshal_with(scores_model)
    @jwt_required()
    def delete(self, id):
        '''delete match'''
        scores_to_delete = Scores.query.get_or_404(id)
        scores_to_delete.delete()
        return scores_to_delete
