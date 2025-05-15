from app import db
from datetime import datetime

class PlantNote(db.Model):
    __tablename__ = 'plant_notes'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    note = db.Column(db.Text, nullable=False)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)
