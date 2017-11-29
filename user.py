from flask import Flask, request
from flask_restful import Resource, Api

users = []

class User(Resource):
    def post(self):
        data = request.get_json()
        user = { 'uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851',
                 'first name' : data['first name'],
                 'last name' : data['last name'],
                 'email' : data['email'],
                 'mobile' : data['mobile'],
                 'source' : data['source'],
                 'source uid' : data['source uid'],
                 'User type' : data['User type'],
                 'vehicle uid' : data['vehicle uid']
               }
        users.append(user)
        return {'status': 'success','uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851'}, 201

class GetUser(Resource):
    def get(self, uid):
        for user in users:
            if user['uid'] == uid:
                return user
        return {'user': None}, 404

class UpdateUser(Resource):
    def put(self):
        data = request.get_json()
        for user in users:
            if user['uid'] == data['uid']:
                user['first name'] = data['first name']
                user['last name'] = data['last name']
                user['email'] = data['email']
                user['mobile'] = data['mobile']
                user['source'] = data['source']
                user['source uid'] = data['source uid']
                user['User type'] = data['User type']
                user['vehicle uid'] = data['vehicle uid']

                return {'status': 'success','uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851'}, 201
        return {'user': None}, 404

class DeleteUser(Resource):
    def delete(self, uid):
        data = request.get_json()
        for user in users:
            if user['uid'] == uid:
                users.remove(user)
                return {'status': 'success','uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851'}, 201
        return {'user': None}, 404
