from app import db
from datetime import datetime

class PlantHeight(db.Model):
    __tablename__ = 'plant_heights'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    height = db.Column(db.Float, nullable=False)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)
