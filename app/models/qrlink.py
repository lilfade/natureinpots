from app import db
from datetime import datetime

class QRLink(db.Model):
    __tablename__ = 'qr_links'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    qr_code = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
