from flask import Blueprint, jsonify, request

from modules.buyers.buyer_service import BuyerService

buyers = Blueprint('buyers', __name__)

@buyers.route('/buyers', methods=['POST'])
def create_buyer():
    try:
        buyerService = BuyerService()

        data = request.json

        response = buyerService.create(data)
        return jsonify(response), 201

    except Exception as err:
        return jsonify({'error': str(err)}), 400

@buyers.route('/buyers/<id>')
def find_by_id(id):
    try:
        buyerService = BuyerService()

        response = buyerService.find_by_id(id)
        return jsonify(response)

    except Exception as err:
        return jsonify({'error': str(err)}), 404
