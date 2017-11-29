from flask import Flask, request
from flask_restful import Resource, Api

rides = []

class RequestRide(Resource):
    def post(self):
        data = request.get_json()
        ride = { 'uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851',
                 'Driver uid': data['Driver uid'],
                 'Rider uid': data['Rider uid'],
                 'Ride location' : data['Ride location'],
                 'Ride time' : data['Ride time'],
                 'Ride cost' : data['Ride cost'],
                 'Ride ratings' : data['Ride ratings'],
                 'vehicle uid' : data['vehicle uid'],
                 'Ride status' : data['Ride status']
               }
        rides.append(ride)
        return {'status': 'success','uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851'}, 201

class PostRide(Resource):
    def post(self):
        data = request.get_json()
        ride = { 'uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851',
                 'Driver uid': data['Driver uid'],
                 'Rider uid': data['Rider uid'],
                 'Ride location' : data['Ride location'],
                 'Ride time' : data['Ride time'],
                 'Ride cost' : data['Ride cost'],
                 'Ride ratings' : data['Ride ratings'],
                 'vehicle uid' : data['vehicle uid'],
                 'Ride status' : data['Ride status']
               }
        rides.append(ride)
        return {'status': 'success','uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851'}, 201

class GetRide(Resource):
    def get(self, uid):
        for ride in rides:
            if ride['uid'] == uid:
                return ride
        return {'ride': None}, 404

class UpdateRideStatus(Resource):
    def put(self):
        data = request.get_json()
        for ride in rides:
            if ride['uid'] == data['uid']:
                ride['Ride status'] = data['Ride status']

                return {'status': 'success','uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851'}, 201
        return {'user': None}, 404

class UpdateRideRatings(Resource):
    def put(self):
        data = request.get_json()
        for ride in rides:
            if ride['uid'] == data['uid']:
                ride['Ride ratings'] = data['Ride ratings']

                return {'status': 'success','uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851'}, 201
        return {'user': None}, 404
