from flask import Flask, request
from flask_restful import Resource, Api
from user import User, GetUser, UpdateUser, DeleteUser
from ride import RequestRide, PostRide, GetRide, UpdateRideStatus, UpdateRideRatings
from vehicle import Vehicle, GetVehicle, UpdateVehicle, DeleteVehicle

app = Flask(__name__)
api = Api(app)

#User management end points
api.add_resource(User, '/create_user')
api.add_resource(GetUser, '/get_user/<string:uid>')
api.add_resource(UpdateUser, '/update_user')
api.add_resource(DeleteUser, '/delete_user/<string:uid>')

#Vehicle management end points
api.add_resource(Vehicle, '/create_vehicle')
api.add_resource(GetVehicle, '/get_vehicle/<string:uid>')
api.add_resource(UpdateVehicle, '/update_vehicle')
api.add_resource(DeleteVehicle, '/delete_vehicle/<string:uid>')

#Ride management end points
api.add_resource(RequestRide, '/request_ride')
api.add_resource(PostRide, '/post_ride')
api.add_resource(GetRide, '/get_ride/<string:uid>')
api.add_resource(UpdateRideStatus, '/update_ride_status')
api.add_resource(UpdateRideRatings, '/update_ride_ratings')

app.run(port = 5000, debug=True)
