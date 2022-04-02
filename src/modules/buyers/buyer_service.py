from models import db, Buyer

class BuyerService:

    def create(self, data):
        buyer = Buyer(name=data['name'], email=data['email'], cpf=data['cpf'])
        db.session.add(buyer)
        db.session.commit()

        result = Buyer.query.filter_by(email=buyer['email']).first()
        return result