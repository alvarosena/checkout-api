from models import db, Buyer

class BuyerService:
    def create(self, data):
        buyer_exists = Buyer.query.filter_by(email=data['email']).first()

        if buyer_exists:
            raise Exception('Buyer already exists.')
        else:
            buyer = Buyer(name=data['name'], email=data['email'], cpf=data['cpf'])
            db.session.add(buyer)
            db.session.commit()

            result = {
                "id": buyer.id,
                "name": buyer.name,
                "cpf": buyer.cpf,
                "created_at": str(buyer.created_at)
            }

            return result

    def find_by_id(self, id):
        buyer = Buyer.query.filter_by(id=id).first()

        if not buyer:
            raise Exception('Buyer not found!')
        else:
            result = {
                "id": buyer.id,
                "name": buyer.name,
                "cpf": buyer.cpf,
                "created_at": str(buyer.created_at)
            }

            return result