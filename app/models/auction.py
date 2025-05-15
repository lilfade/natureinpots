from app import db
from datetime import datetime
from sqlalchemy import Enum
import enum

class AuctionStatus(enum.Enum):
    active = 'active'
    paused = 'paused'
    completed = 'completed'

class Auction(db.Model):
    __tablename__ = 'auctions'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    starting_price = db.Column(db.Float, nullable=False)
    current_highest_bid = db.Column(db.Float, nullable=True)
    highest_bidder = db.Column(db.String(150), nullable=True)
    status = db.Column(db.Enum(AuctionStatus), default=AuctionStatus.active)
    end_date = db.Column(db.DateTime, nullable=False)
