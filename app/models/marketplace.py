from app import db
from datetime import datetime
from sqlalchemy import Enum
import enum

class ListingType(enum.Enum):
    direct_sale = 'direct_sale'
    auction = 'auction'
    presale = 'presale'

class MarketplaceListing(db.Model):
    __tablename__ = 'marketplace_listings'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    listing_type = db.Column(db.Enum(ListingType))
    price = db.Column(db.Float)
    status = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
