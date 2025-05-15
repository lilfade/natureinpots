from app import db

class HealthScan(db.Model):
    __tablename__ = 'health_scans'
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('plant_images.id'), nullable=False)
    score = db.Column(db.Integer)
    result = db.Column(db.Text)
