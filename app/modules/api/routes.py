from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models.plant import Plant
from app.models.healthscan import HealthScan
from app.models.image import PlantImage

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/plants')
@login_required
def list_plants():
    plants = Plant.query.all()
    data = [{
        'id': p.id,
        'plant_id': p.plant_id,
        'name': p.name,
        'status': p.status.name,
        'price': p.price
    } for p in plants]
    return jsonify(data)

@bp.route('/health/<int:plant_id>')
@login_required
def health_result(plant_id):
    scan = HealthScan.query.join(PlantImage).filter(PlantImage.plant_id == plant_id).order_by(HealthScan.id.desc()).first()
    if not scan:
        return jsonify({'error': 'No scan found'}), 404
    return jsonify({'score': scan.score, 'result': scan.result})

@bp.route('/upload', methods=['POST'])
@login_required
def upload_stub():
    return jsonify({'message': 'Upload endpoint stub active'}), 200
