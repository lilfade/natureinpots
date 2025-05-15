from app import db
from datetime import datetime

class PlantImage(db.Model):
    __tablename__ = 'plant_images'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    image_url = db.Column(db.String(300), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
