from flask import Blueprint, jsonify, request

from modules.cards.card_service import CardService

cards = Blueprint('cards', __name__)

@cards.route('/cards', methods=['POST'])
def create_card():
    try:
        cardService = CardService()
        data = request.json

        response = cardService.create_card(data)

        return jsonify(response), 201

    except Exception as err:
        return jsonify({'error': str(err)}), 400
