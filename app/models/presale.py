from app import db
from datetime import datetime
from sqlalchemy import Enum
import enum

class PresaleStatus(enum.Enum):
    available = 'available'
    reserved = 'reserved'
    sold = 'sold'

class Presale(db.Model):
    __tablename__ = 'presales'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    user_email = db.Column(db.String(150), nullable=False)
    status = db.Column(db.Enum(PresaleStatus), default=PresaleStatus.available)
    reserved_date = db.Column(db.DateTime, default=datetime.utcnow)
