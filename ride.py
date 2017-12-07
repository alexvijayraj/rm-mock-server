from flask import Flask, request
from flask_restful import Resource, Api

rides = []

class RequestRide(Resource):
    def post(self):
        data = request.get_json()
        ride = { 'uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851',
                 'driver_uid': data['driver_uid'],
                 'rider_uid': data['rider_uid'],
                 'ride_location' : data['ride_location'],
                 'ride_time' : data['ride_time'],
                 'ride_cost' : data['ride_cost'],
                 'ride_ratings' : data['ride_ratings'],
                 'vehicle_uid' : data['vehicle_uid'],
                 'ride_status' : data['ride_status']
               }
        rides.append(ride)
        return {'status': 'success','uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851'}, 201

class PostRide(Resource):
    def post(self):
        data = request.get_json()
        ride = { 'uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851',
                 'driver_uid': data['driver_uid'],
                 'rider_uid': data['rider_uid'],
                 'ride_location' : data['ride_location'],
                 'ride_time' : data['ride_time'],
                 'ride_cost' : data['ride_cost'],
                 'ride_ratings' : data['ride_ratings'],
                 'vehicle_uid' : data['vehicle_uid'],
                 'ride_status' : data['ride_status']
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
                ride['ride_status'] = data['ride_status']

                return {'status': 'success','uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851'}, 201
        return {'user': None}, 404

class UpdateRideRatings(Resource):
    def put(self):
        data = request.get_json()
        for ride in rides:
            if ride['uid'] == data['uid']:
                ride['ride_ratings'] = data['ride_ratings']

                return {'status': 'success','uid': 'd290f1ee-6c54-4b01-90e6-d701748f0851'}, 201
        return {'user': None}, 404
