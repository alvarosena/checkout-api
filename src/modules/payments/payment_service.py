from models import db, Payment

class PaymentService:
    def create_payment(self, data, buyer_id, card_id):
        payment = Payment(amount=data['amount'], type=data['type'], buyer_id=buyer_id,card_id=card_id)

        if data['type'] == 'card':
            card = {
                'id': payment.id,
                'amount': payment.amount,
                'type': payment.type,
                'buyer_id': payment.buyer_id,
                'card_id': payment.card_id,
                'created_at': payment.created_at,
                'message': 'successful'
            }

            db.session.add(payment)
            db.session.commit()

            return card

        else:
            ticket = {
                'id': payment.id,
                'amount': payment.amount,
                'type': payment.type,
                'buyer_id': payment.buyer_id,
                'card_id': payment.card_id,
                'created_at': payment.created_at,
                'ticket_number': '00000000000000000'
            }

            db.session.add(payment)
            db.session.commit()

            return ticket