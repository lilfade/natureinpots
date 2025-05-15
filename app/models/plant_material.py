from app import db

class PlantMaterial(db.Model):
    __tablename__ = 'plant_materials'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    link = db.Column(db.String(300), nullable=True)
