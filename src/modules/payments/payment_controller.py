from crypt import methods
from flask import Blueprint, jsonify, request

from modules.payments.payment_service import PaymentService

payments = Blueprint('payments', __name__)

@payments.route('/payments/<buyer_id>/<card_id>', methods=['POST'])
def create_payment(buyer_id, card_id):
    try:
        paymentService = PaymentService()

        data = request.json

        response = paymentService.create_payment(data, buyer_id, card_id)
        return jsonify(response), 201
    except Exception as err:
        return jsonify({'error': str(err)}), 400
