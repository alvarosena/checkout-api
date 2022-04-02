from models import db, Buyer

class BuyerService:
    def create(self, data):
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
            return {'error': 'Buyer not found.'}
        else:
            result = {
                "id": buyer.id,
                "name": buyer.name,
                "cpf": buyer.cpf,
                "created_at": str(buyer.created_at)
            }

            return result