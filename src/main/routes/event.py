"""
    Register  new rotes for events using blueprint
"""
from flask import Blueprint, jsonify


event_route_bp = Blueprint("event_route", __name__)
@event_route_bp.route("/event",methods=["POST"])
def create_new_event():
    """
        Create route to create new events
    """
    return jsonify({"estou": "aqui"}),201
