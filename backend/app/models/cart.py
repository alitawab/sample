from app.extensions import db


class Cart(db.Model):
    __tablename__ = 'cart'

    cart_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='RESTRICT'), nullable=False)
    status = db.Column(db.String(45), nullable=False)

    # Relationship to User (optional but recommended)
    user = db.relationship('User', backref=db.backref('carts', lazy=True))
