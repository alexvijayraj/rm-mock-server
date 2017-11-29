from flask import Flask, request
from flask_restful import Resource, Api

vehicles = []

class Vehicle(Resource):
    def post(self):
        data = request.get_json()
        vehicle = { 'uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851',
                 'User uid': data['User uid'],
                 'Vehicle type' : data['Vehicle type'],
                 'seats' : data['seats'],
                 'Reg number' : data['Reg number'],
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
                vehicle['User uid'] = data['User uid']
                vehicle['Vehicle type'] = data['Vehicle type']
                vehicle['seats'] = data['seats']
                vehicle['Reg number'] = data['Reg number']
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
