from models import db, Card

class CardService:
    def create_card(self, data):
        card_exists = Card.query.filter_by(card_number=data['card_number']).first()

        if card_exists:
            raise Exception("Card already exists.")
        else:
            card = Card(
                holder_name=data['holder_name'],
                card_number=data['card_number'],
                expiration_date=data['expiration_date'],
                cvv=data['cvv'],
                buyer_id=1,
            )

            db.session.add(card)
            db.session.commit()

            result = {
                'holder_name': card.holder_name,
                'card_number': card.card_number,
                'expiration_date': card.expiration_date,
                'cvv': card.cvv,
                'buyer_id': card.buyer_id
            }

            return result