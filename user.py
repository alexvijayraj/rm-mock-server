from flask import Flask, request
from flask_restful import Resource, Api

users = []

class User(Resource):
    def post(self):
        data = request.get_json()
        user = { 'uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851',
                 'first_name' : data['first_name'],
                 'last_name' : data['last_name'],
                 'email' : data['email'],
                 'mobile' : data['mobile'],
                 'source' : data['source'],
                 'source_uid' : data['source_uid'],
                 'user_type' : data['user_type'],
                 'rating' : data['rating'],
                 'vehicle_uid' : data['vehicle_uid'],
                 'user_status' : data['user_status']
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
                user['first_name'] = data['first_name']
                user['last_name'] = data['last_name']
                user['email'] = data['email']
                user['mobile'] = data['mobile']
                user['source'] = data['source']
                user['source_uid'] = data['source_uid']
                user['user_type'] = data['user_type']
                user['rating'] = data['rating']
                user['vehicle_uid'] = data['vehicle_uid']
                user['user_status'] = data['user_status']

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
