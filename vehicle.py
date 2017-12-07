from flask import Flask, request
from flask_restful import Resource, Api

vehicles = []

class Vehicle(Resource):
    def post(self):
        data = request.get_json()
        vehicle = { 'uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851',
                 'user_uid': data['user_uid'],
                 'vehicle_type' : data['vehicle_type'],
                 'seats' : data['seats'],
                 'reg_number' : data['reg_number'],
                 'fare' : data['fare']
               }
        vehicles.append(vehicle)
        return {'status': 'success','uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851'}, 201

class GetVehicle(Resource):
    def get(self, uid):
        for vehicle in vehicles:
            if vehicle['uid'] == uid:
                return vehicle
        return {'vehicle': None}, 404

class UpdateVehicle(Resource):
    def put(self):
        data = request.get_json()
        for vehicle in vehicles:
            if vehicle['uid'] == data['uid']:
                vehicle['user_uid'] = data['user_uid']
                vehicle['vehicle_type'] = data['vehicle_type']
                vehicle['seats'] = data['seats']
                vehicle['reg_number'] = data['reg_number']
                vehicle['fare'] = data['fare']

                return {'status': 'success','uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851'}, 201
        return {'vehicle': None}, 404

class DeleteVehicle(Resource):
    def delete(self, uid):
        data = request.get_json()
        for vehicle in vehicles:
            if vehicle['uid'] == uid:
                vehicles.remove(vehicle)
                return {'status': 'success','uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851'}, 201
        return {'vehicle': None}, 404
