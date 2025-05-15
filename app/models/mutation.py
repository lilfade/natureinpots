from app import db
from datetime import datetime

class Mutation(db.Model):
    __tablename__ = 'mutations'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    observed_at = db.Column(db.DateTime, default=datetime.utcnow)
