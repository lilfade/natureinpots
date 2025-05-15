from app import db
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Enum
import enum

class PlantStatus(enum.Enum):
    not_for_sale = 'Not For Sale'
    for_sale = 'For Sale'
    sold = 'Sold'
    presale = 'Presale'
    auction = 'Auction'
    private = 'Private Collection'

class MarketplaceStatus(enum.Enum):
    private = 'private'
    unlisted = 'unlisted'
    public = 'public'

class Plant(db.Model):
    __tablename__ = 'plants'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    scientific_name = db.Column(db.String(150))
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=True)
    initial_price = db.Column(db.Float, nullable=True)
    status = db.Column(db.Enum(PlantStatus), default=PlantStatus.not_for_sale)
    marketplace_status = db.Column(db.Enum(MarketplaceStatus), default=MarketplaceStatus.private)
    image_url = db.Column(db.String(300), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
