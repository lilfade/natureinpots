from app import db
from datetime import datetime

class Backup(db.Model):
    __tablename__ = 'backups'
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
